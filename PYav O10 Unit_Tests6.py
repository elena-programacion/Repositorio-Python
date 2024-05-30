import unittest
import operaciones_aritmeticas


class Pruebas(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones_aritmeticas.Suma(8,9),17)
    def test_resta(self):
        self.assertEqual(operaciones_aritmeticas.Resta(9,3), 6)
    def test_multi(self):
        self.assertEqual(operaciones_aritmeticas.Multi(5,6),30)
    def test_divis(self):
        self.assertEqual(operaciones_aritmeticas.Divis(9,3),3)

if __name__ == '__main__':
    unittest.main()

