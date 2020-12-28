#Isotropico com k = 0.485, e sem tumor
# 1 significa sem tumor

import numpy
import math
import matplotlib.pyplot as plt
import seaborn

#Numerica 1D
nr = 80#valores pares

T = numpy.zeros([nr], dtype=float)

nz = 100
Z = 0.1
R = 0.03
ra = 0.01

ro = 1050
c = 3617
Ta = 37

h = 10.0
Tinf = 23.0

for i in range(0, nr, 1):

    ks = 0.485
    ke = 0.485
    kw = 0.485
    kn = 0.485
    gm = 991.9
    w = 0.0006722

    ae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz)) / ((R - ra) / nr)
    aw = (((i * (R - ra) / nr) + ra) * kw * (Z / nz)) / ((R - ra) / nr)

    sc = (gm * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

    if (i == 0):
        ap = ae
        T[i] = ((ae * (T[i + 1])) / ap) + (sc / ap)

    if (i == nr - 1):
        q1 = 400
        q2 = h / (1 + (h * ((R - ra) / (nr * 2)) / ke))
        ap = aw + (
                    (((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q2))

        T[i] = ((aw * (T[i - 1])) / ap) + (sc / ap) + (
                    ((((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q1 + (q2 * Tinf))) / ap)

    elif (i != nr -1 and i != 0):
        ap = ae + aw

        T[i] = ((aw * (T[i - 1])) / ap) + (
                    (ae * (T[i + 1])) / ap) + (sc / ap)

    print(T)

D = T.copy()
print(D)


def calculo(E):
    for i in range(0, nr, 1):

        ks = 0.485
        ke = 0.485
        kw = 0.485
        kn = 0.485
        gm = 991.9
        w = 0.0006722

        ae = ((((i + 1) * (R - ra) / nr) + ra) * ke * (Z / nz)) / ((R - ra) / nr)
        aw = (((i * (R - ra) / nr) + ra) * kw * (Z / nz)) / ((R - ra) / nr)

        sc = (gm * ((Z / nz) * (((i + (1.0 / 2.0)) * (R - ra) / nr) + ra) * ((R - ra) / nr)))

        if (i == 0):
            ap = ae
            E[i] = ((ae * (E[i + 1])) / ap) + (sc / ap)

        if (i == nr - 1):
            q1 = 400
            q2 = h / (1 + (h * ((R - ra) / (nr * 2)) / ke))
            ap = aw + (
                    (((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q2))

            E[i] = ((aw * (E[i - 1])) / ap) + (sc / ap) + (
                    ((((i + 1.0) * (R - ra) / nr) + ra) * (Z / nz) * (q1 + (q2 * Tinf))) / ap)

        elif (i != nr - 1 and i != 0):
            ap = ae + aw

            E[i] = ((aw * (E[i - 1])) / ap) + (
                    (ae * (E[i + 1])) / ap) + (sc / ap)

    print(E)
    return E


#iteracao e convergencia
cont_i = 0
for a in range(0, 10000000000, 1):

    DOld2 = D.copy()

    D = calculo(D)

    DNew2 = D.copy()

    Ddif = []
    for i in range(0, nr, 1):
        Ddif.append(math.fabs(DOld2[i] - DNew2[i]))

    MaxDif = numpy.max(Ddif)
    # print(MaxDif)
    Tol = 0.0000001
    cont_i += 1

    if (MaxDif <= Tol):
        break

DSA = D.copy()
print(DSA)
print(cont_i)

