
#PARAMS DE TEST

Nespresso = {'qualite' : 3.0, 'fonctionnalite' : 2.0}
Tassimo = {'qualite' : 2.0, 'fonctionnalite' : 1.0}
Cfe = {'qualite' : 3.0, 'fonctionnalite' : 2.0}


poids = {'qualite':3.0, 'fonctionnalite':6.0}

def utilite_marginale_unit(n,I):
	#Cette fonction servira à normaliser l'utlité marginale (sera appelée au niveau du test final --> tout en bas du code)



def sommePonderee (utilite_marginale, poids):
    
    SommeP = 0
    if(utilite_marginale == {} or poids =={}):
        return 'ERROR'
    else:
        for i,j in zip(utilite_marginale.values(), poids.values()):
            SommeP += i * j;
    return SommeP



print(sommePonderee(utilite_marginale_unit(Nespresso),poids));