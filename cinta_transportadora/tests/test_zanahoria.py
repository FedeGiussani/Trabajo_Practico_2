import unittest
import numpy as np
from modules.zanahoria import Zanahoria

class TestZanahoria(unittest.TestCase):

    def test_aw_zanahoria(self):
        zanahoria = Zanahoria()
        zanahoria_data = {"alimento": "zanahoria", "peso": 20}
        
        resultado_actual = zanahoria.aw_zanahoria(zanahoria_data)
        
        resultado_esperado = 0.96 * (1 - np.exp(-zanahoria.C * zanahoria_data["peso"]))
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()
