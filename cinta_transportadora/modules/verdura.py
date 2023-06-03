from modules.alimento import Alimento 
from abc import ABC, abstractmethod

class Verdura(Alimento, ABC):

    @abstractmethod
    def calcular_aw(self):
        pass
       
    def getPapas(self):
        return self.papas
        
    def getZanahorias(self):
        return self.zanahorias