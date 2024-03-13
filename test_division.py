import unittest
from division import dividir

class TestDivision(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(8,4),2)
        self.assertEqual(dividir(10,2),5)
        self.assertEqual(dividir(0,2),0)
        # Comprobar que se lanza el error al dividir entre 0
        with self.assertRaises(ValueError):
            dividir(9, 0)

if __name__ == '__main__':
    unittest.main()

