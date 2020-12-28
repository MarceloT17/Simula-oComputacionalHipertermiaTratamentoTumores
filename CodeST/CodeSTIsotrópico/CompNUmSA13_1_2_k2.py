#Isotropico com k = 0.53, e sem tumor
# 1 significa sem tumor
#Dois plots: diferença percentual, e soluções sobrepostas
#Quando quiser um plot, comentar o outro

import numpy
import math
import matplotlib.pyplot as plt
import seaborn
import CodeST.CodeSTIsotropico.TccCode13_SA_1_k2
import CodeST.CodeSTIsotropico.TccCode13_Num_1_k2

nr = 80 #valores pares
R = 0.03
ra = 0.01


#plot de diferença percentual
eixor = numpy.linspace(ra, R, nr)
DSa3 = CodeST.CodeSTIsotropico.TccCode13_Num_1_k2.DSA
T4 = CodeST.CodeSTIsotropico.TccCode13_SA_1_k2.T3
D5 = []
for i in range(len(eixor)):
    D5.append((T4[i] - DSa3[i])/ T4[i] * 100)

PDiff = D5
plt.ylabel('Valores percentuais', fontsize=25)
plt.plot(eixor, PDiff)
#plt.title('CompNumSA_13_1_2_k2, , Malha de '+ str(nr) + ' volumes', fontsize=20)
plt.xlabel("Eixo z [m]", fontsize=21)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.show()


#plot de soluções sobrepostas
"""eixor = numpy.linspace(ra, R, nr)
DSa3 = CodeST.CodeSTIsotropico.TccCode13_Num_1_k2.DSA
T4 = CodeST.CodeSTIsotropico.TccCode13_SA_1_k2.T3
plt.plot(eixor, DSa3, marker='o', label='Solução Numérica')
plt.plot(eixor, T4, marker='^', label='Solução Analítica')
plt.ylabel('T[°C]', fontsize=25)
plt.xlabel("Eixo z [m]", fontsize=21)
plt.ylim(60, 70)
#plt.title('CompNumSA_13_1_k2, , Malha de '+ str(nr) + ' volumes', fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
#plt.legend()
plt.show()
"""
