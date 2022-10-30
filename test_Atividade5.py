import unittest
from Atividade5 import invert_string


class Atividade5Tests(unittest.TestCase):
    def test_should_invert_a_string(self):
        self.assertEqual(invert_string("abcde"), "edcba")

    def test_should_invert_string_and_keep_spaces(self):
        self.assertEqual(invert_string("a b c d e"), "e d c b a")

    def test_should_invert_string_and_keep_casing(self):
        self.assertEqual(invert_string("a B c D e"), "e D c B a")  # add assertion here


if __name__ == '__main__':
    unittest.main()
