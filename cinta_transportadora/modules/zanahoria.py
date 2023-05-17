from modules.verduras import verduras 
import numpy as np

class zanahoria (verduras):
    def __init__(self):
        self.C = 10
        
    def aw_zanahoria(self, zanahoria):
        
        return (0.96*(1-np.exp(-self.C*zanahoria["peso"])))