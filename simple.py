from random import randrange
def diccion_lista():
	lista = []
	#For para crear la lista de diccionarios aleatoria y con longitud de 10
	for x in range(0,10):
	
	    diccionario = {'id' : x, 'edad' : randrange(0,101)} 
	    lista.append(diccionario)
	
	return lista

def ordenar(lista):
    """La funcion debe recibir una lista de diccionarios de llaves id y edad con una longitud de 10 y devolver los valores de id que tengan mas edad y menos edad

>>> lista=[] 
>>> for x in range(0,10):
...     lista.append({'id': x, 'edad': x})
>>> ordenar(lista)
id de las personas con menos edad: [0]
id de las personas con mas edad: [9]
[{'id': 9, 'edad': 9}, {'id': 8, 'edad': 8}, {'id': 7, 'edad': 7}, {'id': 6, 'edad': 6}, {'id': 5, 'edad': 5}, {'id': 4, 'edad': 4}, {'id': 3, 'edad': 3}, {'id': 2, 'edad': 2}, {'id': 1, 'edad': 1}, {'id': 0, 'edad': 0}]


>>> lista=[{'id': 0, 'edad': 0}, {'id': 1, 'edad': 0}, {'id': 2, 'edad': 2}, {'id': 3, 'edad': 3}, {'id': 4, 'edad': 4}, {'id': 5, 'edad': 5}, {'id': 6, 'edad': 6}, {'id': 7, 'edad': 7}, {'id': 8, 'edad': 8}, {'id': 9, 'edad': 9}] 
>>> ordenar(lista)
id de las personas con menos edad: [0, 1]
id de las personas con mas edad: [9]
[{'id': 9, 'edad': 9}, {'id': 8, 'edad': 8}, {'id': 7, 'edad': 7}, {'id': 6, 'edad': 6}, {'id': 5, 'edad': 5}, {'id': 4, 'edad': 4}, {'id': 3, 'edad': 3}, {'id': 2, 'edad': 2}, {'id': 0, 'edad': 0}, {'id': 1, 'edad': 0}]


>>> ordenar(2)
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute 'sort'
    """
    
    lista2=[]
    lista3=[]
    lista.sort(reverse = True, key=lambda p: p['edad']) #Se ordena la lista
    n = 0
    for x in range(0,len(lista)):
	    if lista[len(lista)-1]['edad'] == lista[x]['edad']:
	        lista2.append(lista[x]['id'])
    for x in range(0,len(lista)):
	    if lista[0]['edad'] == lista[x]['edad']:
	        lista3.append(lista[x]['id'])
    print('id de las personas con menos edad:', lista2)
    print('id de las personas con mas edad:', lista3)
    return lista
	


import doctest
doctest.testmod() 