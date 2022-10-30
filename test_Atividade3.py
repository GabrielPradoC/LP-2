import unittest
from Atividade3 import return_lowest_number


class Atividade3Tests(unittest.TestCase):
    def test_should_return_correct_min_value(self):
        self.assertEqual(return_lowest_number([1, 2, 3]), 1)

    def test_should_return_valid_result_with_negative_numbers(self):
        self.assertEqual(return_lowest_number([-1, -2, -3]), -3)


if __name__ == '__main__':
    unittest.main()
