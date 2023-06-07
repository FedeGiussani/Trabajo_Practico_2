import unittest
from modules.cintaTransportadora import CintaTransportadora
from modules.detectorAlimento import DetectorAlimento as det


class TestCintaTransportadora(unittest.TestCase):

    def setUp(self):
        self.detector = det()
        self.cinta = CintaTransportadora()

    def test_iniciar_transporte(self):
        alimentos_cajon = 5
        self.cinta.iniciar_transporte(alimentos_cajon)
        self.assertEqual(len(self.cinta.getAlimentos()), alimentos_cajon)

    def test_getAlimentos(self):
        alimentos_cajon = 3
        self.cinta.iniciar_transporte(alimentos_cajon)
        alimentos = self.cinta.getAlimentos()
        self.assertEqual(len(alimentos), alimentos_cajon)
        self.assertListEqual(alimentos, self.cinta.alimentos)

    def test_getAlimentos_vacio(self):
        alimentos = self.cinta.getAlimentos()
        self.assertEqual(len(alimentos), 0)
        self.assertListEqual(alimentos, [])

if __name__ == '__main__':
    unittest.main()