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

    def aw_promedio(self):
        aw_manzanas=0
        aw_kiwis=0
        aw_papas=0
        aw_zanahorias=0
        manzana=0
        kiwi=0
        papa=0
        zanahoria=0

        for alimento in self.alimentos:
            if isinstance(alimento, Manzana):
                aw_manzanas = aw_manzanas + alimento.calcular_aw()
                manzana = manzana +1
            elif isinstance(alimento, Kiwi):
                aw_kiwis = aw_kiwis + alimento.calcular_aw()
                kiwi=kiwi+1
            elif isinstance(alimento, Papa):
                aw_papas = aw_papas + alimento.calcular_aw()
                papa=papa+1
            elif isinstance(alimento, Zanahoria):
                aw_zanahorias = aw_zanahorias + alimento.calcular_aw()
                zanahoria=zanahoria+1
        
        aw_verduras=0
        for verdura in self.alimentos:
            if issubclass(type(verdura), Verdura):
                aw_verduras = aw_verduras+verdura.calcular_aw()

        aw_frutas=0
        for fruta in self.alimentos:
            if issubclass(type(fruta), Fruta):
                aw_frutas = aw_frutas+fruta.calcular_aw()

        aw_prom=0
        for alimento in self.alimentos:
            if issubclass(type(alimento), Alimento):
                aw_prom = aw_prom+alimento.calcular_aw()

        if manzana>0:
            aw_manzanas = self.redondear(aw_manzanas/manzana)

        if kiwi>0:
            aw_kiwis = self.redondear(aw_kiwis/kiwi)

        if papa>0:
            aw_papas = self.redondear(aw_papas/papa)

        if zanahoria>0:
            aw_zanahorias = self.redondear(aw_zanahorias/zanahoria)
        
        if (manzana+kiwi)>0:
            aw_frutas = self.redondear(aw_frutas/(manzana+kiwi))

        if (papa+zanahoria)>0:
            aw_verduras = self.redondear(aw_verduras/(papa+zanahoria))

        if len(self.alimentos)>0:
            aw_prom = self.redondear(aw_prom/len(self.alimentos))

        return {
            "aw_manzanas" : aw_manzanas,
            "aw_kiwis" : aw_kiwis,
            "aw_papas" : aw_papas,
            "aw_zanahorias" : aw_zanahorias,
            "aw_frutas" : aw_frutas,
            "aw_verduras" : aw_verduras,
            "aw_total" : aw_prom 
        }
  
    def redondear (self, aw_prom):
        return round(aw_prom,2)
    
    def advertencia(self, aw_promedio):
        if aw_promedio > 0.95:
            return True