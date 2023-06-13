import unittest
from modules.manzana import Manzana

class TestManzana(unittest.TestCase):
    def setUp(self):
        self.manzana=Manzana(0.3)
        self.manzana_1=Manzana(0)
        self.manzana_2=Manzana(0.6)
    

    def test_aw_manzana(self):
        
        resultado_actual = self.manzana.calcular_aw()
        
        resultado_esperado = 0.97 * ((15 * 0.30)**2) / (1 + (15 * 0.30)**2)
        
        self.assertAlmostEqual(resultado_actual, resultado_esperado, places=2)

        self.assertEqual(self.manzana_1.calcular_aw(), 0)
        self.assertLess(self.manzana_2.calcular_aw(), 1)


if __name__ == '__main__':
    unittest.main()