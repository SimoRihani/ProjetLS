import numpy as np



# Params de test
n= 3
poids  = [0.5,0.25,0.25]
indice_interaction = [[1,0.9,0.8],[0.75,0.6,0.8],[0.9,0.7,0.9]]

utilite_marginale = [19,9,12]



def sommePBis(poids,utilite_marginale,n):
    res = 0
    for i in range(0,n):
        res += poids[i]*utilite_marginale[i]

    return res



def SommeP_Interact(utilite_marginale,poids,indice_interaction,n):
    resF = 0

    for i in range(0,n):
        for j in range(1,n):
            resF += 0.5*indice_interaction[i][j]*abs(utilite_marginale[i]-utilite_marginale[j])

    resF = sommePBis(poids,utilite_marginale,n) - r

    return resF


print "resultat de l'évalution par une somme pondérée avec prise en compte de l'interaction entre critères : ", SommeP_Interact(utilite_marginale,poids,indice_interaction,n)
#Ce test ne prends pas en compte les différentes normalisations potentielles sur les params: utilite_marginale, poids ou indice_interaction...