from modules.fruta import Fruta 

class Manzana (Fruta):
    def __init__(self, peso):
        super().__init__()
        self.C = 15
        self.peso=peso
        
    def calcular_aw(self):
        
        return (0.97 * ((self.C * self.peso)**2)/(1 + (self.C * self.peso)**2))
    
    def getPeso(self):
        return self.peso
    