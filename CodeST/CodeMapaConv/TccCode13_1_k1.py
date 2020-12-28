#Isotropico com k = 0.485, e sem tumor
# 1 significa sem tumor

import numpy
import math
import matplotlib.pyplot as plt
import seaborn

nr = 8  # valores pares
nz = 10

T = numpy.zeros([nr, nz], dtype=float)

Z = 0.1
R = 0.03
ra = 0.01

ro = 1050
c = 3617
Ta = 37

h = 10.0
Tinf = 23.0


def calculo(E):
    for i in range(0, nr, 1):

        ks = 0.485
        ke = 0.485
        kw = 0.485
        kn = 0.485
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


MaxDifMapConv = []
cont_iMapConv = []

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

    MaxDifMapConv.append(MaxDif)
    cont_iMapConv.append(cont_i)
    if (MaxDif <= Tol):
        break


    # print(Ddif)

print(cont_i)


#--------------------------------------------------------------------------------------------------------------
#1 Comentar o plot que veio junto
#2Colocar essa estrutura abaixo em cima do for das iterações
"""MaxDifMapConv = []
cont_iMapConv = []"""
#3Colocar essa estrutura abaixo, em cima do if do break
"""MaxDifMapConv.append(MaxDif)
cont_iMapConv.append(cont_i)"""


#colocar o codigo daqui para cima --------
#plot com escala log no eixoy, como o professor pediu
#plt.title('TccCode13_1_k1, , Malha de '+ str(nr) + ' volumes, e '+ str(cont_i) + ' iterações no total', fontsize=20)
plt.xlabel("Número de iterações", fontsize=20)
plt.ylabel('Máxima Diferença entre as iterações (Escala Log)', fontsize=15)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.plot(cont_iMapConv, MaxDifMapConv, label='Solução Numérica')
plt.yscale('log')

plt.show()





#plot com escala simples
"""plt.title('TccCode13_1_k1, , Malha de '+ str(nr) + ' volumes, e '+ str(cont_i) + ' iterações no total', fontsize=20)
plt.xlabel("Número de iterações", fontsize=20)
plt.ylabel('Máxima Diferença entre as iterações', fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.plot(cont_iMapConv, MaxDifMapConv, label='Solução Numérica')
plt.show()
"""









