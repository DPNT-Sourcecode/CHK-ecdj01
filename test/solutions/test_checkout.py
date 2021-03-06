import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAABBCD'), 210)

        self.assertEqual(checkout('AAAABBC'), 245)

        self.assertEqual(checkout('&'), -1)

        self.assertEqual(checkout('CCC'), 60)

    def test_E_discount(self):
        self.assertEqual(checkout('AAABBBCDEE'), 290)
        self.assertEqual(checkout('AAABBCDEE'), 275)
        self.assertEqual(checkout('EEB'), 80)
        self.assertEqual(checkout('EEEB'), 120)
        self.assertEqual(checkout('EEEEBB'), 160)

    def test_A_new_discount(self):
        self.assertEqual(checkout('AAAA'), 180)
        self.assertEqual(checkout('AAAAA'), 200)
        self.assertEqual(checkout('AAAAAA'), 250)
        self.assertEqual(checkout('AAAAAAA'), 300)
        self.assertEqual(checkout('AAAAAAAA'), 330)
        self.assertEqual(checkout('AAAAAAAAA'), 380)
        self.assertEqual(checkout('AAAAAAAAAA'), 400)

    def test_F_discount(self):
        self.assertEqual(checkout('F'), 10)
        self.assertEqual(checkout('FF'), 20)
        self.assertEqual(checkout('FFF'), 20)
        self.assertEqual(checkout('FFFF'), 30)
        self.assertEqual(checkout('FFFFF'), 40)
        self.assertEqual(checkout('FFFFFF'), 40)


    def test_group_discount(self):
        self.assertEqual(checkout('ST'), 40)
        self.assertEqual(checkout('TY'), 40)
        self.assertEqual(checkout('ZZS'), 45)
        self.assertEqual(checkout('TTX'), 45)
        self.assertEqual(checkout('XXX'), 45)
        self.assertEqual(checkout('TXY'), 45)
        self.assertEqual(checkout('TXYS'), 62)
        self.assertEqual(checkout('ZSTY'), 65)
        self.assertEqual(checkout('ZZZY'), 65)
        self.assertEqual(checkout('ZXZZ'), 62)

if __name__ == '__main__':
    unittest.main()
