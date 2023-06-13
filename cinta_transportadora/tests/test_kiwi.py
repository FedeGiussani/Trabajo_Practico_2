import unittest
import numpy as np
from modules.kiwi import Kiwi

class TestKiwi(unittest.TestCase):
    def setUp(self):
        self.kiwi = Kiwi(0.25)

    def test_aw_kiwi(self):
        
        
        resultado_actual = self.kiwi.calcular_aw()
        
        numerador = 0.96 * (1 - np.exp(-18 * 0.25))
        denominador = 1 + np.exp(-18 * 0.25)
        resultado_esperado = numerador / denominador
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()