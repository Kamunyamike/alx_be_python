import unittest

num1 = int(input("Enter your number to square: "))
def square(num1):
    area =  num1 ** 2
    return area

class TestCalc(unittest.TestCase):
    def test_square_positive(self):
        result = square(10)
        self.assertEqual(result, 100)
    def test_square_negative(self):
        result = square(-12)
        self.assertEqual(result, 144)
    def test_square_zero(self):
        result = square(0)
        self.assertEqual(result, 0)
    def test_square_float(self):
        result = square(2.5)
        self.assertEqual(result, 6.25)
if __name__ == "__main__":
    unittest.main()