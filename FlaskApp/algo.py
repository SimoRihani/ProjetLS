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


# (utilite, poids, mu_i, mu_ij, columns, N, Lambda) = read_params(File)
# V = v(mu_i, mu_ij)
#print(V)

def algorithme_1(File) :
    data_brute = read_data(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, normalise) = read_params(File)

    #test des paramètres
    if (not param_Valide_Algo_1(poids)) :
        print('poids non valides')
        # return False
    data_brute = traite_data(data_brute, poids)

    print('data_brute ')
    print(data_brute)

    data = norm(data_brute, utilite, normalise)
    data['score'] = -1

    for idx in data.index :
        data.loc[idx, 'score'] = sommePonderee(data.loc[idx, data.columns[:-1]], poids)
    res = []
    for idx in data.index :
        l = {}
        line = data.loc[idx]
        for x in data.columns :
            l[x] = line[x]
        res = res + [l]
    print(res)
    return res

def norm(data, normalisation=0, normal=[]) :
    data_norm = data.copy()
    #for x in range(len(data_norm.columns)) :
    #    data_norm[x] =
    return data_norm

def algorithme(File) :
    print(File["Method"])
    if (File["Method"] == '1') :
        print('OUIPIOEOEEO')
        return algorithme_1(File)
    if (File["Method"] == '2') :
        return algorithme_2(File)
    if (File["Method"] == '3') :
        return algorithme_3_Optimiste(File)
    if (File["Method"] == '4') :
        return algorithme_3_Pessimiste(File)

def algorithme_2(File) :
    print("2")
    data_brute = read_data(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, normalise) = read_params(File)
    V = v(mu_i, mu_ij, N)
    I = i(mu_i, mu_ij, N)

    #test des paramètres
    if (not param_Valide_Algo_2(V, mu_i, mu_ij, I, poids, N)) :
        print('parametres non valides')
        #return False

    print(utilite, normalise)
    data_brute = traite_data(data_brute, poids)

    data = norm(data_brute, utilite, normalise)
    data['score'] = -1

    for idx in data.index :
        data.loc[idx, 'score'] = EvalWeightedSumInteract(data.loc[idx, data.columns[:-1]], poids, I, N)

    #d = {}
    #for x in data.columns :
        #d[x] = list(data[x])
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
    print("3")

    data_brute = read_data(File)
    profiles = read_profiles(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, normalise) = read_params(File)

    #test des paramètres
    if (not param_Valide_Algo_3(Lambda)) :
        print('parametres non valides')
        #return False

    data_brute = traite_data(data, poids)

    data = norm(data_brute, utilite, normalise)

    data['classe'] = -1

    for idx in data.index :
        data.loc[idx, 'classe'] = EvalOptimiste(data.loc[idx, data.columns[:-1]], profiles)

    return data

def algorithme_3_Pessimiste(File) :
    print("4")

    data_brute = read_data(File)
    profiles = read_profiles(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, normalise) = read_params(File)

    #test des paramètres
    if (not param_Valide_Algo_3(Lambda)) :
        print('parametres non valides')
        #return False
    # if ()

    data_brute = traite_data(data, poids)

    data = norm(data_brute, utilite, normalise)

    data['classe'] = -1

    for idx in data.index :
        data.loc[idx, 'classe'] = EvalPessimiste(data.loc[idx, data.columns[:-1]], profiles)

    return data

# algorithme(File)
