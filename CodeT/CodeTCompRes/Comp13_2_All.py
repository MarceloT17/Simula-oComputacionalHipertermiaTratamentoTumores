
#comparação entre os dois Isotrópicos, o Vertical, e o Horizontal, T
#Os plots ficarão aqui, e quando quiser plotar um, deixo os outros comentados

#Antes de rodar, verificar os quatro códigos, Dois Isotrópicos, o Vertical e o Horizontal, e esse código:
#Tamanho de malha
#Valor do q do fluxo de calor
#Valor da constante ColunaTumorComp, no final dos dois códigos

import CodeT.CodeTCompRes.TccCode13_2_k1
import CodeT.CodeTCompRes.TccCode13_2_k2
#Isotrópico K1 T
D_13_2_k1_RLine2 = CodeT.CodeTCompRes.TccCode13_2_k1.D_13_2_k1_RLine
#Isotrópico K2 T
D_13_2_k2_RLine2 = CodeT.CodeTCompRes.TccCode13_2_k2.D_13_2_k2_RLine
import CodeT.CodeTCompRes.TccCode13_2_FH
#Fibras na Horizontal T
D_13_2_FH_RLine2 = CodeT.CodeTCompRes.TccCode13_2_FH.D_13_2_FH_RLine
import CodeT.CodeTCompRes.TccCode13_2_FV
#Fibras na Vertical T
D_13_2_FV_RLine2 = CodeT.CodeTCompRes.TccCode13_2_FV.D_13_2_FV_RLine




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
eixox = numpy.linspace(ra, R, nr)
plt.plot(eixox, D_13_2_k1_RLine2, marker='o', label='Isotrópico K = 0.485, Com Tumor')
plt.plot(eixox, D_13_2_k2_RLine2, marker='^', label='Isotrópico K = 0.53, Com Tumor')
plt.plot(eixox, D_13_2_FH_RLine2, marker='s', label='Fibras na Horizontal, Com Tumor')
plt.plot(eixox, D_13_2_FV_RLine2, marker='p', label='Fibras na Vertical, Com Tumor')
# o título para o trabalho sai, mas deixar por enquanto para facilitar
#plt.title('Comp13_2_All, com '+ str(nr) + ' volumes paralelos em r', fontsize=20)
plt.xlabel("Eixo r [m]", fontsize=21)
plt.ylabel('T[°C]', fontsize=25)

plt.xlabel('Eixo r [m]', fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.show()
