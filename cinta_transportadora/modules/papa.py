from modules.verduras import verduras 
import numpy as np


class papa (verduras):
    def __init__(self):
        self.C = 18
        
        
    def aw_papa(self, papa):
        
        return (0.66*(np.arctan(self.C * papa["peso"])))