import matplotlib.pyplot as plt
import numpy as np

fig, [[arriba_iz, arriba_cnt, arriba_dr], [abajo_iz, abajo_cnt, abajo_dr]] = plt.subplots(2, 3)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55, wspace=0.55)
plt.suptitle('Figuras variables: 2 filas de 3 graficas')

plt.sca(arriba_iz)
plt.plot([1,2,3,4])
plt.xlabel('Una lista')

plt.sca(arriba_cnt)
plt.plot(range(12), range(12,0,-1), linestyle='dotted')
plt.xlabel('Dos listas')

plt.sca(arriba_dr)
x = np.arange(0.0, 1.0, 0.01)
plt.plot(x,np.sin(2*np.pi*x), linestyle='dashed')
plt.xlabel('Funcion')

plt.sca(abajo_iz)
plt.plot(range(10), range(0,20,2), 'yo')
plt.xticks(range(10), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j'])

plt.sca(abajo_cnt)
x = np.arange(-1.0, 1.0, 0.02)
plt.plot(x, x**2, 'r', linestyle='dashdot')

plt.subplot(236, facecolor='g')
plt.plot([0,1], "y:", [1,0], "r", x, np.sin(2*np.pi*x), "m--")
plt.title('Grafico verde')

plt.savefig("Figuras_Variadas")
plt.show()