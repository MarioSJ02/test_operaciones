import unittest
from multiplicacion import multiplicar

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-3, -1), 3)
        self.assertEqual(multiplicar(9, -2), -18)
        self.assertEqual(multiplicar(9, 0), 0)

if __name__ == '__main__':
    unittest.main()