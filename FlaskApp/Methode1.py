import numpy as np
#PARAMS DE TEST

poids = [3, 4, 5]

utilite = [2, 3, 4]


def sommePonderee(utilite_marginale, poids):
    u = np.array(utilite_marginale)
    p = np.array(poids)

    return np.dot(u, p)



print(sommePonderee(utilite,poids));
