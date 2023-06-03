from modules.deteccion import DetectorAlimento
from modules.alimento import Alimento
from modules.cajon_alimentos import Cajon_alimentos


#detector = det()
#al = Alimento()
#cajon=Cajon_alimentos()

class CintaTransportadora:

    def __init__(self):
        self.alimentos = [] # vacio porque se va a ir llenando
        self.detector=DetectorAlimento()
        
    def iniciar_transporte(self,alimentos_cajon):
        #este ciclo llena las listas de alimentos y pesos
        i = 0
        while i < alimentos_cajon:
            alimento = self.detector.detectar_alimento()
            if alimento["alimento"] != "undefined": #aca se hace el control de alimentos 
                aux=(alimento["alimento"], alimento["peso"])
                self.alimentos.append(aux)
                i= i + 1



        """cajon.org_alimentos(self.alimentos)
        cajon.org_frutas(self.alimentos)
        cajon.org_verduras(self.alimentos)

        for kiwi in cajon.getKiwis():
            aw_prom_kiwi = kiwi.calcular_aw()
            print(aw_prom_kiwi)

        for zanahoria in cajon.getZanahorias():
            aw_prom_zanahorias = zanahoria.calcular_aw()
            print(aw_prom_zanahorias)"""


            
    def getAlimentos (self):
        return self.alimentos
    
    def getPesos (self):
        return self.pesos
    
    

