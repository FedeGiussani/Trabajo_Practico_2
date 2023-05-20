import unittest

from modules.verdura import Verdura

class TestVerdura(unittest.TestCase):
    def test_aw_prom_verduras(self):
        vd = Verdura()
        aw_prom_zanahoria=0
        aw_prom_papa=0.80

        aw_prom_verduras=Verdura.aw_prom_verduras(vd,aw_prom_papa,aw_prom_zanahoria)
        self.assertEqual(aw_prom_verduras, aw_prom_papa)

    