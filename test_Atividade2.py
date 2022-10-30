import unittest
from Atividade2 import check_triangle_sides


class Atividade2Tests(unittest.TestCase):
    def test_should_return_false_to_invalid_sides(self):
        self.assertFalse(check_triangle_sides(10, 20, 40))

    def test_should_return_true_to_valid_sides(self):
        self.assertTrue(check_triangle_sides(10, 20, 29))

    def test_should_return_true_if_all_sides_are_equal(self):
        self.assertTrue(check_triangle_sides(10, 10, 10))

    def test_should_return_true_if_two_sides_are_equal_and_valid(self):
        self.assertTrue(check_triangle_sides(10, 10, 15))


if __name__ == '__main__':
    unittest.main()
