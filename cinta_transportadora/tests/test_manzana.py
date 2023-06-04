import unittest
from modules.manzana import Manzana

class TestManzana(unittest.TestCase):

    def test_aw_manzana(self):
        manzana = Manzana(30)
                
        resultado_actual = manzana.calcular_aw()
        
        resultado_esperado = 0.97 * ((15 * 30)**2) / (1 + (15 * 30)**2)
        
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

if __name__ == '__main__':
    unittest.main()