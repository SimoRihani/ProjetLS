import numpy as np




def somme_A(poids,utilite_marginale,n) :
    res = 0
    
    for i in range(0,n):    
        res = res + poids[i]*utilite_marginale[i]

    return res



def EvalWeightedSumInteract(utilite_marginale, poids, indice_interaction, n) :
    """Evaluation par indice d'interaction"""
    s_B = 0
    s_A = somme_A(poids, utilite_marginale, n)
    
    for i in range(n):
        for j in range(n):
            s_B = s_B + indice_interaction[i][j] * abs(utilite_marginale[i]-utilite_marginale[j])

    s_B = 0.5 * s_B
    return (s_A - s_B)
