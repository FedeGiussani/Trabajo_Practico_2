import unittest
import numpy as np
from modules.zanahoria import Zanahoria

class TestZanahoria(unittest.TestCase):
    def setUp(self):
        self.zanahoria = Zanahoria(0.20)

    def test_aw_zanahoria(self):
        
        resultado_actual = self.zanahoria.calcular_aw()
        
        resultado_esperado = 0.96 * (1 - np.exp(-10 * 0.20))
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()
