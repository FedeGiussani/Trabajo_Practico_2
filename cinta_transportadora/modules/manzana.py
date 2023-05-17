from modules.frutas import frutas 

class manzana (frutas):
    def __init__(self):
        self.C = 15
        
    def aw_manzana(self, manzana):
        
        return (0.97 * ((self.C * manzana["peso"])**2)/(1 + (self.C * manzana["peso"])**2))
    
    