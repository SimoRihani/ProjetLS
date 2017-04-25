# -*- coding: utf-8 -*-
"""
editeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import pandas as pd
import json
from pprint import pprint

File = {"Profiles" : { "Academie" : [60000, 30000, 40000], "Departement" : [5, 6, 7], "Dernier" : [80, 90, 100] },
        "Content" : {"Academie" : [2000, 3000, 4000], "Departement" : [5, 6, 7], "Dernier" : [8, 9, 10] },
        "Param" : {"maximiser" : ["1", "1", "0"], "norm" : ["1000", "1", "20"], "nbProfiles" : ["0"], "N" : ["3"], "mu_ij" : [.1, .3, .4], "mu_i" : [5, 6, 7], "poids" : [8, 9, 10] },
        "Method" : "1"
}


def read_params(File) :
    utilite = 0 #fonction par defaut (a definir)
    poids = None
    mu_i = None
    mu_ij = None
    columns = None
    N = 0 #Ce parametre doit etre renseigne avant mu_ij
    Lambda = 0
    norm = None
    nbProfiles = None
    maximiser = None

    params = File['Param']
    for param_c, value_param in params.items() :
        #param_c = p.split(';')

        #Nombre de criteres
        if (param_c == 'N') :
            N = int(value_param[0])

        #Nombre de criteres
        if (param_c == 'nbProfiles') :
            nbProfiles = int(value_param[0])

        #lambda
        if (param_c == 'lambda') :
            Lambda = float(value_param[0])

        #Poids
        if ((param_c == 'poids') or (param_c == 'poids_2') or (param_c == 'w') or (param_c == 'v')) :
            poids = []
            for x in value_param :
                if(x != ''):
                    poids = poids + [float(x)]

        #colonne
        if ((param_c == 'colonne') or (param_c == 'cols') or (param_c == 'columns')) :
            columns = []
            for x in value_param :
                columns = columns + [float(x)]

        #Utilite
        if ((param_c == 'utilite') or (param_c == 'u')) :
            utilite = int(value_param[0])

        #norm
        if (param_c == 'norm') :
            norm = []
            for x in value_param :
                if(x != ''):
                    norm = norm + [float(x)]

        #mu_i
        if (param_c == 'mu_i') :
            mu_i = []
            for x in value_param :
                if(x != ''):
                    mu_i = mu_i + [float(x)]

        #maximiser
        if (param_c == 'maximiser') :
            maximiser = []
            for x in value_param :
                if(x != ''):
                    maximiser = maximiser + [int(x)]

        if (param_c == 'mu_ij') :
            N = int(params["N"][0])
            mu_ij = np.zeros((N, N))
            idx = 0
            for i in range(0, N - 1) :
                for j in range(i + 1, N) :
                    mu_ij[i, j] = float(value_param[idx])
                    mu_ij[j, i] = mu_ij[i, j]
                    idx = idx + 1
            #print(mu_ij)


    return (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser)

#read_params(File)
def I_ij(i, j, mu_i, mu_ij, N) :
    #print(mu_ij[i, j] , mu_i[i], mu_i[j])
    return 0 if (i == j) else mu_ij[i, j] - mu_i[i] - mu_i[j]

def V_i(i, mu_i, mu_ij, N) :
    tmp_I = [I_ij(i, j, mu_i, mu_ij, N) for j in range(0, N) if (j != i)]
    tmp_I = np.array(tmp_I).sum()

    return mu_i[i] - .5 * tmp_I

def v(mu_i, mu_ij, N) :
    """Calcule le tableau V[i]"""
    return [V_i(i, mu_i, mu_ij, N) for i in range (0, N)]

def i(mu_i, mu_ij, N) :
    """Calcule le tableau I[i, j]"""
    return [[I_ij(i, j, mu_i, mu_ij, N) for j in range(0, N)] for i in range(0, N)]

def valide_N(N) :
    """ Valide si N >= 2"""
    return N > 2

def valide_I(I) :
    """Valide si I[i, j] >= 0"""
    return np.all(np.all((I >= 0) & (I <= 1), axis=1))

def valide_V(V) :
    """Valide si V appartient a [0, 1] et somme(V[i]) = 1"""
    return np.all((V >= 0) & (V <= 1)) and (V.sum() == 1)

def valide_Lambda(Lambda) :
    """ Valide si Lambda est entre .5 et 1"""
    return (Lambda >= .5) and (Lambda < 1)

def valide_poids(poids) :
    poids = np.array(poids)
    return np.all((poids >= 1) & (poids <= 10))

def valide_poids_algo2(poids) :
    poids = np.array(poids)
    return np.all((poids >= 0) & (poids < 1)) and (poids.sum() == 1)

def valide_mu_i(mu_i) :
    mu_i = np.array(mu_i)
    return np.all((mu_i >= 0) & (mu_i <= 1))

def valide_mu_ij(mu_ij, mu_i) :
    positif = np.all(np.all((mu_ij >= 0) & (mu_ij <= 1), axis=1))
    sup_i = 1
    #Teste de la condition de mu_ij > m_i
    for i in range(0, N) :
        for j in range(i + 1, N) :
            sup_i = (mu_ij[i, j] >= mu_i[i])
            if (-sup_i) :
                return False
    return positif


def param_Valide_Algo_1(poids) :
    """Il faut que les poids soient valides"""
    return valide_poids(poids)

def param_Valide_Algo_2(V, mu_i, mu_ij, I, poids, N) :
    """Il faut que les poids soient valides"""
    return valide_N(N) and valide_poids_algo2(poids) and valide_V(V) and valide_mu_i(mu_i) and valide_mu_ij(mu_ij, mu_i) and valide_I(I)

def param_Valide_Algo_3(Lambda) :
    """Il faut que lambda soit valide"""
    return valide_Lambda(Lambda)

def parse_data(data, cols=None) :
    """Renvoie la matrice de donnees avec les colonnes selectionnees"""
    if (cols != None) :
        old_cols = data.columns
        new_cols = old_cols[cols == 1]

    return data[new_cols]

def read_profiles(File) :
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser) = read_params(File)

    content = File["Content"]

    data = pd.DataFrame(content)
    test = 'Individus' in data.columns
    if (test):
        data.set_index('Individus', inplace=True)
    # print(data)
    if ('\r' in data.columns) :
        data.drop('\r', axis=1, inplace=True)
    if (nbProfiles != None and nbProfiles > 0) :
        data = data.loc[data.index[-nbProfiles:]]
    return data

def read_data(File) :
    (utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm, nbProfiles, maximiser) = read_params(File)

    content = File["Content"]

    data = pd.DataFrame(content)
    if ('\r' in data.columns) :
        data.drop('\r', axis=1, inplace=True)
    test = 'Individus' in data.columns
    if (test):
        data.set_index('Individus', inplace=True)
    #print(data)
    if (nbProfiles != None and nbProfiles > 0) :
        data = data.loc[data.index[:-nbProfiles]]
    return data

def traite_data(data, poids) :
    """converti en float la matrice brute de donnees"""
    col_select = data.columns[np.array(poids) != 0]
    print('Colonne ')
    print(col_select)
    print('Donnees ')
    print(data)
    data[col_select] = data[col_select].apply(lambda x : pd.to_numeric(x))
    return data

def read_line_dict(data) :
    cols = data.columns
    data_res = []

    for idx in data.index :
        line_data = data.loc[idx]

        line = {}
        for i in range(len(cols)) :
            line[cols[i]] = line_data[i]
        data_res.append(line)
    return data_res

def normalize(data, normalisation=None) :
    """Normalisation des donnees brutes par reduction d'echelle """
    data_norm = data.copy()

    if (normalisation != None) :
        for x in range(len(data_norm.columns)) :
            data_norm[data_norm.columns[x]] = data_norm[data_norm.columns[x]] / normalisation[x]
    return data_norm

#print(read_params(File))
#data = read_profiles(File)
#print(data)
#(utilite, poids, mu_i, mu_ij, columns, N, Lambda, norm) = read_params(File)
#print(normalize(data, normalisation=norm))
# data['score'] = 12
# data.to_csv('resultat.csv', index=False)
#print(read_profiles(File))
#print()
# profiles = read_profiles(File)
#print(profiles)
#data = read_data(File)

#(utilite, poids, mu_i, mu_ij, I, V, columns, N, Lambda, profiles) = read_params(File)
#print(profiles)
#print(mu_i)
#print(I(mu_i, mu_ij))
#print(I_ij(2, 3, mu_i, mu_ij))
#print(V_i(2, mu_i, mu_ij))
