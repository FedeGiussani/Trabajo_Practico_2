import unittest
import numpy as np
from modules.zanahoria import Zanahoria

class TestZanahoria(unittest.TestCase):

    def test_aw_zanahoria(self):
        zanahoria = Zanahoria(20)
        
        resultado_actual = zanahoria.calcular_aw()
        
        resultado_esperado = 0.96 * (1 - np.exp(-10 * 20))
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()
