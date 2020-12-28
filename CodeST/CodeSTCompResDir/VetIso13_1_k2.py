
#comparação entre Fibras na Vertical com Isotrópico 0.53
#Os plots ficarão aqui, e quando quiser plotar um, deixo o outro comentado
#Fibras na Vertical usando o Diretório, como fonte do código vertical

#Antes de rodar, verificar do Isotrópico K2 ST, e Vertical e nesse codigo:
#Tamanho de malha
#Valor do q do fluxo de calor
#Valor da constante ColunaTumorComp, no final dos dois códigos


import CodeST.CodeSTCompResDir.TccCode13_1_k2
import CodeST.CodeSTCompResDir.TccCode13_1_FV_Principal

#Isotrópico K2 ST
D_13_1_k2_RLine2 = CodeST.CodeSTCompResDir.TccCode13_1_k2.D_13_1_k2_RLine
#Fibras na Vertical ST
D_13_1_FV_RLine2 = CodeST.CodeSTCompResDir.TccCode13_1_FV_Principal.D_13_1_FV_RLine



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
plt.plot(eixox, D_13_1_k2_RLine2, marker='^', label='Isotrópico K = 0.53')
plt.plot(eixox, D_13_1_FV_RLine2, marker='s', label='Fibras na Vertical')
plt.ylabel('T[°C]', fontsize=25)
# o título para o trabalho sai, mas deixar por enquanto para facilitar
#plt.title('VetIso13_1_k1, com '+ str(nr) + ' volumes paralelos em r', fontsize=20)
plt.xlabel('Eixo r [m]', fontsize=22)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.show()
"""

#plot de diferença percentual

Diff_1_k1_k2 = []
eixox = numpy.linspace(ra, R, nr)
for i in range(len(eixox)):
    Diff_1_k1_k2.append(math.fabs((D_13_1_k2_RLine2[i] - D_13_1_FV_RLine2[i]))/ D_13_1_k2_RLine2[i] * 100)

PercDiff = Diff_1_k1_k2.copy()
plt.ylabel('Valores percentuais', fontsize=25)
plt.plot(eixox, PercDiff)
#plt.title('VetIso13_1_k2, , Malha de '+ str(nr) + ' volumes', fontsize=25)
plt.xlabel('Eixo r [m]', fontsize=21)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

