from Alimento import alimento 

class Manzana(alimento):
    
    def __init__(self,p_peso):
        super().__init__(p_peso)  #Constructor de la clase padre
        self._nombre =  "Manzana"
        self._cantidad_aw = self.calcular_agua()
  
    def calcular_aw (self):
        c_manzana=15000
        aw_manzana=  0.97 *( (pow(c_manzana*peso)) / (1 + (pow(c_manzana*peso))))
        return aw_manzana

