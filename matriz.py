        
from random import randrange
def matrizrandomizada():
    x=0
    matriz= []
    conse = 0
    
    for x in range(0,5):
        matriz.append([randrange(0,100),randrange(0,100),randrange(0,100),randrange(0,100),randrange(0,100)])
    return (matriz)
    
    
    
    
    
def consecutivos(matriz):
    '''Encuentra (si es que hay) 4 numeros consecutivos horizontales o verticales en una matriz 5x5
    
    
    
>>> matriz=[[4,4,2,2,2],[4,4,2,7,2],[4,4,2,0,2],[4,4,4,4,2],[4,2,1,1,2]]
>>> consecutivos(matriz)
Consecutivos horizontales:
4 numeros consecutivos entre [ 3 ][ 0 ] y[ 3 ] [ 3 ]
<BLANKLINE>
Consecutivos verticales:
4 numeros consecutivos entre [ 0 ][ 0 ] y[ 3 ] [ 0 ]
4 numeros consecutivos entre [ 0 ][ 1 ] y[ 3 ] [ 1 ]
4 numeros consecutivos entre [ 0 ][ 4 ] y[ 3 ] [ 4 ]
4 numeros consecutivos entre [ 1 ][ 4 ] y[ 4 ] [ 4 ]
    '''
    conse = 0 # Numeros consecutivos
    vencontrados = 0 #para saber si se encontro algun consecutivo vertical
    hencontrados = 0 #
    
    
    
    #Primero se buscan los numeros consecutivos horizontales y luego los verticales
    
    
    print ('Consecutivos horizontales:')
    for fila in range(4): #Como hay 5 filas se crea un bucle de 5 vueltas
        for n in range(2): #puede haber 4 numeros consecutivos horizontales de la posicion 0 a la 3 y de la 1 a la 4. En el primer vuelta se comprueba las posiciones 0 a 3 de la fila y en el segundo de 1 a 4.
            matriz2=matriz[fila][n:n+4]
            
            cont = matriz2.count(matriz2[n])
            
            if cont == 4:
                hencontrados = 1
                print('4 numeros consecutivos entre [',fila,'][', n, '] y[', fila,']','[', n+3, ']')
            cont = 0
    
    matriz3=[]
    if hencontrados == 0:
        print('No hay 4 numeros consecutivos horizontales')
    
    
    
    print('')
    print ('Consecutivos verticales:')
    #Se divide la comprobacion en dos for uno para comprobar de la posicion 0 a 3 de cada columna y otro de la posicion 1 a 4
    for columna in range(0,5):
        
        for x in range(0,4): #Se toman los primeros 4 numeros de cada columna y se comprueba
            
            matriz3.append(matriz[x][columna])
        cont = matriz3.count(matriz3[0])
        if cont == 4:
            print('4 numeros consecutivos entre [',x-3,'][', columna, '] y[', x,']','[', columna, ']')
            vencontrados=1
        matriz3=[]
        
    
    
        
    for columna in range (1,5):
        for x in range(1,5): #Se toman los ultimos 4 numeros de cada columna y se comprueba
           
            matriz3.append(matriz[x][columna])
        cont = matriz3.count(matriz3[0])
        if cont == 4:
            print('4 numeros consecutivos entre [',x-3,'][',columna, '] y[', x,']','[', columna, ']')
            vencontrados=1
        matriz3=[]
    if vencontrados == 0:
        print('No hay 4 numeros consecutivos horizontales')








import doctest
doctest.testmod() 


