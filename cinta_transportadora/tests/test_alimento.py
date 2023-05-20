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

    def test_advertencia_1(self):
        al = Alimento()
        aw_prom=0.80
        alim="papa"

        self.assertIsNone(Alimento.advertencia(al,aw_prom,alim))

    def test_advertencia_2(self):
        al = Alimento()
        aw_prom=0.98
        alim="papa"

        self.assertIsNotNone(Alimento.advertencia(al,aw_prom,alim))