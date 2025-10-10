import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):
    def test_sqrt(self): self.assertEqual(calculator.sqrt(9), 3)
    def test_factorial(self): self.assertEqual(calculator.factorial(5), 120)
    def test_ln(self): self.assertAlmostEqual(calculator.ln(math.e), 1.0)
    def test_power(self): self.assertEqual(calculator.power(2, 3), 8)

if __name__ == "__main__":
    unittest.main()
