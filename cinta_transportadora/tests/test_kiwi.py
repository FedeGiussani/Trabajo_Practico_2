import unittest
import numpy as np
from modules.kiwi import Kiwi

class TestKiwi(unittest.TestCase):

    def test_aw_kiwi(self):
        kiwi = Kiwi(25)
        
        resultado_actual = kiwi.calcular_aw()
        
        numerador = 0.96 * (1 - np.exp(-18 * 25))
        denominador = 1 + np.exp(-18 * 25)
        resultado_esperado = numerador / denominador
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()