#comparação entre Fibras na Horizontal e Verticais
#Os plots ficarão aqui, e quando quiser plotar um, deixo o outro comentado
#Fibras na Horizontal usando o Diretório

#Antes de rodar, verificar do Vertical T, e Horizontal T, e esse código:
#Tamanho de malha
#Valor do q do fluxo de calor
#Valor da constante ColunaTumorComp, no final dos dois códigos


import CodeT.CodeTCompRes.TccCode13_2_FV
import CodeT.CodeTCompRes.TccCode13_2_FH
#Fibras na Vertical T
D_13_2_FV_RLine2 = CodeT.CodeTCompRes.TccCode13_2_FV.D_13_2_FV_RLine
#Fibras na Horizontal T
D_13_2_FH_RLine2 = CodeT.CodeTCompRes.TccCode13_2_FH.D_13_2_FH_RLine



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
plt.plot(eixox, D_13_2_FV_RLine2, marker='s', label='Fibras na Vertical')
plt.plot(eixox, D_13_2_FH_RLine2, marker='p', label='Fibras na Horizontal')
plt.ylabel('T[°C]', fontsize=25)
# o título para o trabalho sai, mas deixar por enquanto para facilitar
#plt.title('VetHor13_2, com '+ str(nr) + ' volumes paralelos em r')
plt.xlabel('Eixo r [m]', fontsize=21)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.show()
"""

#plot de diferença percentual
Diff_1_k1_k2 = []
eixox = numpy.linspace(ra, R, nr)
for i in range(len(eixox)):
    Diff_1_k1_k2.append(math.fabs((D_13_2_FV_RLine2[i] - D_13_2_FH_RLine2[i]))/ D_13_2_FV_RLine2[i] * 100)

PercDiff = Diff_1_k1_k2.copy()
plt.ylabel('Valores percentuais', fontsize=25)
plt.plot(eixox, PercDiff)
#plt.title('VetHor13_2, , Malha de '+ str(nr) + ' volumes')
plt.xlabel('Eixo r [m]', fontsize=21)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
