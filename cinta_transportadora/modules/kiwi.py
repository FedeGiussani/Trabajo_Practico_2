from modules.fruta import Fruta 
import numpy as np

class Kiwi (Fruta):
    def __init__(self, peso):
        super().__init__(peso) 
        self.C = 18

    def calcular_aw(self):
        
        return 0.96 * (1-(np.exp(-self.C * self.peso)))/(1 + (np.exp(-self.C * self.peso)))
    
    def getPeso(self):
        return self.peso