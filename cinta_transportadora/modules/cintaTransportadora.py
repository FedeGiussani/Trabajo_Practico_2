from modules.deteccion import DetectorAlimento as det

    
detector = det()
class CintaTransportadora:

    def __init__(self):
        self.alimentos = [] # vacio porque se va a ir llenando
        
    def iniciar_transporte(self,alimentos_cajon):
        i = 0
        while i < alimentos_cajon:
            alimento = det.detectar_alimento(detector)
            self.alimentos.append(alimento)
            i= i + 1
            
    def getAlimentos (self):
        
        return self.alimentos
            

            
    
        

     
