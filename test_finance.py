import unittest
from finance import currency_convert, simple_interest

class TestFinance(unittest.TestCase):
    def test_currency(self):
        self.assertEqual(currency_convert(100, 4.2), 420.0)
    def test_interest(self):
        self.assertEqual(simple_interest(1000, 5, 3), 150.0)

if __name__ == "__main__":
    unittest.main()