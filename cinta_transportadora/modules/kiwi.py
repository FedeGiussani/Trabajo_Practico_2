from modules.fruta import Fruta 
import numpy as np

class Kiwi (Fruta):
    def __init__(self): 
        self.C = 18
        
    def aw_kiwi(self, kiwi):
        
        return 0.96 * (1-(np.exp(-self.C * kiwi["peso"])))/(1 + (np.exp(-self.C * kiwi["peso"])))