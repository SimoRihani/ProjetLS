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
    print(" ------B----- ", b)
    print("MAXIMISER ", type(maximiser), " H  ", H[j], " Type ", type(H[j]))
    print(" TESTB ", b[j], " TYPE ", type(b[j]))
    return (int(H[j] >= b[j]) if (maximiser) else int(H[j] <= b[j]))

def C(H, b, maximiser_list, poids) :
    """indice de condordance global entre H et b"""
    # print("TAIIILLLE : ", b.shape)
    N = b.shape[0]

    c = np.array([c_j(H, b, j, maximiser=maximiser_list[j]) for j in range(N)])

    return (np.dot(poids, c) / np.array(poids).sum())

def S(H, b, maximiser_list, poids, Lambda) :
    """Vrai si candidat H surclasse le profile b"""
    return (C(H, b, maximiser_list, poids) >= Lambda)

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
# pareto_dominance(profiles)

def EvalOptimiste(H, profiles, maximiser_list, poids, Lambda) :
    """Effectue un classement optimiste du candidat H"""
    rang = profiles.index
    for i in rang :
        #on recupère le ieme profile
        b = profiles.loc[i]
        if (S(b, H, maximiser_list, poids, Lambda)) :
            return int(i) - 1

    return rand.max()

def EvalPessimiste(H, profiles, maximiser_list, poids, Lambda) :
    """Effectue un classement optimiste du candidat H"""
    rang = profiles.index
    for i in rang[::-1] :
        #on recupère le ieme profile
        b = profiles.loc[i]
        if (S(H, b, maximiser_list, poids, Lambda)) :
            return int(i)

    return rand.min()
