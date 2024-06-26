#!/usr/bin/env python3
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 8), 256)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(4, 0)


if __name__ == "__main__":
    unittest.main()
