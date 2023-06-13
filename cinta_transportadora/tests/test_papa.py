import unittest
import numpy as np
from modules.papa import Papa


class TestPapa(unittest.TestCase):
    def setUp(self):
        self.papa = Papa(0.25)

    def test_aw_papa(self):
                
        resultado_actual = self.papa.calcular_aw()
        
        resultado_esperado = 0.66 * np.arctan(18 * 0.25)
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()