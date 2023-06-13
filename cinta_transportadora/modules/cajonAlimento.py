from modules.manzana import Manzana
from modules.kiwi import Kiwi
from modules.papa import Papa
from modules.zanahoria import Zanahoria
from modules.alimento import Alimento
from modules.verdura import Verdura
from modules.fruta import Fruta

class CajonAlimento():
    def __init__(self, lista_alimentos_pesos):
        self.lista_alim_pesos=lista_alimentos_pesos #lista de tuplas de (alim,peso)
        self.alimentos=[]
        self.org_alimentos() #organiza los alimentos creando objetos en la lista alimentos 
        
    def org_alimentos(self): #crea una lista de objetos alimentos
        for alimento in self.lista_alim_pesos:
            if alimento[0] == "manzana":
                self.alimentos.append(Manzana(alimento[1]))
            
            elif alimento[0] == "kiwi":
                self.alimentos.append(Kiwi(alimento[1]))

            elif alimento[0] == "papa":
                self.alimentos.append(Papa(alimento[1]))
            
            elif alimento[0] == "zanahoria":
                self.alimentos.append(Zanahoria(alimento[1]))

    def aw_promedio(self, clase):
        aw=0
        al=0
        for alimento in self.alimentos:
            if isinstance(alimento, clase):
                aw = aw + alimento.calcular_aw()
                al = al +1
        if al>0:
            return self.redondear(aw/al)
        return 0

    def aw_alimentos(self):
        
        return {
            "aw_manzanas" : self.aw_promedio(Manzana),
            "aw_kiwis" : self.aw_promedio(Kiwi),
            "aw_papas" : self.aw_promedio(Papa),
            "aw_zanahorias" : self.aw_promedio(Zanahoria),
            "aw_frutas" : self.aw_promedio(Fruta),
            "aw_verduras" : self.aw_promedio(Verdura),
            "aw_total" : self.aw_promedio(Alimento) 
        }
  
    def redondear (self, aw_prom):
        return round(aw_prom,2)
    
    def advertencia(self, aw_promedio):
        if aw_promedio > 0.95:
            return True