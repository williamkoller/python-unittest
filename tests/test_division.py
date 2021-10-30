import unittest

from src.division import Division


class TestDivision(unittest.TestCase):
    def test_return_division_10_5(self):
        self.assertEqual(Division.division(25, 5), 5)
