import unittest

from modules.fruta import Fruta

class TestFruta(unittest.TestCase):
    def test_aw_prom_frutas(self):
        fr = Fruta()
        aw_prom_kiwi=0
        aw_prom_manz=0.80

        aw_prom_frutas=Fruta.aw_prom_frutas(fr,aw_prom_manz,aw_prom_kiwi)
        self.assertEqual(aw_prom_frutas, aw_prom_manz)

    def test_org_frutas(self):
        fruta = Fruta()
        frutas = [
            {"alimento": "manzana", "peso": 20},
            {"alimento": "kiwi", "peso": 15},
            {"alimento": "manzana", "peso": 10}
        ]
        
        fruta.org_frutas(frutas)
        
        manzanas = fruta.getManzana()
        kiwis = fruta.getKiwi()
        
        self.assertEqual(len(manzanas), 2)
        self.assertEqual(len(kiwis), 1)
        self.assertEqual(manzanas[0]["peso"], 20)
        self.assertEqual(manzanas[1]["peso"], 10)
        self.assertEqual(kiwis[0]["peso"], 15)

if __name__ == '__main__':
    unittest.main()
