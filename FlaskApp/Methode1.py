import numpy as np
#PARAMS DE TEST


def sommePonderee(utilite_marginale, poids):
    """Evaluation par somme ponderee"""
    u = np.array(utilite_marginale)
    p = np.array(poids)
    print(" U ----", u, '-----P', p)
    return np.dot(u, p)
