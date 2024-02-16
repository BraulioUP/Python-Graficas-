import os
import time
import datetime
import numpy as np
import random
from tqdm import tqdm
import torch
from torch.utils.data import Dataset, DataLoader, random_split, RandomSampler
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AdamW, get_linear_schedule_with_warmup

seed_val = 42
random.seed(seed_val)
np.random.seed(seed_val)

if torch.cuda.is_available():
    print("Usar GPU")
    torch.manual_seed(seed_val)
    torch.cuda.manual_seed_all(seed_val)
    device = torch.device("cuda")
    batch_size = 3

else:
    print("usar CPU")
    device = torch.device("cpu")
    batch_size = 1

tokenizer = AutoTokenizer.from_pretrained("flax-community/gpt-2-spanish", bos_token='<|startoftext|>', eos_token='<|endoftext|>', pad_token='<|pad|>')

model = AutoModelForCausalLM.from_pretrained("flax-community/gpt-2-spanish")

control_code = "ibai"

special_tokens_dict = {
         "additional_special_tokens": ['f"<|{control_code}|>"'],
}
num_added_toks = tokenizer.add_special_tokens(special_tokens_dict)
model.resize_token_embeddings(len(tokenizer))
unk_tok_emb = model.transformer.wte.weight.data[tokenizer.unk_token_id, :]
for i in range(num_added_toks):
        model.transformer.wte.weight.data[-(i+1), :] = unk_tok_emb
        
        
class GPT2Dataset(Dataset):

  def __init__(self, control_code, tokenizer, archivo_texto = 'all.txt', max_length=768):

    self.tokenizer = tokenizer
    self.input_ids = []
    self.attn_masks = []

    print('loading text...')
    sentences = open(archivo_texto, 'r', encoding="utf-8").read().lower().split('\n')
    print('qty:',len(sentences))

    for row in tqdm(sentences):
      encodings_dict = tokenizer('<|startoftext|>'+ f"<|{control_code}|>" + row + '<|endoftext|>', truncation=True, max_length=max_length, padding="max_length")
      self.input_ids.append(torch.tensor(encodings_dict['input_ids']))
      self.attn_masks.append(torch.tensor(encodings_dict['attention_mask']))
    
  def __len__(self):
    return len(self.input_ids)

  def __getitem__(self, idx):
    return self.input_ids[idx], self.attn_masks[idx] 
  
  
dataset = GPT2Dataset(control_code, tokenizer, archivo_texto="ibai_textos.txt", max_length=768)

train_size = int(0.99 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

print('{:>5,} training samples'.format(train_size))
print('{:>5,} validation samples'.format(val_size))

train_dataloader = DataLoader(
            train_dataset,
            sampler = RandomSampler(train_dataset),
            batch_size = batch_size
        )

epochs = 1
learning_rate = 1e-5
warmup_steps = 1e2
epsilon = 1e-8
sample_every = 500
optimizer = AdamW(model.parameters(),
                  lr = learning_rate,
                  eps = epsilon,
                  no_deprecation_warning=True
                )
total_steps = len(train_dataloader) * epochs

scheduler = get_linear_schedule_with_warmup(optimizer, 
                                            num_warmup_steps = warmup_steps, 
                                            num_training_steps = total_steps)

def format_time(elapsed):
    return str(datetime.timedelta(seconds=int(round((elapsed)))))
  
  
  
  
total_t0 = time.time()

model = model.to(device)

for epoch_i in range(0, epochs):
    print("")
    print('======== Epoch {:} / {:} ========'.format(epoch_i + 1, epochs))
    print('Training...')

    t0 = time.time()
    total_train_loss = 0

    model.train()

    for step, batch in enumerate(train_dataloader):

        b_input_ids = batch[0].to(device)
        b_labels = batch[0].to(device)
        b_masks = batch[1].to(device)

        model.zero_grad()        

        outputs = model(  b_input_ids,
                          labels=b_labels, 
                          attention_mask = b_masks,
                          token_type_ids=None
                        )

        loss = outputs[0]
        batch_loss = loss.item()
        total_train_loss += batch_loss

        if step % sample_every == 0 and not step == 0:

            elapsed = format_time(time.time() - t0)
            print('  Batch {:>5,}  of  {:>5,}. Loss: {:>5,}.   Elapsed: {:}.'.format(step, len(train_dataloader), batch_loss, elapsed))

            model.eval()

            sample_outputs = model.generate(
                                    bos_token_id=random.randint(1,30000),
                                    do_sample=True,   
                                    top_k=50, 
                                    max_length = 200,
                                    top_p=0.95, 
                                    num_return_sequences=1
                                )
            for i, sample_output in enumerate(sample_outputs):
                  print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))
            
            model.train()

        loss.backward()
        optimizer.step()
        scheduler.step()

    avg_train_loss = total_train_loss / len(train_dataloader)
    
    training_time = format_time(time.time() - t0)

    print("")
    print("  Average training loss: {0:.2f}".format(avg_train_loss))
    print("  Training epoch took: {:}".format(training_time))
    
    t0 = time.time()

    total_eval_loss = 0
    nb_eval_steps = 0

print("")
print("Training complete!")
print("Total training took {:} (h:mm:ss)".format(format_time(time.time()-total_t0)))

output_dir = './model_gpt_ibai/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Saving model to %s" % output_dir)

model_to_save = model.module if hasattr(model, 'module') else model 
model_to_save.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

model.eval()

prompt = "<|startoftext|>" + "<|"+control_code+"|>" + "¿ qué es el fútbol ?"

generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
generated = generated.to(device)

sample_outputs = model.generate(
                                generated, 
                                do_sample=True,   
                                top_k=50, 
                                max_length = 300,
                                top_p=0.95, 
                                num_return_sequences=8
                                )

for i, sample_output in enumerate(sample_outputs):
  print("{}: {}\n\n".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))