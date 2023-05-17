from modules.verdura import Verdura 
import numpy as np

class Zanahoria (Verdura):
    def __init__(self):
        self.C = 10
        
    def aw_zanahoria(self, zanahoria):
        
        return (0.96*(1-np.exp(-self.C*zanahoria["peso"])))