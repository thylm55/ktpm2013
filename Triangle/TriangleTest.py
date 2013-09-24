OUTPUT01 = 'equilateral triangle'
OUTPUT02 = 'isosceles right triangle'
OUTPUT03 = 'right triangle'
OUTPUT04 = 'isosceles triangle'
OUTPUT05 = 'triangle'
OUTPUT06 = 'not identified'
OUTPUT07 = 'error: invalid input'

import unittest
import math

from Triangle import getTriangleType

class TriangleTest(unittest.TestCase):


    # classification test cases

    # equilateral triangle
    def test01a(self):
        result = getTriangleType(3, 3, 3)
        self.assertEqual(result, OUTPUT01)
        
    def test01b(self):
        result = getTriangleType("3", 3, 3)
        self.assertEqual(result, OUTPUT01)

    def test01c(self):
        result = getTriangleType("3", "3", "3")
        self.assertEqual(result, OUTPUT01)

    # isosceles right triangle
    def test02a(self):
        result = getTriangleType(2, "2", math.sqrt(8))
        self.assertEqual(result, OUTPUT02)
        
    def test02b(self):
        result = getTriangleType(3, 3, math.sqrt(18))
        self.assertEqual(result, OUTPUT02)

    def test02c(self):
        result = getTriangleType(4, 4, math.sqrt(32))
        self.assertEqual(result, OUTPUT02)

    def test02d(self):
        result = getTriangleType(7, 7, math.sqrt(98))
        self.assertEqual(result, OUTPUT02)

    # right triangle
    def test03a(self):
        result = getTriangleType(3, 4, 5)
        self.assertEqual(result, OUTPUT03)

    def test03b(self):
        result = getTriangleType(6, 5, math.sqrt(61))
        self.assertEqual(result, OUTPUT03)

    # isosceles triangle
    def test04a(self):
        result = getTriangleType(7, 7, 5)
        self.assertEqual(result, OUTPUT04)

    def test04b(self):
        result = getTriangleType(2**132-1, 2**132-1, "1")
        self.assertEqual(result, OUTPUT04)

    # triangle
    def test05(self):
        result = getTriangleType(2, 3, 4)
        self.assertEqual(result, OUTPUT05)
        
    def test06(self):
        result = getTriangleType(1, 2, 3)
        self.assertEqual(result, OUTPUT06)

    # input test cases
    def test07a(self):
        result = getTriangleType(-2, 3, 4)
        self.assertEqual(result, OUTPUT07)

    def test07b(self):
        result = getTriangleType(2, -3, 4)
        self.assertEqual(result, OUTPUT07)

    def test07c(self):
        result = getTriangleType(2, 3, -4)
        self.assertEqual(result, OUTPUT07)

    def test08a(self):
        result = getTriangleType("a", 3, 4)
        self.assertEqual(result, OUTPUT07)

    def test08b(self):
        result = getTriangleType(2, "math.sqrt(2)", 4)
        self.assertEqual(result, OUTPUT07)

    def test08c(self):
        result = getTriangleType(2, 3, "2**32-1")
        self.assertEqual(result, OUTPUT07)

    def test09a(self):
        result = getTriangleType()
        self.assertEqual(result, OUTPUT07)

    def test09b(self):
        result = getTriangleType(2)
        self.assertEqual(result, OUTPUT07)

    def test09c(self):
        result = getTriangleType(2, 3)
        self.assertEqual(result, OUTPUT07)

# run test
if __name__ == '__main__':
    unittest.main()
