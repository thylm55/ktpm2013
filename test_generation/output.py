import unittest

from input import main

class MainTest(unittest.TestCase):
    def test1(self):
        try:
            main(-4, -4, -3)
        except:
            self.fail("Raised an exception.")
    
    def test2(self):
        try:
            main(-1, -4, -3)
        except:
            self.fail("Raised an exception.")
    
    def test3(self):
        try:
            main(3, -4, -3)
        except:
            self.fail("Raised an exception.")
    
    def test4(self):
        try:
            main(-4, -1, -3)
        except:
            self.fail("Raised an exception.")
    
    def test5(self):
        try:
            main(-1, -1, -3)
        except:
            self.fail("Raised an exception.")
    
    def test6(self):
        try:
            main(3, -1, -3)
        except:
            self.fail("Raised an exception.")
    
    def test7(self):
        try:
            main(-4, 4, -3)
        except:
            self.fail("Raised an exception.")
    
    def test8(self):
        try:
            main(-1, 4, -3)
        except:
            self.fail("Raised an exception.")
    
    def test9(self):
        try:
            main(3, 4, -3)
        except:
            self.fail("Raised an exception.")
    
    def test10(self):
        try:
            main(-4, -4, -1)
        except:
            self.fail("Raised an exception.")
    
    def test11(self):
        try:
            main(-1, -4, -1)
        except:
            self.fail("Raised an exception.")
    
    def test12(self):
        try:
            main(3, -4, -1)
        except:
            self.fail("Raised an exception.")
    
    def test13(self):
        try:
            main(-4, -1, -1)
        except:
            self.fail("Raised an exception.")
    
    def test14(self):
        try:
            main(-1, -1, -1)
        except:
            self.fail("Raised an exception.")
    
    def test15(self):
        try:
            main(3, -1, -1)
        except:
            self.fail("Raised an exception.")
    
    def test16(self):
        try:
            main(-4, 4, -1)
        except:
            self.fail("Raised an exception.")
    
    def test17(self):
        try:
            main(-1, 4, -1)
        except:
            self.fail("Raised an exception.")
    
    def test18(self):
        try:
            main(3, 4, -1)
        except:
            self.fail("Raised an exception.")
    
    def test19(self):
        try:
            main(-4, -4, 4)
        except:
            self.fail("Raised an exception.")
    
    def test20(self):
        try:
            main(-1, -4, 4)
        except:
            self.fail("Raised an exception.")
    
    def test21(self):
        try:
            main(3, -4, 4)
        except:
            self.fail("Raised an exception.")
    
    def test22(self):
        try:
            main(-4, -1, 4)
        except:
            self.fail("Raised an exception.")
    
    def test23(self):
        try:
            main(-1, -1, 4)
        except:
            self.fail("Raised an exception.")
    
    def test24(self):
        try:
            main(3, -1, 4)
        except:
            self.fail("Raised an exception.")
    
    def test25(self):
        try:
            main(-4, 4, 4)
        except:
            self.fail("Raised an exception.")
    
    def test26(self):
        try:
            main(-1, 4, 4)
        except:
            self.fail("Raised an exception.")
    
    def test27(self):
        try:
            main(3, 4, 4)
        except:
            self.fail("Raised an exception.")
    
# run test
if __name__ == '__main__':
    unittest.main()