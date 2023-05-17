from modules.alimento import alimento 


class frutas (alimento):
    def __init__(self):
        self.kiwis = [] 
        self.manzanas = []
        self.aw_total 
       

    def aw_prom_frutas(self, aw_prom_manzanas, aw_prom_kiwis):
        if aw_prom_kiwis > 0 :
            if  aw_prom_manzanas >0: 
                return (aw_prom_manzanas + aw_prom_kiwis)/2
        
        if aw_prom_manzanas > 0:
            return aw_prom_manzanas
        
        if aw_prom_kiwis > 0:
            return aw_prom_kiwis
        
        return 0
        
    def org_frutas(self, x):
        for ali in x:
            if ali['alimento'] == "manzana":
                self.manzanas.append(ali)
            
            elif ali['alimento'] == "kiwi":
                self.kiwis.append(ali)
                
                
    def getKiwi (self):
        return self.kiwis
    
    def getManzana (self):
        return self.manzanas
    
    