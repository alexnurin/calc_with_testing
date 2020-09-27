import unittest
import random

from simple_calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(random.randint(1,100))

    def test_add(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_mul(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_accuracy(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(3).root(12).power(12, integer_power=True).value, calc_value + 3)

    def test_chain(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(7, -5, 0).divide(2, 1 / 2, 3).power(2).add(127).value,
                         ((calc_value + 2) / 3) ** 2 + 127)

    def test_float(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(6).divide(10, 2, 1 / 2).multiply(2.28).value, (calc_value**(1/6)) / 10 * 2.28)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
