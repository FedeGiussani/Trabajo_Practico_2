from modules.fruta import Fruta 

class Manzana (Fruta):
    def __init__(self):
        self.C = 15
        
    def aw_manzana(self, manzana):
        
        return (0.97 * ((self.C * manzana["peso"])**2)/(1 + (self.C * manzana["peso"])**2))
    
    