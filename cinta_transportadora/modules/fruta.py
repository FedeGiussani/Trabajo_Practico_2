from modules.alimento import Alimento 
from abc import ABC, abstractmethod

class Fruta (Alimento, ABC):
        
    @abstractmethod
    def calcular_aw(self):
        pass
                
    def getKiwi (self):
        return self.kiwis
    
    def getManzana (self):
        return self.manzanas
    
    