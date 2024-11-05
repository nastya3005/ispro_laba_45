import unittest

def volume(a, b, c):
    return a*b*c

class VolumeTestCase(unittest.TestCase):
    def test_a_zero(self):
        res = volume(0, 10, 5)
        self.assertEqual(res, 0)
    def test_cube(self):
        res = volume(6, 6, 6)
        self.assertEqual(res, 216)