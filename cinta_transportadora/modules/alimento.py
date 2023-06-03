from abc import ABC, abstractmethod

class Alimento(ABC):
        
    @abstractmethod
    def calcular_aw(self):
        pass

    def advertencia(self, aw_promedio):
        if aw_promedio > 0.95:
            return True

    def advertencia_web(self, aw_promedio, alim):
        
        if aw_promedio > 0.95:
            return alim
        return 0
            
    

            