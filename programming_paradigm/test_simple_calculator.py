#Import the unittest module and the SimpleCalculator class from simple_calculator.py.
import unittest
from simple_calculator import SimpleCalculator
class SimpleCalc(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1,1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,5), 5)
        self.assertEqual(self.calc.subtract(-1,1), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10,5), 50)
        self.assertEqual(self.calc.multiply(-1,1), -1)
        self.assertEqual(self.calc.multiply(-1,-1), 1)

    def test_divide(self):
        try: 
            self.assertEqual(self.calc.divide(10,5), 2)
            self.assertEqual(self.calc.divide(-4,2), -2)
            self.assertEqual(self.calc.divide(-4,-2), 2)
        except ValueError:
            return "Error: Please enter numeric values only."
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
