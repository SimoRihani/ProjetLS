# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 23:28:45 2017

@author: Jasmin
"""

import numpy as np
import pandas as pd
import json
from pprint import pprint
import parser



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
    
def pareto_dominance_ij(b_sup, b_inf) :
    """Vrai si b_sup est meilleur que b_inf sur tous les critères"""
    return np.all(b_sup > b_inf)
    
def pareto_dominance(profiles) :
    """Vrai si la pareto dominance stricte est vérifiée pour tous les profiles"""
    for idx in range(len(profiles.index) - 1) :
        b_inf = profiles.loc[profiles.index[idx]]
        b_sup = profiles.loc[profiles.index[idx + 1]]
        if (not pareto_dominance_ij(b_sup, b_inf)) :
            return False
            
    return True
pareto_dominance(profiles)

def EvalOptimiste(H, profiles) :
    """Effectue un classement optimiste du candidat H"""
    rang = profiles.index
    for i in rang :
        #on recupère le ieme profile
        b = profiles.loc[i] 
        if (S(b, H)) :
            return i - 1

    return rand.max()
    
def EvalPessimiste(H, profiles) :
    """Effectue un classement optimiste du candidat H"""
    rang = profiles.index
    for i in rang[::-1] :
        #on recupère le ieme profile
        b = profiles.loc[i] 
        if (S(H, b)) :
            return i

    return rand.min()

    
H = np.array([2, 3, 4])
b = np.array([1, 4, 4])

#[1, 0, 1]
print(poids)
print(S(H, b))