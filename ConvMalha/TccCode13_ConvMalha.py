
import numpy
import math
import matplotlib.pyplot as plt
import seaborn
nr = 80  # valores pares
nz = 100
R = 0.03
ra = 0.01
#conferir valores
eps_Max = [9.29643E-5, 0.000124461, 8.54142E-05, 6.79675E-05, 0.000228217, 0.00031864]
eps_Min = [6.00671E-05, 8.47309E-05, -6.38995E-05, 5.62134E-05, 0.000227028, 0.000367592]
eps_Avg = [7.47171E-05, 0.000102387, 7.35746E-05, 6.16993E-05, 0.000229918, 0.000351262]

eixox = [2, 3, 4, 5, 6, 7]

plt.plot(eixox, eps_Max, marker='s', label='eps Máximo')
plt.plot(eixox, eps_Min, marker='D', label='eps Mínimo')
plt.plot(eixox, eps_Avg, marker='o', label='eps Average')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.show()


