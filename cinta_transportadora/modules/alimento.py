class Alimento:

    def __init__(self):
        self.frutas = []
        self.verduras = []
        self.undefined = []
        
    def getFrutas (self):
        return self.frutas
    
    def getverduras (self):
        return self.verduras
        
    def aw_total(self, aw_prom_frutas, aw_prom_verduras):
        if aw_prom_frutas > 0:
            if aw_prom_verduras > 0 :
                return (aw_prom_frutas + aw_prom_verduras)/2
        
        if aw_prom_frutas > 0:
            return aw_prom_frutas
        
        if aw_prom_verduras > 0:
            return aw_prom_verduras
        
    def org_alimentos(self,x):
        for alimento in x:
            if alimento['alimento'] == "manzana":
                self.frutas.append(alimento)
            
            elif alimento['alimento']== "kiwi":
                self.frutas.append(alimento)

            elif alimento['alimento'] == "papa":
                self.verduras.append(alimento)
            
            elif alimento['alimento'] == "zanahoria":
                self.verduras.append(alimento)
            
            elif alimento['alimento'] == "undefined":
                self.undefined.append(alimento)
    
    def advertencia(self, aw_promedio, alim):
        
        if aw_promedio > 0.95:
            print("La actividad acuosa de " + alim + " supera el 0.95")
            
    def redondear (self, aw_prom):
        return round(aw_prom,2)

            