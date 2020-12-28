
#comparação entre os dois Isotrópicos, o Vertical, e o Horizontal, ST
#Os plots ficarão aqui, e quando quiser plotar um, deixo os outros comentados

#Antes de rodar, verificar os quatro códigos, Dois Isotrópicos, o Vertical e o Horizontal, e esse código:
#Tamanho de malha
#Valor do q do fluxo de calor
#Valor da constante ColunaTumorComp, no final dos dois códigos

import CodeST.CodeSTCompResDir.TccCode13_1_k1
import CodeST.CodeSTCompResDir.TccCode13_1_k2
import CodeST.CodeSTCompResDir.TccCode13_1_FV_Principal
import CodeST.CodeSTCompResDir.TccCode13_1_FH

#Isotrópico K1 ST
D_13_1_k1_RLine2 = CodeST.CodeSTCompResDir.TccCode13_1_k1.D_13_1_k1_RLine
#Isotrópico K2 ST
D_13_1_k2_RLine2 = CodeST.CodeSTCompResDir.TccCode13_1_k2.D_13_1_k2_RLine
#Fibras na Vertical ST
D_13_1_FV_RLine2 = CodeST.CodeSTCompResDir.TccCode13_1_FV_Principal.D_13_1_FV_RLine
#Fibras na Horizontal ST
D_13_1_FH_RLine2 = CodeST.CodeSTCompResDir.TccCode13_1_FH.D_13_1_FH_RLine


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
plt.plot(eixox, D_13_1_k1_RLine2, marker='o', label='Isotrópico K = 0.485')
plt.plot(eixox, D_13_1_k2_RLine2, marker='^', label='Isotrópico K = 0.53')
plt.plot(eixox, D_13_1_FV_RLine2, marker='s', label='Fibras na Vertical')
plt.plot(eixox, D_13_1_FH_RLine2, marker='p', label='Fibras na Horizontal')
# o título para o trabalho sai, mas deixar por enquanto para facilitar
#plt.title('Comp13_1_All, com '+ str(nr) + ' volumes paralelos em r', fontsize=20)
plt.xlabel("Eixo r [m]", fontsize=21)
plt.ylabel('T[°C]', fontsize=25)

plt.xlabel('Eixo r [m]', fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
plt.show()



