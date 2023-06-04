from modules.alimento import Alimento 
from abc import ABC, abstractmethod

class Verdura(Alimento, ABC):

    @abstractmethod
    def calcular_aw(self):
        pass
    
    @abstractmethod
    def getPeso(self):
        pass