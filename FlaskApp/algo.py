# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:47:12 2017

@author: Jasmin
"""

from parser import *
from parser import read_data
from parser import read_params
import parser
from Methode2 import EvalWeightedSumInteract
from Methode2 import *
from Methode1 import *


# (utilite, poids, mu_i, mu_ij, columns, N, Lambda) = read_params(File)
# V = v(mu_i, mu_ij)
#print(V)

def algorithme_1(File) :
    data_brute = read_data(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda) = read_params(File)

    #test des paramètres
    if (not param_Valide_Algo_1(poids)) :
        print('poids non valides')
        # return False
    data_brute = traite_data(data_brute, poids)

    print('data_brute ')
    print(data_brute)

    data = norm(data_brute, normalisation=utilite)
    data['score'] = -1

    for idx in data.index :
        data.loc[idx, 'score'] = sommePonderee(data.loc[idx, data.columns[:-1]], poids)
    return data

def norm(data, normalisation=0) :
    data_norm = data.copy()
    return data_norm

def algorithme_2(File) :
    print('JASMIN------- ')
    print(File)
    data_brute = read_data(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda) = read_params(File)
    V = v(mu_i, mu_ij, N)
    I = i(mu_i, mu_ij, N)

    #test des paramètres
    if (not param_Valide_Algo_2(V, mu_i, mu_ij, I, poids, N)) :
        print('parametres non valides')
        #return False
    print('I & V & N & mus ')
    print(I)
    print(V)
    print(N)
    print(mu_i)
    print(mu_ij)

    data_brute = traite_data(data_brute, poids)
    print('data_brute ')
    print(data_brute)
    print(data_brute.info())
    data = norm(data_brute, normalisation=utilite)
    data['score'] = -1

    for idx in data.index :
        data.loc[idx, 'score'] = EvalWeightedSumInteract(data.loc[idx, data.columns[:-1]], poids, I, N)
        print('EVALUATION ')
        print(EvalWeightedSumInteract(data.loc[idx, data.columns[:-1]], poids, I, N))
    return data

#print(algorithme_2(File))

def algorithme_3_Pessimiste(File) :
    data_brute = read_data(File)
    profiles = read_profiles(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda) = read_params(File)

    #test des paramètres
    if (not param_Valide_Algo_3(Lambda)) :
        print('parametres non valides')
        #return False

    data_brute = traite_data(data, poids)

    data = norm(data_brute, normalisation=utilite)

    data['classe'] = -1

    for idx in data.index :
        data.loc[idx, 'classe'] = EvalOptimiste(data.loc[idx, data.columns[:-1]], profiles)

    return data

def algorithme_3_Pessimiste(File) :
    data_brute = read_data(File)
    profiles = read_profiles(File)
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda) = read_params(File)

    #test des paramètres
    if (not param_Valide_Algo_3(Lambda)) :
        print('parametres non valides')
        #return False
    # if ()

    data_brute = traite_data(data, poids)

    data = norm(data_brute, normalisation=utilite)

    data['classe'] = -1

    for idx in data.index :
        data.loc[idx, 'classe'] = EvalPessimiste(data.loc[idx, data.columns[:-1]], profiles)

    return data
