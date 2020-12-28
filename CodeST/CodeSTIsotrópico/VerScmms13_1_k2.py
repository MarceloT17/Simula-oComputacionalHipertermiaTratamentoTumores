#Isotropico com k = 0.53, e sem tumor
# 1 significa sem tumor

import numpy
import math
import matplotlib.pyplot as plt
import seaborn

nr = 80 #valores pares
nz = 100

T = numpy.zeros([nr, nz], dtype=float)

Z = 0.1
R = 0.03
ra = 0.01

ro = 1050
c = 3617
Ta = 37

h = 100
b = Z/2
cvetorq = 0.01

h2 = 10.0
Tinf = 23.0


for i in range(0, nr, 1):
    ks = 0.53
    ke = 0.53
    kw = 0.53
    kn = 0.53
    gm = 991.9
    w = 0.0006722

    for j in range(0, nz, 1):
        an = ((((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * kn * ((R - ra) / nr))/ (Z / nz)
        asul = ((((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ks * ((R - ra) / nr)) / (Z / nz)
        ae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz)) / ((R - ra) / nr)
        aw = (((i * (R - ra) / nr) + ra) * kw * (Z / nz)) / ((R - ra) / nr)

        sc = (gm * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr))) + (ro * c * w * Ta * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

        scmms = (((-1 * (ro * c * w)) * (Ta - (
                    (math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z))))) - gm - (
                         (1 / (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra)) * kn * (
                     math.sin((math.pi) / Z * (j + (1.0 / 2.0)) * Z / nz)) * (math.pi) / (R - ra) * (
                             math.cos((math.pi) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) / (R - ra)))) + (
                         kn * ((math.pi) / (R - ra)) * ((math.pi) / (R - ra)) * (math.sin(
                     (math.pi) * (j + (1.0 / 2.0)) * Z / nz / Z)) * (math.sin(
                     (math.pi) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) / (R - ra)))) + (
                         kn * ((math.pi) / Z) * ((math.pi) / Z) * (
                     math.sin((math.pi) / Z * (j + (1.0 / 2.0)) * Z / nz)) * (math.sin(
                     (math.pi) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) / (R - ra))))) * (
                        Z / nz * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (R - ra) / nr)

        if (i == 0 and j == 0):
            ap = an + ae + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scaw = - (((i * (R - ra) / nr) + ra) * (Z/nz) * kw * (math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R-ra)) * (math.cos((math.pi) * ra / (R-ra))))
            scasul = ((-1) * ks * ((math.pi) / Z) * (math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

            T[i, j] = ((an * (T[i, j + 1])) / ap) + ((ae * (T[i + 1, j])) / ap) + (sc / ap) + (scmms / ap) + (scaw / ap) + (scasul / ap)

        elif (i == 0 and j != 0 and j != nz - 1):
            ap = an + ae + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scaw = - (((i * (R - ra) / nr) + ra) * (Z / nz) * kw * (
                math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                          math.cos((math.pi) * ra / (R - ra))))

            T[i, j] = ((an * (T[i, j + 1])) / ap) + ((asul * (T[i, j - 1])) / ap) + ((ae * (T[i + 1, j])) / ap) + (
                        sc / ap) + (scmms / ap) + (scaw / ap)

        elif (i == 0 and j == nz - 1):
            ap = ae + asul + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scaw = - (((i * (R - ra) / nr) + ra) * (Z / nz) * kw * (
                math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                          math.cos((math.pi) * ra / (R - ra))))
            scan1 = ((-1) * kn * ((math.pi) / Z) * (math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

            T[i, j] = ((asul * (T[i, j - 1])) / ap) + ((ae * (T[i + 1, j])) / ap) + (sc / ap) + (scmms / ap) + (scaw / ap) + (scan1 / ap)


        elif (i != 0 and i != nr - 1 and j == nz - 1):
            ap = ae + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scan1 = ((-1) * kn * ((math.pi) / Z) * (
                math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                 ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

            T[i, j] = ((asul * (T[i, j - 1])) / ap) + ((aw * (T[i - 1, j])) / ap) + (ae * (T[i + 1, j]) / ap) + (
                        sc / ap) + (scmms / ap) + (scan1 / ap)


        elif (i == nr - 1 and j == nz - 1):
            ap = aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scan1 = ((-1) * kn * ((math.pi) / Z) * (
                math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                             ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))
            scae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz) * (math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (math.cos((math.pi) * R / (R-ra))))

            T[i, j] = ((asul * (T[i, j - 1])) / ap) + ((aw * (T[i - 1, j])) / ap) + (sc / ap) + (scmms / ap) + (scan1 / ap) + (scae / ap)


        elif (i == nr - 1 and j != 0 and j != nz - 1):
            ap = an + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz) * (
                math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                        math.cos((math.pi) * R / (R - ra))))

            T[i, j] = ((an * (T[i, j + 1])) / ap) + ((asul * (T[i, j - 1])) / ap) + ((aw * (T[i - 1, j])) / ap) + (
                        sc / ap) + (scmms / ap) + (scae / ap)


        elif (i == nr - 1 and j == 0):
            ap = an + aw + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz) * (
                math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                        math.cos((math.pi) * R / (R - ra))))
            scasul = ((-1) * ks * ((math.pi) / Z) * (
                math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                  ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

            T[i, j] = ((an * (T[i, j + 1])) / ap) + ((aw * (T[i - 1, j])) / ap) + (sc / ap) + (scmms / ap) + (scae / ap) + (scasul / ap)


        elif (i != 0 and i != nr - 1 and j == 0):
            ap = an + ae + aw + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
            scasul = ((-1) * ks * ((math.pi) / Z) * (
                math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                              ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

            T[i, j] = ((an * (T[i, j + 1])) / ap) + ((aw * (T[i - 1, j])) / ap) + ((ae * (T[i + 1, j])) / ap) + (
                        sc / ap) + (scmms / ap) + (scasul / ap)


        elif (i != 0 and i != nr - 1 and j != 0 and j != nz - 1):
            ap = an + ae + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

            T[i, j] = ((an * (T[i, j + 1])) / ap) + ((asul * (T[i, j - 1])) / ap) + ((aw * (T[i - 1, j])) / ap) + (
                        (ae * (T[i + 1, j])) / ap) + (sc / ap) + (scmms / ap)

        print(T)

    D = T.copy()
    print(D)

def calculo(E):

    for i in range(0, nr, 1):

        ks = 0.53
        ke = 0.53
        kw = 0.53
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

            scmms = (((-1 * (ro * c * w)) * (Ta - (
                    (math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z))))) - gm - (
                             (1 / (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra)) * kn * (
                         math.sin((math.pi) / Z * (j + (1.0 / 2.0)) * Z / nz)) * (math.pi) / (R - ra) * (
                                 math.cos((math.pi) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) / (R - ra)))) + (
                             kn * ((math.pi) / (R - ra)) * ((math.pi) / (R - ra)) * (math.sin(
                         (math.pi) * (j + (1.0 / 2.0)) * Z / nz / Z)) * (math.sin(
                         (math.pi) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) / (R - ra)))) + (
                             kn * ((math.pi) / Z) * ((math.pi) / Z) * (
                         math.sin((math.pi) / Z * (j + (1.0 / 2.0)) * Z / nz)) * (math.sin(
                         (math.pi) * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) / (R - ra))))) * (
                            Z / nz * (((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (R - ra) / nr)

            if (i == 0 and j == 0):
                ap = an + ae + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scaw = - (((i * (R - ra) / nr) + ra) * (Z / nz) * kw * (
                    math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                              math.cos((math.pi) * ra / (R - ra))))
                scasul = ((-1) * ks * ((math.pi) / Z) * (
                    math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                      ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((ae * (E[i + 1, j])) / ap) + (sc / ap) + (scmms / ap) + (
                            scaw / ap) + (scasul / ap)

            elif (i == 0 and j != 0 and j != nz - 1):
                ap = an + ae + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scaw = - (((i * (R - ra) / nr) + ra) * (Z / nz) * kw * (
                    math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                              math.cos((math.pi) * ra / (R - ra))))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((asul * (E[i, j - 1])) / ap) + ((ae * (E[i + 1, j])) / ap) + (
                        sc / ap) + (scmms / ap) + (scaw / ap)

            elif (i == 0 and j == nz - 1):
                ap = ae + asul + (
                            ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scaw = - (((i * (R - ra) / nr) + ra) * (Z / nz) * kw * (
                    math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                              math.cos((math.pi) * ra / (R - ra))))
                scan1 = ((-1) * kn * ((math.pi) / Z) * (
                    math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                     ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

                E[i, j] = ((asul * (E[i, j - 1])) / ap) + ((ae * (E[i + 1, j])) / ap) + (sc / ap) + (scmms / ap) + (
                            scaw / ap) + (scan1 / ap)


            elif (i != 0 and i != nr - 1 and j == nz - 1):
                ap = ae + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scan1 = ((-1) * kn * ((math.pi) / Z) * (
                    math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                 ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

                E[i, j] = ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (ae * (E[i + 1, j]) / ap) + (
                        sc / ap) + (scmms / ap) + (scan1 / ap)


            elif (i == nr - 1 and j == nz - 1):
                ap = aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scan1 = ((-1) * kn * ((math.pi) / Z) * (
                    math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                 ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))
                scae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz) * (
                    math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                            math.cos((math.pi) * R / (R - ra))))

                E[i, j] = ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (sc / ap) + (scmms / ap) + (
                            scan1 / ap) + (scae / ap)


            elif (i == nr - 1 and j != 0 and j != nz - 1):
                ap = an + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz) * (
                    math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                            math.cos((math.pi) * R / (R - ra))))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (
                        sc / ap) + (scmms / ap) + (scae / ap)


            elif (i == nr - 1 and j == 0):
                ap = an + aw + (ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz) * (
                    math.sin(((j + (1.0 / 2.0)) * (Z / nz)) * (math.pi) / Z)) * ((math.pi) / (R - ra)) * (
                            math.cos((math.pi) * R / (R - ra))))
                scasul = ((-1) * ks * ((math.pi) / Z) * (
                    math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                  ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (sc / ap) + (scmms / ap) + (
                            scae / ap) + (scasul / ap)


            elif (i != 0 and i != nr - 1 and j == 0):
                ap = an + ae + aw + (
                            ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))
                scasul = ((-1) * ks * ((math.pi) / Z) * (
                    math.sin((((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * (math.pi) / (R - ra))) * (
                                  ((i + (1.0 / 2.0)) * ((R - ra) / nr)) + ra) * ((R - ra) / nr))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + ((ae * (E[i + 1, j])) / ap) + (
                        sc / ap) + (scmms / ap) + (scasul / ap)


            elif (i != 0 and i != nr - 1 and j != 0 and j != nz - 1):
                ap = an + ae + aw + asul + (
                        ro * c * w * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

                E[i, j] = ((an * (E[i, j + 1])) / ap) + ((asul * (E[i, j - 1])) / ap) + ((aw * (E[i - 1, j])) / ap) + (
                        (ae * (E[i + 1, j])) / ap) + (sc / ap) + (scmms / ap)

    print(E)
    return E




# iteracoes e convergencia
ncolunas3 = (nr * nz)
cont_i = 0
for a in range(0, 10000000000000, 1):
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



# -----------------------------------------------------------------------------------------------------------
#Colcar o código daqui para cima, deixar a parte do plot comentada, e tirar do comentário o plot que desejar




#plot de linhas sobrepostas

eixox = numpy.linspace(ra, R, nr)
#estrutura para comparação, Tira uma linha paralela a r
#Importante atualizar o valor de ColunaTumorComp para ((nz/2) + 1)
# Usar o valor de D_Mms_13_1_k1_RLine na comparação
D_Mms_13_1_k2 = D.copy()
#usando a coluna que tem o tumor. Neste código não tem tumor, mas para ficar no padrão dos que tem
# Valor de ColunaTumorComp = (nz/2) + 1
ColunaTumorComp = 51
D_Mms_13_1_k2_RLine = D_Mms_13_1_k2[:, ColunaTumorComp]
#SolTmms13_1_k1
import CodeST.CodeSTIsotropico.SolTmms13_1_k2
A_1 = CodeST.CodeSTIsotropico.SolTmms13_1_k2.A_sol13.copy()
A_1RLine = A_1[:, ColunaTumorComp]
plt.plot(eixox, D_Mms_13_1_k2_RLine, marker='o', label='Solução pelo Mms')
plt.plot(eixox, A_1RLine, marker='^', label='Solução Manufaturada')
plt.ylabel('Valores sobrepostos', fontsize=21)
plt.xlabel("Eixo r [m]", fontsize=25)
#plt.title('VerScmms13_1_k2, , Malha de '+ str(nr) + ' volumes', fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(fontsize=20)
#plt.legend()
plt.show()




#plot de diferença percentual
"""
#estrutura para comparação, Tira uma linha paralela a r
#Importante atualizar o valor de ColunaTumorComp para ((nz/2) + 1)
# Usar o valor de D_Mms_13_1_k1_RLine na comparação
D_Mms_13_1_k2 = D.copy()
#usando a coluna que tem o tumor. Neste código não tem tumor, mas para ficar no padrão dos que tem
# Valor de ColunaTumorComp = (nz/2) + 1
ColunaTumorComp = 51
D_Mms_13_1_k2_RLine = D_Mms_13_1_k2[:, ColunaTumorComp]

#SolTmms13_1_k1
import CodeST.CodeSTIsotropico.SolTmms13_1_k2
A_1 = CodeST.CodeSTIsotropico.SolTmms13_1_k2.A_sol13.copy()
A_1RLine = A_1[:, ColunaTumorComp]

Diff_SolScMms_13_1_k1 = []
eixox = numpy.linspace(ra, R, nr)
for i in range(len(eixox)):
    Diff_SolScMms_13_1_k1.append(math.fabs((D_Mms_13_1_k2_RLine[i] - A_1RLine[i]))/ D_Mms_13_1_k2_RLine[i] * 100)

PercDiff = Diff_SolScMms_13_1_k1.copy()
plt.ylabel('Valores percentuais', fontsize=20)
plt.plot(eixox, PercDiff)
plt.title('VerScmms13_1_k2, , Malha de '+ str(nr) + ' volumes', fontsize=20)
plt.xlabel('Eixo r [m]', fontsize=20)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.show()
"""
















#plot das matrizes sobrepostas, professor falou para não usar

"""#plots
#rever esses plots
#transformar array em vetor nrxnz
B_sol12 = D.copy()
ncolunas1 = (nr * nz)
D1 = numpy.reshape(B_sol12, ncolunas1)
eixoD1 = numpy.linspace(ra, R, ncolunas1)
plt.plot(eixoD1, D1, label='Solução pelo Mms')

#SolTmms12_1_k1
import CodeST.CodeSTIsotropico.solTmms13_1_k1
A_1 = CodeST.CodeSTIsotropico.solTmms13_1_k1.A_sol13.copy()
A_1_1 = numpy.reshape(A_1, ncolunas1)
plt.plot(eixoD1, A_1_1, label='Solução Manufatura')

plt.title('VerScmms13_1_k2, Malha de '+ str(nr) + ' x ' + str(nz) + ' volumes, Matrizes Sobrepostas')
plt.ylabel("Valores ")
plt.legend()
plt.show()
"""