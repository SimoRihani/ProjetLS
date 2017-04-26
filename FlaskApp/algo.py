# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:47:12 2017

@author: Jasmin
"""

from parser import *
#from parser import read_data
#from parser import read_params
#import parser
from Methode2 import EvalWeightedSumInteract
from Methode2 import *
from Methode1 import *
from algo3 import *


#oui
def algorithme_1(File) :
    data_brute = read_data(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser) = read_params(File)

    #test des parametres
    if (not param_Valide_Algo_1(poids)) :
        print('poids non valides')
        # return False
    data_brute = traite_data(data_brute, poids)

    # print(data_brute)

    data = normalize(data_brute, normalisation=norm)
    data['score'] = -1

    for idx in data.index :
        print("SHAPEEEEE", data.loc[idx].shape)
        # if (data.loc[idx].shape[0] < 2) :
        data.loc[idx, 'score'] = sommePonderee(data.loc[idx, data.columns[:-1]], poids)
    data.sort_values('score', inplace=True, ascending=False)
    data = data.reset_index()

    # data.to_csv("resultat.csv")

    res = []
    for idx in data.index :
        l = {}
        line = data.loc[idx]
        for x in data.columns :
            l[x] = line[x]
        res = res + [l]
    print(data)
    print('RES ')
    print(res)
    return res


def algorithme(File) :
    if (File["Method"] == "1") :
        return algorithme_1(File)
    if (File["Method"] == "2") :
        return algorithme_2(File)
    if (File["Method"] == "3") :
        return algorithme_3_Optimiste(File)
    if (File["Method"] == "4") :
        return algorithme_3_Pessimiste(File)

def algorithme_2(File) :
    data_brute = read_data(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser) = read_params(File)
    V = v(mu_i, mu_ij, N)
    I = i(mu_i, mu_ij, N)

    #test des parametres
    if (not param_Valide_Algo_2(V, mu_i, mu_ij, I, poids, N)) :
        print('parametres non valides')
        # return False

    #print(utilite, normalise)
    data_brute = traite_data(data_brute, poids)

    data = normalize(data_brute, normalisation=norm)
    data['score'] = -1

    for idx in data.index :
        data.loc[idx, 'score'] = EvalWeightedSumInteract(data.loc[idx, data.columns[:-1]], poids, I, N)
    data.sort_values('score', inplace=True, ascending=False)
    data = data.reset_index()

    # data.to_csv("resultat.csv")

    res = []
    for idx in data.index :
        l = {}
        line = data.loc[idx]
        for x in data.columns :
            l[x] = line[x]
        res = res + [l]
    print(res)
    return res


def algorithme_3_Optimiste(File) :
    data_brute = read_data(File)
    profiles = read_profiles(File)

    print("________PROFILES________", profiles)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser) = read_params(File)

    #test des parametres
    if (not param_Valide_Algo_3(Lambda)) :
        print('parametres non valides')
        # return False
    profiles = traite_data(profiles, poids)
    data_brute = traite_data(data_brute, poids)

    data = normalize(data_brute, normalisation=norm)

    data['classe'] = -1

    for idx in data.index :
        data.loc[idx, 'classe'] = EvalOptimiste(data.loc[idx, data.columns[:-1]], profiles, maximiser, poids, Lambda)
    data.sort_values('classe', inplace=True, ascending=False)
    data = data.reset_index()

    # data.to_csv("resultat.csv")

    res = []
    for idx in data.index :
        l = {}
        line = data.loc[idx]
        for x in data.columns :
            l[x] = line[x]
        res = res + [l]
    print(res)
    return res

def algorithme_3_Pessimiste(File) :
    data_brute = read_data(File)
    profiles = read_profiles(File)

    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser) = read_params(File)

    #test des parametres
    if (not param_Valide_Algo_3(Lambda)) :
        print('parametres non valides')
        # return False

    data_brute = traite_data(data_brute, poids)
    profiles = traite_data(profiles, poids)
    data = normalize(data_brute, normalisation=norm)

    data['classe'] = -1

    for idx in data.index :
        data.loc[idx, 'classe'] = EvalPessimiste(data.loc[idx, data.columns[:-1]], profiles, maximiser, poids, Lambda)
    data.sort_values('classe', inplace=True, ascending=False)
    data = data.reset_index()
    # data.to_csv("resultat.csv")
    res = []
    for idx in data.index :
        l = {}
        line = data.loc[idx]
        for x in data.columns :
            l[x] = line[x]
        res = res + [l]
    print(res)
    return res

algorithme(File)
