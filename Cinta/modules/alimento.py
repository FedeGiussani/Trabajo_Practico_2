from abc import ABC, abstractmethod

class Alimento (ABC):
    
    def __init__(self, p_peso):
        self._nombre = None
        self._cantidad_aw = None
       
        if isinstance (p_peso,float):
            self._peso = p_peso
        else:
            raise TypeError("El peso ingresado no es del tipo flotante")
   
        @abstractmethod
        def calcular_aw(self):  
            pass
  