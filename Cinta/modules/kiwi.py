from fruta import Fruta 

class Pomelo(Fruta):
    
    def __init__(self,p_peso):
        super().__init__(p_peso) 
        self._nombre =  "Pomelo"
        self._cantidad_agua = self.calcular_agua()
        self._cantidad_vitC = self.calcular_vitC()
        self._cantidad_Calcio = self.calcular_calcio()
        self._cantidad_Azucar = self.calcular_azucar()

    def calcular_agua (self):
        agua= (self._peso * 90 /100)**0.90
        return agua      

    def calcular_vitC (self):
        return self._peso * 0.0312 /100
    
        

    def calcular_calcio (self):
        return self._peso * 0.022 /100
        

    def calcular_azucar (self):
        return self._peso * 7.0 /100