import unittest
from modules.cajonAlimento import CajonAlimento



class TestCajonAlimento(unittest.TestCase):
    def setUp(self):
        lista_alimentos_pesos = [('zanahoria', 0.15), ('zanahoria', 0.3), 
                         ('manzana', 0.25), ('manzana', 0.3), ('papa', 0.05), 
                         ('zanahoria', 0.35), ('zanahoria', 0.3), ('kiwi', 0.4), 
                         ('papa', 0.6), ('zanahoria', 0.2), ('kiwi', 0.3), ('manzana', 0.35), 
                         ('kiwi', 0.4), ('papa', 0.45), ('kiwi', 0.45), ('kiwi', 0.15), ('kiwi', 0.2), 
                         ('kiwi', 0.25), ('kiwi', 0.3), ('manzana', 0.05)]
        
        self.cajon = CajonAlimento(lista_alimentos_pesos)

        lista_alimentos=[('manzana', 0.05), ('zanahoria', 0.05), ('kiwi', 0.5), ('papa', 0.3), ('papa', 0.15), 
                         ('kiwi', 0.4), ('manzana', 0.15), ('kiwi', 0.4), ('manzana', 0.3), ('papa', 0.25)]
        
        self.cajon_1=CajonAlimento(lista_alimentos)

    def test_aw_promedio(self):
        
        aw=self.cajon.aw_alimentos()

        self.assertEqual(aw["aw_manzanas"], 0.78)
        self.assertEqual(aw["aw_kiwis"], 0.93)
        self.assertEqual(aw["aw_papas"], 0.81)
        self.assertEqual(aw["aw_zanahorias"], 0.87)
        self.assertEqual(aw["aw_frutas"], 0.88)
        self.assertEqual(aw["aw_verduras"], 0.84)
        self.assertEqual(aw["aw_total"], 0.87)

    def test_advertencia(self):
        
        
        aw=self.cajon_1.aw_alimentos()

        for clave, valor in aw.items():
            if self.cajon_1.advertencia(valor):
                self.assertTrue(self.cajon_1.advertencia(valor))

if __name__ == '__main__':
    unittest.main()