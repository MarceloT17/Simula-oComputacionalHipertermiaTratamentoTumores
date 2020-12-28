
# TccCode13_1_FV com o plot em formato de comentário
# Variável armazena a coluna de D, e o código de comparação pega para plotar
#Vertical com k = 0.485, e sem tumor
# 1 significa sem tumor

#Fibras na Vertical usando o Diretório

#Colar o TccCode13_1_FV, do Diretório CodeSTFibrasVertical, do pacote CodeSTIsotrópico
#verificar o código, para comparar
#comentar o plot
#trocar o código daqui-------------------
# Quando plotar o novo código, comentar o plot
#-------------------------------
#------------------------------------------------------------------------------------------------------------------




#Fibras na Vertical com k11 = 0.485, k22 = 0.53, e sem tumor
# 1 significa sem tumor
#along em r, e across em z

#tempo para rodar o código
import time
start = time.time()


import numpy
import math
import matplotlib.pyplot as plt
import seaborn

nr = 80 # valores pares
nz = 100

T = numpy.zeros([nr, nz], dtype=float)

Z = 0.1
R = 0.03
ra = 0.01

ro = 1050
c = 3617
Ta = 37

h = 10.0
Tinf = 23.0

#k11=0.485 para W e E
#k22=0.53 para S e N
#Na condicao de contorno fica em r aqui, e assim k11, podendo ser como ke, como está

def calculo(E):
    for i in range(0, nr, 1):

        ke = 0.485
        kw = 0.485
        ks = 0.53
        kn = 0.53
        gm = 991.9
        w = 0.0006722

        for j in range(0, nz, 1):

            an = ((((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * kn * ((R - ra) / nr)) / (Z / nz)
            asul = ((((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ks * ((R - ra) / nr)) / (Z / nz)
            ae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz)) / ((R - ra) / nr)
            aw = (((i * (R - ra) / nr) + ra) * kw * (Z / nz)) / ((R - ra) / nr)

            sc = (gm * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr))) + (
                    ro * c * w * Ta * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

            if (i == 0 and j == 0):
                ap = an + ae + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((ae * (E[i + 1, j])) / ap) + (sc / ap)

            elif (i == 0 and j != 0 and j != nz - 1):
                ap = an + ae + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((asul * (E[i, j - 1])) / ap) + ((ae * (E[i + 1, j])) / ap) + (
                        sc / ap)

            elif (i == 0 and j == nz - 1):
                ap = ae + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((asul * (E[i, j - 1])) / ap) + ((ae * (E[i + 1, j])) / ap) + (sc / ap)


            elif (i != 0 and i != nr - 1 and j == nz - 1):
                ap = ae + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (ae * (E[i + 1, j]) / ap) + (
                        sc / ap)


            elif (i == nr - 1 and j == nz - 1):
                q1 = 400
                q2 = h / (1 + (h * ((R - ra) / (nr * 2)) / ke))
                ap = aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr))) + (
                             (((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q2))

                E[i, j] = ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (sc / ap) + (
                        ((((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q1 + (q2 * Tinf))) / ap)


            elif (i == nr - 1 and j != 0 and j != nz - 1):
                q1 = 400
                q2 = h / (1 + (h * ((R - ra) / (nr * 2)) / ke))
                ap = an + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr))) + (
                             (((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q2))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (
                        sc / ap) + (((((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q1 + (q2 * Tinf))) / ap)


            elif (i == nr - 1 and j == 0):
                q1 = 400
                q2 = h / (1 + (h * ((R - ra) / (nr * 2)) / ke))
                ap = an + aw + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr))) + (
                             (((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q2))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (sc / ap) + (
                        ((((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q1 + (q2 * Tinf))) / ap)


            elif (i != 0 and i != nr - 1 and j == 0):
                ap = an + ae + aw + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + ((ae * (E[i + 1, j])) / ap) + (
                        sc / ap)


            elif (i != 0 and i != nr - 1 and j != 0 and j != nz - 1):
                ap = an + ae + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (
                        (ae * (E[i + 1, j])) / ap) + (sc / ap)

    print(E)
    return E


# inicializacao com o T de zeros
F = calculo(T)
D = F.copy()

# iteracoes e convergencia
ncolunas3 = (nr * nz)
cont_i = 0

for a in range(0, 10000000000000000, 1):
    DOld2 = D
    DOld3 = numpy.reshape(DOld2, ncolunas3)
    DOld4 = DOld3.copy()

    # print(DOld4)
    # print("----------------------------------")
    # print(D)
    D = calculo(D)
    # print(D)

    DNew2 = D.copy()
    DNew3 = numpy.reshape(DNew2, ncolunas3)
    DNew4 = DNew3.copy()
    # print(DNew4)

    Ddif = []
    for i in range(0, ncolunas3, 1):
        Ddif.append(math.fabs(DOld4[i] - DNew4[i]))

    MaxDif = numpy.max(Ddif)
    # print(MaxDif)
    Tol = 0.000001
    cont_i += 1

    if (MaxDif <= Tol):
        break

    # print(Ddif)

print(cont_i)


#calculando tempo
end = time.time()
DifSecs = end - start
DifHour = (DifSecs/3600)
print(DifHour)


"""# plot
eixoz = numpy.linspace(0, Z)
eixor = numpy.linspace(ra, R, nr)
eixox = D

numpy.meshgrid(eixoz, eixor)
ax = seaborn.heatmap(eixox)
ax.invert_yaxis()
#title
plt.title('TccCode13_1_FV, Malha de '+ str(nr) + ' x ' + str(nz) + ' volumes, Fluxo de calor = ' + str(400) + ' Z = ' + str(Z) + ' Tempo em Horas =  ' + str(DifHour), fontsize=10)
#lablestitles
plt.xlabel("Eixo z", fontsize=20)
plt.ylabel("Eixo r", fontsize=20)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

#color bar formats
ax.collections[0].colorbar.set_label("T[°C]", fontsize=20)
cbar = ax.collections[0].colorbar.ax.tick_params(labelsize=15)

#legendas limites
x0, x1 = 0, 0.1
y0, y1 = 0.01, 0.03
ax.text(0, -0.07, x0, ha='center', va='top', fontsize=20, color='black', transform=ax.transAxes)
ax.text(1, -0.07, x1, ha='center', va='top', fontsize=20, color='black', transform=ax.transAxes)
ax.text(-0.05, 0, y0, ha='right', va='center', fontsize=20, color='black', transform=ax.transAxes)
ax.text(-0.05, 1, y1, ha='right', va='center', fontsize=20, color='black', transform=ax.transAxes)
ax.vlines([0, 1], [0, 0], [-0.06, -0.06], color='black', clip_on=False, transform=ax.transAxes)
ax.hlines([0, 1], [0, 0], [-0.04, -0.04], color='black', clip_on=False, transform=ax.transAxes)
plt.tight_layout()

plt.show()
"""














#------------------------------------------------------------------------------------------------------------------
#trocar o código: até aqui-------------------



#estrutura para comparação, Tira uma linha paralela a r
#Importante atualizar o valor de ColunaTumorComp para ((nz/2) + 1)
# Usar o valor de D_13_1_k2_RLine na comparação
D_13_1_FV = D.copy()
#usando a coluna que tem o tumor. Neste código não tem tumor, mas para ficar no padrão dos que tem
# Valor de ColunaTumorComp = (nz/2) + 1
ColunaTumorComp = 51
D_13_1_FV_RLine = D_13_1_FV[:, ColunaTumorComp]

