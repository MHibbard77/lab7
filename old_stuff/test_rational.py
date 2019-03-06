from unittest import TestCase
from rational import Rational


class TestRational(TestCase):

    def test___init__(self):
        # testing 0
        self.rat1 = Rational(0,1)
        self.assertEqual(self.rat1.n, 0)
        self.assertEqual(self.rat1.d, 1)

        # testing 1
        self.rat1 = Rational(1, 1)
        self.assertEqual(self.rat1.n, 1)
        self.assertEqual(self.rat1.d, 1)

        # testing -1
        self.rat1 = Rational(-1, 1)
        self.assertEqual(self.rat1.n, -1)
        self.assertEqual(self.rat1.d, 1)

        # testing 1 million
        self.rat1 = Rational(1000000, 1)
        self.assertEqual(self.rat1.n, 1000000)
        self.assertEqual(self.rat1.d, 1)

        # testing 1 millionth
        self.rat1 = Rational(1, 10000000)
        self.assertEqual(self.rat1.n, 1)
        self.assertEqual(self.rat1.d, 10000000)

        # testing -1 million
        self.rat1 = Rational(-1000000, 1)
        self.assertEqual(self.rat1.n, 1)
        self.assertEqual(self.rat1.d, 1)

        # testing -1 millionth
        self.rat1 = Rational(-1, 1000000)
        self.assertEqual(self.rat1.n, 1)
        self.assertEqual(self.rat1.d, 1)

        # testing 0 denom
        with self.assertRaises(ZeroDivisionError):
            self.rat1 = Rational(1,0)

        # test type error
        with self.assertRaises(TypeError):
            self.rat1 = Rational('bork', 'blork')

    def test___add__(self):
        # zero
        self.rat1 = Rational(0, 1)
        # one
        self.rat2 = Rational(1, 1)
        # neg one
        self.rat3 = Rational(-1, 1)
        # one million
        self.rat4 = Rational(1000000, 1)
        # one millionth
        self.rat5 = Rational(1, 10000000)
        # neg one million
        self.rat6 = Rational(-1000000, 1)
        # neg one millionth
        self.rat7 = Rational(-1, 1000000)

        # 0 + 1
        self.assertEqual(self.rat1.__add__(self.rat2), Rational(1,1))

        # 0 + -1
        self.assertEqual(self.rat1.__add__(self.rat3), Rational(-1, 1))

        # 0 + 1000000
        self.assertEqual(self.rat1.__add__(self.rat4), Rational(1000000, 1))

        # 0 + 1/1000000
        self.assertEqual(self.rat1.__add__(self.rat5), Rational(1, 1000000))

        # 0 + -1000000
        self.assertEqual(self.rat1.__add__(self.rat6), Rational(-1000000, 1))

        # 0 + - 1/1000000
        self.assertEqual(self.rat1.__add__(self.rat7), Rational(-1, 1000000))

        # add string
        with self.assertRaises(TypeError):
            self.rat1.__add__('bork')

    def test___sub__(self):
        self.rat0 = Rational(0, 1)
        self.rat1 = Rational(2, 1)
        self.rat2 = Rational(1, 2)
        self.rat3 = Rational(1, 3)
        self.rat4 = Rational(100000, 1)
        self.rat5 = Rational(50000, 1)

        self.assertEqual(self.rat1.__sub__(self.rat2), Rational(3, 2))
        self.assertEqual(self.rat2.__sub__(self.rat2), Rational(0, 1))
        self.assertEqual(self.rat2.__sub__(self.rat3), Rational(1, 6))
        self.assertEqual(self.rat1.__sub__(self.rat0), Rational(2, 1))
        self.assertEqual(self.rat3.__sub__(self.rat2), Rational(-1, 6))
        self.assertEqual(self.rat2.__sub__(self.rat1), Rational(-3, 2))
        self.assertEqual(self.rat4.__sub__(self.rat5), Rational(50000, 1))

    def test___div__(self):
        self.rat1 = Rational(1, 1)
        self.rat2 = Rational(2, 1)
        self.rat3 = Rational(1, 2)
        self.rat4 = Rational(-2, 1)
        self.rat5 = Rational(-1, 2)

        self.assertEqual(self.rat1.__div__(self.rat2), Rational(1,2))
        self.assertEqual(self.rat2.__div__(self.rat3), Rational(4,1))
        self.assertEqual(self.rat3.__div__(self.rat2), Rational(1,4))
        self.assertEqual(self.rat4.__div__(self.rat2), Rational(-1,1))
        self.assertEqual(self.rat5.__div__(self.rat4), Rational(1,4))

    def test___str__(self):
        self.rat1 = Rational(1, 1)
        self.rat2 = Rational(2, 1)
        self.rat3 = Rational(1, 2)
        self.rat4 = Rational(-2, 1)
        self.rat5 = Rational(-1, 2)

        self.assertEqual(self.rat1.__str__(), "1")
        self.assertEqual(self.rat2.__str__(), "2")
        self.assertEqual(self.rat3.__str__(), "1/2")
        self.assertEqual(self.rat4.__str__(), "-2")
        self.assertEqual(self.rat5.__str__(), "-1/2")

    def test___float__(self):
        self.ratFloat = Rational()
        self.ratFloat1 = Rational(1, 100000)
        self.ratFloat2 = Rational(10000, 10)
        self.ratFloat3 = Rational(2341, 3980)

        self.assertType(self.ratFloat.__float__(), float)
        self.assertType(self.ratFloat1.__float__(), float)
        self.assertType(self.ratFloat2.__float__(), float)
        self.assertType(self.ratFloat3.__float__(), float)
