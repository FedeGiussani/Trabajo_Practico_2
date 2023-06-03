import unittest

from modules.verdura import Verdura

class TestVerdura(unittest.TestCase):
    
    def test_aw_prom_verduras(self):
        verdura = Verdura()
        aw_prom_papas = 0.8
        aw_prom_zanahorias = 0.7

        resultado_actual = verdura.aw_prom_verduras(aw_prom_papas, aw_prom_zanahorias)

        self.assertEqual(resultado_actual, 0.75)

    def test_org_verduras(self):
        verdura = Verdura()
        alimentos = [
            {"alimento": "manzana", "peso": 20},
            {"alimento": "kiwi", "peso": 15},
            {"alimento": "papa", "peso": 30},
            {"alimento": "zanahoria", "peso": 10},
            {"alimento": "undefined", "peso": 5}
        ]

        verdura.org_verduras(alimentos)

        papas = verdura.getPapas()
        zanahorias = verdura.getZanahorias()

        self.assertEqual(len(papas), 1)
        self.assertEqual(len(zanahorias), 1)
        self.assertEqual(papas[0]["alimento"], "papa")
        self.assertEqual(zanahorias[0]["alimento"], "zanahoria")

if __name__ == '__main__':
    unittest.main()