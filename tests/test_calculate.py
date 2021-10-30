import unittest
from src.calculater import Calculate


class TestCalculate(unittest.TestCase):
    def test_return_calculate_sum(self):
        self.assertEqual(Calculate.sum(30, 30), 60)

    def test_return_calculate_division(self):
        result = Calculate.sum(30, 30)
        self.assertEqual(Calculate.division(result, 10), 6)
