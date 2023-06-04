from abc import ABC, abstractmethod

class Alimento(ABC):
        
    @abstractmethod
    def calcular_aw(self):
        pass

    @abstractmethod
    def getPeso(self):
        pass