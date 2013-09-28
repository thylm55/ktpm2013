OUTPUT01 = 'equilateral triangle'
OUTPUT02 = 'isosceles right triangle'
OUTPUT03 = 'right triangle'
OUTPUT04 = 'isosceles triangle'
OUTPUT05 = 'triangle'
OUTPUT06 = 'not identified'

import unittest
import math

from triangle import detect_triangle

class TriangleTest(unittest.TestCase):
    # classification test cases

    # equilateral triangle
    def test01a(self):
        result = detect_triangle(3, 3, 3)
        self.assertEqual(result, OUTPUT01)
        
    def test01b(self):
        result = detect_triangle(2**32-1, 2**32-1, 2**32-1)
        self.assertEqual(result, OUTPUT01)

    def test01c(self):
        result = detect_triangle(1e-30, 1e-30, 1e-30)
        self.assertEqual(result, OUTPUT01)

    # isosceles right triangle
    def test02a(self):
        result = detect_triangle(2, 2, math.sqrt(8))
        self.assertEqual(result, OUTPUT02)
        
    def test02b(self):
        result = detect_triangle(3, 3, math.sqrt(18))
        self.assertEqual(result, OUTPUT02)

    def test02c(self):
        result = detect_triangle(4, 4, math.sqrt(32))
        self.assertEqual(result, OUTPUT02)

    def test02d(self):
        result = detect_triangle(7, 7, math.sqrt(98))
        self.assertEqual(result, OUTPUT02)

    # right triangle
    def test03a(self):
        result = detect_triangle(3, 4, 5)
        self.assertEqual(result, OUTPUT03)

    def test03b(self):
        result = detect_triangle(6, 5, math.sqrt(61))
        self.assertEqual(result, OUTPUT03)

    # isosceles triangle
    def test04a(self):
        result = detect_triangle(7, 7, 5)
        self.assertEqual(result, OUTPUT04)

    def test04b(self):
        result = detect_triangle(2**32-1, 2**32-1, 4)
        self.assertEqual(result, OUTPUT04)

    def test04c(self):
        result = detect_triangle(2**32-1, 2**32-1, 2**32-2)
        self.assertEqual(result, OUTPUT04)

    def test04d(self):
        result = detect_triangle(2**32-1, 4, 2**32-1)
        self.assertEqual(result, OUTPUT04)

    def test04d(self):
        result = detect_triangle(2**32-1, 4, 2**32-1)
        self.assertEqual(result, OUTPUT04)

    # triangle
    def test05a(self):
        result = detect_triangle(2, 3, 4)
        self.assertEqual(result, OUTPUT05)

    def test05b(self):
        result = detect_triangle(2**32-1, 2**32-2, 2**32-3)
        self.assertEqual(result, OUTPUT05)

    def test05c(self):
        result = detect_triangle(2**32-1, 2**32-2, 3)
        self.assertEqual(result, OUTPUT05) 

    def test06a(self):
        result = detect_triangle(1, 2, 3)
        self.assertEqual(result, OUTPUT06)

    # input test cases
    def test07a(self):
        result = detect_triangle(-2, 3, 4)
        self.assertEqual(result, OUTPUT06)

    def test07b(self):
        result = detect_triangle(2, -3, 4)
        self.assertEqual(result, OUTPUT06)

    def test07c(self):
        result = detect_triangle(2, 3, -4)
        self.assertEqual(result, OUTPUT06)

    def test08a(self):
        result = detect_triangle("a", 3, 4)
        self.assertEqual(result, OUTPUT06)

    def test08b(self):
        result = detect_triangle(2, "math.sqrt(2)", 4)
        self.assertEqual(result, OUTPUT06)

    def test08c(self):
        result = detect_triangle(2, 3, "2**32-1")
        self.assertEqual(result, OUTPUT06)

    def test09a(self):
        result = detect_triangle()
        self.assertEqual(result, OUTPUT06)

    def test09b(self):
        result = detect_triangle(2)
        self.assertEqual(result, OUTPUT06)

    def test09c(self):
        result = detect_triangle(2, 3)
        self.assertEqual(result, OUTPUT06)

    def test10a(self):
        result = detect_triangle(0, 0, 0)
        self.assertEqual(result, OUTPUT06)

    def test10b(self):
        result = detect_triangle(0, 3, 4)
        self.assertEqual(result, OUTPUT06)

    def test10c(self):
        result = detect_triangle(2, 0, 4)
        self.assertEqual(result, OUTPUT06)

    def test10d(self):
        result = detect_triangle(2, 3, 0)
        self.assertEqual(result, OUTPUT06)

# run test
if __name__ == '__main__':
    unittest.main()
