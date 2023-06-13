from modules.verdura import Verdura 
import numpy as np


class Papa (Verdura):
    def __init__(self, peso):
        super().__init__(peso)
        self.C = 18
      
    def calcular_aw(self):
        
        return (0.66*(np.arctan(self.C * self.peso)))
    
    def getPeso(self):
        return self.peso