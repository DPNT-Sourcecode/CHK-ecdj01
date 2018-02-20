import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAABBCD'), 210)

        self.assertEqual(checkout('AAAABBC'), 245)

        self.assertEqual(checkout('Z'), -1)

        self.assertEqual(checkout('CCC'), 60)

    def test_E_discount(self):
        self.assertEqual(checkout('AAABBBCDEE'), 290)
        self.assertEqual(checkout('AAABBCDEE'), 275)

if __name__ == '__main__':
    unittest.main()
