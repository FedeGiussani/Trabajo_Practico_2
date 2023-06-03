import unittest
import numpy as np
from modules.kiwi import Kiwi

class TestKiwi(unittest.TestCase):

    def test_aw_kiwi(self):
        kiwi = Kiwi()
        kiwi_data = {"alimento": "kiwi", "peso": 25}
        
        resultado_actual = kiwi.aw_kiwi(kiwi_data)
        
        numerador = 0.96 * (1 - np.exp(-kiwi.C * kiwi_data["peso"]))
        denominador = 1 + np.exp(-kiwi.C * kiwi_data["peso"])
        resultado_esperado = numerador / denominador
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()