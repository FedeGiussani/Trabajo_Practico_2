import unittest
from modules.cajonAlimento import CajonAlimento
from modules.manzana import Manzana
from modules.kiwi import Kiwi
from modules.papa import Papa
from modules.zanahoria import Zanahoria

lista_alimentos_pesos = [('zanahoria', 0.15), ('zanahoria', 0.3), 
                         ('manzana', 0.25), ('manzana', 0.3), ('papa', 0.05), 
                         ('zanahoria', 0.35), ('zanahoria', 0.3), ('kiwi', 0.4), 
                         ('papa', 0.6), ('zanahoria', 0.2), ('kiwi', 0.3), ('manzana', 0.35), 
                         ('kiwi', 0.4), ('papa', 0.45), ('kiwi', 0.45), ('kiwi', 0.15), ('kiwi', 0.2), 
                         ('kiwi', 0.25), ('kiwi', 0.3), ('manzana', 0.05)]

class TestCajonAlimento(unittest.TestCase):
    
    
    def test_aw_manzanas(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        aw_manzanas = cajon.aw_manzanas()

        self.assertEqual(aw_manzanas, 0.78)

    def test_aw_kiwis(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        aw_kiwis = cajon.aw_kiwis()
        self.assertEqual(aw_kiwis, 0.93)

    def test_aw_papas(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        aw_papas = cajon.aw_papas()

        self.assertEqual(aw_papas, 0.81)

    def test_aw_zanahorias(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        aw_zanahorias = cajon.aw_zanahorias()

        self.assertEqual(aw_zanahorias, 0.87)

    def test_prom_frutas(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        prom_frutas = cajon.aw_prom_frutas()

        self.assertEqual(prom_frutas, 0.88)

    def test_prom_verduras(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        prom_verduras = cajon.aw_prom_verduras()

        self.assertEqual(prom_verduras, 0.84)

    def test_prom_total(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)
        total = cajon.aw_total()

        self.assertEqual(total, 0.87)

    def test_advertencia(self):
        
        lista_alimentos=[('manzana', 0.05), ('zanahoria', 0.05), ('kiwi', 0.5), ('papa', 0.3), ('papa', 0.15), ('kiwi', 0.4), ('manzana', 0.15), ('kiwi', 0.4), ('manzana', 0.3), ('papa', 0.25)]
        
        cajon=CajonAlimento(lista_alimentos)
        aw_kiwis=cajon.aw_kiwis()
        print(aw_kiwis)
        self.assertTrue(cajon.advertencia(aw_kiwis))

    def test_clasificar_alim(self):
        global lista_alimentos_pesos

        cajon=CajonAlimento(lista_alimentos_pesos)

        frutas=cajon.getFrutas()
        verduras=cajon.getVerduras()
        kiwis=cajon.getKiwis()
        manzanas=cajon.getManzanas()
        papas=cajon.getPapas()
        zanahorias=cajon.getZanahorias()

        self.assertEqual(len(frutas), 12)
        self.assertEqual(len(verduras), 8)
        self.assertEqual(len(kiwis), 8)
        self.assertEqual(len(manzanas), 4)
        self.assertEqual(len(papas), 3)
        self.assertEqual(len(zanahorias), 5)

        for manzana in manzanas:
            self.assertIsInstance(manzana, Manzana)
        for kiwi in kiwis:
            self.assertIsInstance(kiwi, Kiwi)
        for papa in papas:
            self.assertIsInstance(papa, Papa)
        for zanahoria in zanahorias:
            self.assertIsInstance(zanahoria, Zanahoria)

        self.assertEqual(manzanas[0].getPeso(), 0.25)
        self.assertEqual(kiwis[2].getPeso(), 0.4)
        self.assertEqual(papas[1].getPeso(), 0.6)
        self.assertEqual(zanahorias[4].getPeso(), 0.2)

if __name__ == '__main__':
    unittest.main()