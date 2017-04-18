# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import pandas as pd
import json
from pprint import pprint

File = {"Profiles" : { "Academie" : [2, 3, 4], "Departement" : [5, 6, 7], "Dernier" : [8, 9, 10] },
        "Contenu" : { "Academie" : [2, 3, 4], "Departement" : [5, 6, 7], "Dernier" : [8, 9, 10] },
        "Parametres" : { "N" : [4], "Departement" : [5, 6, 7], "Dernier" : [8, 9, 10] }
}



#Liste des paramètres 
utilite = 0 #fonction par defaut (à définir)
poids = None
mu_i = None
mu_ij = None
I = None
V = None
columns = None
N = 0 #Ce paramètre doit etre renseigné avant mu_ij 
Lambda = 0
profiles = None


#poids; liste des poids pour chaque critère séparés par un ;
#params = ['N;4', 'mu_ij;.1;.3;.4;.6;.7;.9;', 'mu_i;.001;.003;.006;.01']


def read_params(File) :
    utilite = 0 #fonction par defaut (à définir)
    poids = None
    mu_i = None
    mu_ij = None
    I = None
    V = None
    columns = None
    N = 0 #Ce paramètre doit etre renseigné avant mu_ij 
    Lambda = 0
    profiles = None

    params = File['Parametres']
    for param_c, value_param in params.items() :
        #param_c = p.split(';')
        
        #Nombre de critères
        if (param_c == 'N') :
            N = int(value_param[0])
        
        #lambda
        if (param_c == 'lambda') :
            Lambda = float(value_param[0])
            
        #Poids
        if ((param_c == 'poids') or (param_c == 'w') or (param_c == 'v')) :
            poids = []
            for x in value_param :
                poids = poids + [float(x)]
    
        #colonne
        if ((param_c == 'colonne') or (param_c == 'cols') or (param_c == 'columns')) :
            columns = []
            for x in value_param :
                columns = columns + [float(x)]
        
        #Utilité
        if ((param_c == 'utilite') or (param_c == 'u')) :
            utilite = int(value_param[0])
        
        #params = ['mu_i;1;3;4;5', '']
        
        #param_c = params[0].split(';')
        #param_c[1:] = map(lambda x : float(x), param_c[1:])
        
        #mu_i
        if (param_c == 'mu_i') :
            mu_i = []
            for x in value_param :
                mu_i = mu_i + [float(x)]
        
        
        if (N > 0 and param_c == 'mu_ij') :
            mu_ij = np.zeros((N, N))
            idx = 1
            for i in range(0, N) :
                for j in range(i, N) :
                    if (i != j) :
                        mu_ij[i, j] = float(value_param[idx])
                        mu_ij[j, i] = mu_ij[i, j]
                        idx = idx + 1
                        
    return (utilite, poids, mu_i, mu_ij, I, V, columns, N, Lambda, profiles)
    
def I_ij(i, j, mu_i, mu_ij) :
    #print(mu_ij[i, j] , mu_i[i], mu_i[j])
    return 0 if (i == j) else mu_ij[i, j] - mu_i[i] - mu_i[j]
    
def V_i(i, mu_i, mu_ij) :
    tmp_I = [I_ij(i, j, mu_i, mu_ij) for j in range(0, N) if (j != i)]
    tmp_I = np.array(tmp_I).sum()
        
    return mu_i[i] - .5 * tmp_I

def V(mu_i, mu_ij) :
    """Calcule le tableau V[i]"""
    return [V_i(i, mu_i, mu_ij) for i in range (0, N)]

def I(mu_i, mu_ij) :
    """Calcule le tableau I[i, j]"""
    return [[I_ij(i, j, mu_i, mu_ij) for j in range(0, N)] for i in range(0, N)]

def valide_N(N) :
    """ Valide si N >= 2"""
    return N > 2
    
def valide_I(I) :
    """Valide si I[i, j] >= 0"""
    return np.all(np.all((I >= 0) & (I <= 1), axis=1)) 
    
def valide_V(V) :
    """Valide si V appartient à [0, 1] et somme(V[i]) = 1"""
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

    
poids = [1, 3, 5]
#print(valide_poids(poids))
#print(poids)  

def param_Valide_Algo_1() :
    """Il faut que les poids soient valides"""
    return valide_poids(poids)

def param_Valide_Algo_2() :
    """Il faut que les poids soient valides"""
    return valide_V(V) and valide_mu_i(mu_i) and valide_mu_ij(mu_ij, mu_i) and valide_I(I) 
    
def param_Valide_Algo_3() :
    """Il faut que lambda soit valide"""
    return valide_Lambda(Lambda)
    
def parse_data(data, cols=None) :
    """Renvoie la matrice de données avec les colonnes selectionnées"""
    if (cols != None) :
        old_cols = data.columns
        new_cols = old_cols[cols == 1]
    
    return data[new_cols]

def read_profiles(File) :
    content = File["Profiles"]
    
    profiles = pd.DataFrame(content)
    return profiles
    
def read_data(File) :
    content = File["Contenu"]
    
    data = pd.DataFrame(content)
    return data


    
#print(param_c)
profiles = read_profiles(File)
data = read_data(File)

(utilite, poids, mu_i, mu_ij, I, V, columns, N, Lambda, profiles) = read_params(File)
print(N)
#print(mu_i)
#print(I(mu_i, mu_ij))
#print(I_ij(2, 3, mu_i, mu_ij))
#print(V_i(2, mu_i, mu_ij))


