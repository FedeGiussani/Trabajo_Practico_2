import unittest

from modules.fruta import Fruta

class TestFruta(unittest.TestCase):
    def test_aw_prom_frutas(self):
        fr = Fruta()
        aw_prom_kiwi=0
        aw_prom_manz=0.80

        aw_prom_frutas=Fruta.aw_prom_frutas(fr,aw_prom_manz,aw_prom_kiwi)
        self.assertEqual(aw_prom_frutas, aw_prom_manz)
