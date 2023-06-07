from modules.detectorAlimento import DetectorAlimento

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
            
    def getAlimentos (self):
        return self.alimentos
    
    
    

