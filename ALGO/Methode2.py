import numpy as np



# Params de test
n= 3
poids  = [0.5,0.25,0.25]
indice_interaction = [[1,0.9,0.8],[0.75,0.6,0.8],[0.9,0.7,0.9]]

utilite_marginale = [19,9,12]



def somme_A(poids,utilite_marginale,n) :
    res = 0
    for i in range(0,n):
        res = res + poids[i]*utilite_marginale[i]

    return res



def EvalWeightedSumInteract(utilite_marginale, poids, indice_interaction, n) :
    s_B = 0
    s_A = somme_A(poids, utilite_marginale, n)

    for i in range(0,n):
        for j in range(1,n):
            s_B = s_B + indice_interaction[i][j] * abs(utilite_marginale[i]-utilite_marginale[j])
    
    s_B = 0.5 * s_B
    return (s_A - s_B)


#print "resultat de l'évalution par une somme pondérée avec prise en compte de l'interaction entre critères : ", SommeP_Interact(utilite_marginale,poids,indice_interaction,n)
#Ce test ne prends pas en compte les différentes normalisations potentielles sur les params: utilite_marginale, poids ou indice_interaction...