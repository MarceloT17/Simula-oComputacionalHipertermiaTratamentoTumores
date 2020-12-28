
#comparação entre o Isotrópico 0.485 e Isotrópico 0.53
#Os plots ficarão aqui, e quando quiser plotar um, deixo o outro comentado

#Antes de rodar, verificar do Isotrópico K1 T, e Isotrópico K2 T:
#Tamanho de malha
#Valor do q do fluxo de calor
#Valor da constante ColunaTumorComp, no final dos dois códigos

import CodeT.CodeTCompRes.TccCode13_2_k1
import CodeT.CodeTCompRes.TccCode13_2_k2
#Isotrópico K1 T
D_13_2_k1_RLine2 = CodeT.CodeTCompRes.TccCode13_2_k1.D_13_2_k1_RLine
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
plt.plot(eixox, D_13_2_k1_RLine2, marker='o', label='Isotrópico K = 0.485, com Tumor')
plt.plot(eixox, D_13_2_k2_RLine2, marker='^', label='Isotrópico K = 0.53, com Tumor')
plt.ylabel('T[°C]', fontsize=25)
# o título para o trabalho sai, mas deixar por enquanto para facilitar
#plt.title('Iso13_2_k1_k2, com '+ str(nr) + ' volumes paralelos em r', fontsize=20)
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
    Diff_1_k1_k2.append(math.fabs((D_13_2_k1_RLine2[i] - D_13_2_k2_RLine2[i]))/ D_13_2_k1_RLine2[i] * 100)

PercDiff = Diff_1_k1_k2.copy()
plt.ylabel('Valores percentuais', fontsize=25)
plt.plot(eixox, PercDiff)
#plt.title('Iso13_2_k1_k2, , Malha de '+ str(nr) + ' volumes', fontsize=20)
plt.xlabel('Eixo r [m]', fontsize=21)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.show()

