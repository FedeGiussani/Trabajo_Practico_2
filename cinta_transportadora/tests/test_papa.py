import unittest
import numpy as np
from modules.papa import Papa


class TestPapa(unittest.TestCase):

    def test_aw_papa(self):
        papa = Papa()
        papa_data = {"alimento": "papa", "peso": 25}
        
        resultado_actual = papa.aw_papa(papa_data)
        
        resultado_esperado = 0.66 * np.arctan(papa.C * papa_data["peso"])
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()