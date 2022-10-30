import unittest
from Atividade1 import process_days


class Atividade1Tests(unittest.TestCase):
    def test_should_correctly_display_days(self):
        result = process_days(10)
        self.assertEqual(result["days"], 10)
        self.assertEqual(result["years"], 0)
        self.assertEqual(result["months"], 0)

    def test_should_correctly_display_months(self):
        result = process_days(30)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["years"], 0)
        self.assertEqual(result["months"], 1)

    def test_should_correctly_display_years(self):
        result = process_days(365)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["years"], 1)
        self.assertEqual(result["months"], 0)

    def test_should_correctly_display_months_with_days(self):
        result = process_days(37)
        self.assertEqual(result["days"], 7)
        self.assertEqual(result["years"], 0)
        self.assertEqual(result["months"], 1)

    def test_should_correctly_display_years_with_months(self):
        result = process_days(395)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["years"], 1)
        self.assertEqual(result["months"], 1)

    def test_should_correctly_display_years_with_days(self):
        result = process_days(370)
        self.assertEqual(result["days"], 5)
        self.assertEqual(result["years"], 1)
        self.assertEqual(result["months"], 0)

    def test_should_correctly_display_full_date(self):
        result = process_days(397)
        self.assertEqual(result["days"], 2)
        self.assertEqual(result["years"], 1)
        self.assertEqual(result["months"], 1)

    def test_should_handle_invalid_input_types(self):
        result = process_days("abcde")
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["years"], 0)
        self.assertEqual(result["months"], 0)


if __name__ == '__main__':
    unittest.main()
