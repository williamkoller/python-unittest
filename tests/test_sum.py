import unittest
from src.main import Sum


class TestSum(unittest.TestCase):
    def test_return_sum_20_30(self):
        self.assertEqual(Sum.sum(20, 30), 50)

    def test_return_sum_10_40(self):
        self.assertEqual(Sum.sum(10, 40), 50)
