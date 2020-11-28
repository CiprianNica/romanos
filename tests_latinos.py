import unittest
from romanos import *

class RomanosTest(unittest.TestCase):
    def test_descomponer(self):
        self.assertEqual(descomponer(1987), [1,9,8,7])

    def test_convertir_1987(self):
        self.assertEqual(convertir([9, 8, 7]), 'CMLXXXVII')
    
    def test_entero_a_romano(self):
        self.assertEqual(entero_a_romano(1987), 'MCMLXXXVII')
        self.assertRaises(OverflowError, entero_a_romano, 4000)
        self.assertRaises(OverflowError, entero_a_romano, 0)
        self.assertRaises(SyntaxError, entero_a_romano, 1987.0)


if __name__ == '__main__':
    unittest.main()