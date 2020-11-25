import unittest
from romanos import *

class RomanosTest(unittest.TestCase):
    def test_descomponer(self):
        self.assertEqual(descomponer(1987), (1,9,8,7))

    def test_descomponer_solo_enteros(self):
        self.assertRaises(SyntaxError), descomponer, 1987, 0)

    def test_convertir_987(self):
        self.assertEqual(convertir([9, 8, 7]), 'CMLXXXVIII')

    def test_entero_a_romano(self):
        self.assertEqual(entero_a_romano)
if __name__ == '__main__':
    unittest.main()