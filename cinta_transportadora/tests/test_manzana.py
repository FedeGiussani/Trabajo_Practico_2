import unittest
from modules.manzana import Manzana

class TestManzana(unittest.TestCase):

    def test_aw_manzana(self):
        manzana = Manzana()
        manzana_data = {"alimento": "manzana", "peso": 30}
        
        resultado_actual = manzana.aw_manzana(manzana_data)
        
        peso = manzana_data["peso"]
        resultado_esperado = 0.97 * ((manzana.C * peso)**2) / (1 + (manzana.C * peso)**2)
        
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()