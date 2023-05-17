from modules.alimento import alimento 


class verduras (alimento):
    def __init__(self):
        self.papas = [] 
        self.zanahorias = [] 
        
    def aw_prom_verduras(self, aw_prom_papas, aw_prom_zanahorias):
        
        if  aw_prom_zanahorias > 0:
            if  aw_prom_papas > 0:
                return (aw_prom_papas + aw_prom_zanahorias)/2
        
        if aw_prom_zanahorias > 0:
            return aw_prom_zanahorias
        
        if aw_prom_papas > 0:
            return aw_prom_papas
        
        return 0
        
    def getAwTotalVerduras (self):
        return self.aw_prom_verduras
        
    def org_verduras(self, x):
        for ali in x:
            if ali['alimento'] == "papa":
                self.papas.append(ali)
            
            elif ali['alimento'] == "zanahoria":
                self.zanahorias.append(ali)
                
    
    def getPapas(self):
        return self.papas
        
    def getZanahoria(self):
        return self.zanahorias