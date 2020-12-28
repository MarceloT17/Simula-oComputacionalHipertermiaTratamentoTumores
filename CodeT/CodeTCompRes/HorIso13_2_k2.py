
#comparação entre Fibras na Horizontal com Isotrópico 0.485
#Os plots ficarão aqui, e quando quiser plotar um, deixo o outro comentado

#Antes de rodar, verificar do Isotrópico K2 T, e Horizontal, e esse código:
#Tamanho de malha
#Valor do q do fluxo de calor
#Valor da constante ColunaTumorComp, no final dos dois códigos

import CodeT.CodeTCompRes.TccCode13_2_FH
import CodeT.CodeTCompRes.TccCode13_2_k2
#Fibras na Horizontal T
D_13_2_FH_RLine2 = CodeT.CodeTCompRes.TccCode13_2_FH.D_13_2_FH_RLine
#Isotrópico K2 T
D_13_2_k2_RLine2 = CodeT.CodeTCompRes.TccCode13_2_k2.D_13_2_k2_RLine


#plot
import numpy
import math
import matplotlib.pyplot as plt
import seaborn
nr = 80  # valores pares
nz = 100
R = 0.03
ra = 0.01
# Os dois plots aqui, quando quiser um, só tirar do comentário

#plot de linhas sobrepostas
"""eixox = numpy.linspace(ra, R, nr)
plt.plot(eixox, D_13_2_k2_RLine2, marker='^', label='Isotrópico K = 0.53, Com Tumor')
plt.plot(eixox, D_13_2_FH_RLine2, marker='s', label='Fibas na Horizontal, Com Tumor')
plt.ylabel('T[°C]', fontsize=25)
# o título para o trabalho sai, mas deixar por enquanto para facilitar
#plt.title('HorIso13_2_k2, com '+ str(nr) + ' volumes paralelos em r', fontsize=20)
plt.xlabel('Eixo r [m]', fontsize=21)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.show()
"""

#plot de diferença percentual
Diff_2_k1_k2 = []
eixox = numpy.linspace(ra, R, nr)
for i in range(len(eixox)):
    Diff_2_k1_k2.append(math.fabs((D_13_2_k2_RLine2[i] - D_13_2_FH_RLine2[i]))/ D_13_2_k2_RLine2[i] * 100)

PercDiff = Diff_2_k1_k2.copy()
plt.ylabel('Valores percentuais', fontsize=20)
plt.plot(eixox, PercDiff)
#plt.title('HorIso13_2_k2, , Malha de '+ str(nr) + ' volumes', fontsize=20)
plt.xlabel('Eixo r [m]', fontsize=25)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.show()
