from modules.verdura import Verdura 
import numpy as np


class Papa (Verdura):
    def __init__(self, peso):
        super().__init__()
        self.C = 18
        self.peso=peso
        
        
    def calcular_aw(self):
        
        return (0.66*(np.arctan(self.C * self.peso)))