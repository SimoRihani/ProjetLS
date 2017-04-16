# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 23:28:45 2017

@author: Jasmin
"""

import numpy as np
import pandas as pd
import json
from pprint import pprint


#Liste des paramètres 
utilite = 0 #fonction par defaut (à définir)
poids = np.array([3, 2, 4])
mu_i = None
mu_ij = None
I = None
V = None
columns = None
N = 3 #Ce paramètre doit etre renseigné avant mu_ij 
Lambda = .8
maximiser_list = [1, 1, 1]
rang = [0, 1, 2]
profiles = None


def c_j(H, b, j, maximiser=1) :
    """indice de concordance partiel selon le critère j, max=1 si le critère est à maximiser,0 si non"""
    return (int(H[j] >= b[j]) if (maximiser) else int(H[j] <= b[j]))

def C(H, b) :
    """indice de condordance global entre H et b"""
    c = np.array([c_j(H, b, j, maximiser=maximiser_list[j]) for j in range(N)])
    
    return (np.dot(poids, c) / poids.sum())
    
def S(H, b) :
    """Vrai si candidat H surclasse le profile b"""
    return (C(H, b) >= Lambda)
    
def pareto_dominance(b_sup, b_inf) :
    """Vrai si b_sup est meilleur que b_inf sur tous les critères"""
    return np.all(b_sup > b_inf)

def EvalOptimiste(H) :
    """Effectue un classement optimiste du candidat H"""
    rang = rang.sort()
    for x in rang :
        #on recupère le ieme profile
        b = profiles.loc[x] 
        if (S(b, H)) :
            return x

    return rand.max()
    
def EvalPessimiste() :
    """Effectue un classement optimiste du candidat H"""
    rang = np.sort(rang)
    for x in rang[::-1] :
        #on recupère le ieme profile
        b = profiles.loc[x] 
        if (S(H, b)) :
            return x

    return rand.min()

    
H = np.array([2, 3, 4])
b = np.array([1, 4, 4])

#[1, 0, 1]
print(S(H, b))