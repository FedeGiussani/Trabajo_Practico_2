from modules.manzana import Manzana
from modules.kiwi import Kiwi
from modules.papa import Papa
from modules.zanahoria import Zanahoria

class CajonAlimento():
    def __init__(self, lista_alimentos_pesos):
        self.lista_alim_pesos=lista_alimentos_pesos #lista de tuplas de (alim,peso)
        self.frutas = []
        self.verduras = []
        self.kiwis = [] 
        self.manzanas = []
        self.papas = [] 
        self.zanahorias = []
        self.org_alimentos() #organiza alimentos en dos listas de objetos Fruta() y Verdura()
        self.org_frutas() #organiza frutas en dos listas de objetos Manzana() y Kiwi()
        self.org_verduras() #organiza verduras en dos listas de objetos Papa() y Zanahoria()
    
    def getFrutas(self):
        return self.frutas
    
    def getVerduras(self):
        return self.verduras
    
    def getKiwis(self):
        return self.kiwis

    def getManzanas(self):
        return self.manzanas
    
    def getPapas(self):
        return self.papas
    
    def getZanahorias(self):
        return self.zanahorias
    
    def org_alimentos(self): #organiza los alimentos en listas de verduras y frutas y crea objetos de cada alimento
        for alimento in self.lista_alim_pesos:
            if alimento[0] == "manzana":
                self.frutas.append(Manzana(alimento[1]))
            
            elif alimento[0] == "kiwi":
                self.frutas.append(Kiwi(alimento[1]))

            elif alimento[0] == "papa":
                self.verduras.append(Papa(alimento[1]))
            
            elif alimento[0] == "zanahoria":
                self.verduras.append(Zanahoria(alimento[1]))

    def org_frutas(self): #organiza los alimentos en listas de objetos manzanas y kiwis
        for alimento in self.lista_alim_pesos:
            if alimento[0] == "manzana":
                self.manzanas.append(Manzana(alimento[1]))
            
            elif alimento[0] == "kiwi":
                self.kiwis.append(Kiwi(alimento[1]))
    
    def org_verduras(self): #organiza los alimentos en listas de objetos papas y zanahorias
        for alimento in self.lista_alim_pesos:
            if alimento[0] == "papa":
                self.papas.append(Papa(alimento[1]))
            
            elif alimento[0] == "zanahoria":
                self.zanahorias.append(Zanahoria(alimento[1]))

    def aw_manzanas(self):
        aw_manzanas=0
        if len(self.manzanas) > 0: #control de que hay manzanas 
            for manzana in self.manzanas:
                aw_manzanas = aw_manzanas + manzana.calcular_aw()
            
            return self.redondear(aw_manzanas/len(self.manzanas))
        return 0
    
    def aw_kiwis(self):
        aw_kiwis=0
        if len(self.kiwis) > 0: #control de que hay kiwis
            for kiwi in self.kiwis:
                aw_kiwis = aw_kiwis + kiwi.calcular_aw()
            
            return self.redondear(aw_kiwis/len(self.kiwis))
        return 0
    
    def aw_papas(self):
        aw_papas=0
        if len(self.papas) > 0: #control de que hay papas
            for papa in self.papas:
                aw_papas = aw_papas + papa.calcular_aw()
            return self.redondear(aw_papas/len(self.papas))
        return 0
    
    def aw_zanahorias(self):
        aw_zanahorias=0
        if len(self.zanahorias) > 0: #control de que hay zanahorias
            for zanahoria in self.zanahorias:
                aw_zanahorias = aw_zanahorias + zanahoria.calcular_aw()
            
            return self.redondear(aw_zanahorias/len(self.zanahorias))
        return 0
    
    def aw_prom_frutas(self):
        aw_frutas=0
        if len(self.frutas)>0: #control de que hay frutas
            for fruta in self.frutas:
                aw_frutas = aw_frutas + fruta.calcular_aw()
            return self.redondear(aw_frutas/len(self.frutas))
        return 0
    
    def aw_prom_verduras(self):
        aw_verduras = 0
        if len(self.verduras)>0:
            for verdura in self.verduras:
                aw_verduras = aw_verduras + verdura.calcular_aw()
            return self.redondear(aw_verduras/len(self.verduras))
        return 0

    def aw_total(self):
        aw_verduras = 0
        for verdura in self.verduras:
            aw_verduras = aw_verduras + verdura.calcular_aw()
        aw_frutas=0
        for fruta in self.frutas:
            aw_frutas = aw_frutas + fruta.calcular_aw()
        
        return self.redondear((aw_verduras+aw_frutas)/(len(self.verduras)+len(self.frutas)))
    
    def redondear (self, aw_prom):
        return round(aw_prom,2)
    
    def advertencia(self, aw_promedio):
        if aw_promedio > 0.95:
            return True