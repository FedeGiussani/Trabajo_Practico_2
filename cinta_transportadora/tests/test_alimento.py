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

    def advertencia(self):
        
