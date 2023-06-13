from modules.verdura import Verdura 
import numpy as np

class Zanahoria(Verdura):
    def __init__(self, peso):
        super().__init__(peso)
        self.C = 10
        
    def calcular_aw(self):
        return (0.96*(1-np.exp(-self.C*self.peso)))
    
    def getPeso(self):
        return self.peso