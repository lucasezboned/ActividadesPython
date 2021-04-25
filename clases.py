from random import randrange

#Se crea la clase Circulo
class Circulo: 
    def __init__(self, radio):
        '''Se asigna el valor al atributo radio y se valida en radio.setter
>>> prueba = Circulo(-3)
Traceback (most recent call last):
    ...
TypeError: Lo siento, el valor tiene que ser mayor a 0
        '''
        
        self.radio = radio
    
    
    @property #Se añade la funcion property para interceptar el seteo del atrubito radio
    def radio(self):
        
        '''Esta funcion devuelve el valor del radio
>>> prueba = Circulo(4)
>>> print(prueba.radio)
4
        '''

        return self._radio
    
    @radio.setter #radio.setter para validar el atributo radio
    def radio(self,radio):
   
        if radio <= 0:
            raise TypeError('Lo siento, el valor tiene que ser mayor a 0')
            
        self._radio = radio
            

    def get_perimetro(self):
        '''Esta funcion devuelve el valor del perimetro del objeto
>>> prueba = Circulo(4)
>>> prueba.get_perimetro()
25.12
        '''
        return self.radio * (3.14*2)
        
    def get_area(self):
        '''Esta funcion devuelve el valor del area de dicho objeto
>>> prueba = Circulo(2)
>>> prueba.get_area()
12.56
        '''
        return (self.radio**2) * 3.14
        
    def __str__(self):
        ''' Al imprimir se devielve una presentacion amigable
>>> n = Circulo(4)
>>> print(n)
<Objeto de clase Circulo con radio de 4>
    '''
        return f"<Objeto de clase Circulo con radio de {self.radio}>"




import doctest
doctest.testmod() 