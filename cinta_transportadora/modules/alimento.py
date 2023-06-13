from abc import ABC, abstractmethod

class Alimento(ABC):
    def __init__(self, peso):
        self.peso=peso
        
    @abstractmethod
    def calcular_aw(self):
        pass

    @abstractmethod
    def getPeso(self):
        pass