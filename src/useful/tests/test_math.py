import unittest

import useful

class MathTest(unittest.TestCase):

    def test_add(self):
        self.assertEquals(useful.add1(5), 6)

    def test_mult(self):
        self.assertEquals(useful.mult2(3), 6)
