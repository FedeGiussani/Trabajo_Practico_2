import unittest
from modules.alimento import Alimento

class TestAlimento(unittest.TestCase):
    
    def test_aw_correcta(self):
        al = Alimento()
        aw_prom_frutas=0.50
        aw_prom_verduras=0.50
        aw_total = Alimento.aw_total(al, aw_prom_frutas, aw_prom_verduras)

        self.assertEqual(aw_total, 0.5)

    def test_aw_prom_0(self):
        al = Alimento()
        aw_prom_frutas=0.50
        aw_prom_verduras=0
        aw_total = Alimento.aw_total(al, aw_prom_frutas, aw_prom_verduras)

        self.assertEqual(aw_total, aw_prom_frutas)

    def test_redondear(self):
        alimento = Alimento()
        aw_prom = 0.82457
        
        resultado_actual = alimento.redondear(aw_prom)
        
        self.assertAlmostEqual(resultado_actual, 0.82, places=2)

    def test_advertencia_1(self):
        al = Alimento()
        aw_prom=0.80
        alim="papa"

        self.assertIsNone(Alimento.advertencia(al,aw_prom,alim))

    def test_org_alimentos(self):
        alimento = Alimento()
        alimentos = [
            {"alimento": "manzana", "peso": 20},
            {"alimento": "kiwi", "peso": 15},
            {"alimento": "papa", "peso": 30},
            {"alimento": "zanahoria", "peso": 10},
            {"alimento": "undefined", "peso": 5}
        ]
        
        alimento.org_alimentos(alimentos)
        
        frutas = alimento.getFrutas()
        verduras = alimento.getverduras()
        undefined = alimento.undefined
        
        self.assertEqual(len(frutas), 2)
        self.assertEqual(len(verduras), 2)
        self.assertEqual(len(undefined), 1)
        self.assertEqual(frutas[0]["alimento"], "manzana")
        self.assertEqual(verduras[0]["alimento"], "papa")
        self.assertEqual(undefined[0]["alimento"], "undefined")

if __name__ == '__main__':
    unittest.main()