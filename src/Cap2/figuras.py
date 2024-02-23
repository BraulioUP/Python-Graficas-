import matplotlib.pyplot as plt

fig, [[arriba_iz, arriba_cnt, arriba_dr], [abajo_iz, abajo_cnt, abajo_dr]] = plt.subplots(2, 3)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55, wspace=0.55)
plt.suptitle('Figuras variables: 2 filas de 3 graficas')

plt.sca(arriba_iz)
plt.plot([1,2,3,4])
plt.xlabel('Una lista')

plt.sca(arriba_cnt)
plt.plot(range(12), range(12,0,-1), linestyle='dotted')
plt.xlabel('Dos listas')


plt.show()
