import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4, -2), 2)
        self.assertEqual(self.calc.add(-10,-5), -15)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(4, -2), 6)
        self.assertEqual(self.calc.subtract(-9,-5), -4)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(4, -2), -8)
        self.assertEqual(self.calc.multiply(-9,-5), 45)

    def test_divide(self):
        self.assertEqual(self.calc.divide(-5, -2), 2)
        self.assertEqual(self.calc.divide(-4, 3), -1)
        self.assertEqual(self.calc.divide(19,5), 3)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, -2), -1)
        self.assertEqual(self.calc.modulo(4, 2), 0)
        self.assertEqual(self.calc.modulo(9,5), 4)
    
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()