import re
import unittest
from input import main

# function to check if 2 input ranges is equivalence classes
def is_two_equivalence_classes(a1, a2, b1, b2):
    if (a2 < b2):
        if ((b2 - a1) <= a2 - a1 + b2 - b1):
            return False
    else:
        if ((a2 - b1) <= a2 - a1 + b2 - b1):
            return False
    return True

# function to check if 3 input ranges is equivalence classes
def is_equivalence_classes(a1="", a2="", b1="", b2="", c1="", c2=""):
    if ((a1 != "") & (a2 != "")
        & (b1 != "") & (b2 != "")
        & (c1 != "") & (c2 != "")):
        if is_two_equivalence_classes(a1, a2, b1, b2):
            if is_two_equivalence_classes(a1, a2, c1, c2):
                if is_two_equivalence_classes(b1, b2, c1, c2):
                    return True
        return False
    if ((a1 != "") & (a2 != "") & (b1 != "") & (b2 != "")):
        if is_two_equivalence_classes(a1, a2, b1, b2):
            return True
        return False

    if ((a1 != "") & (a2 != "")):
        return True

# return array of numbers exist in a line
def read_number_in_line(line):
    p = re.compile('[-+]?\d+')
    arrString = p.findall(line)
    arrNumber = []
    # convert string to int
    for i in arrString:
        arrNumber.append(int(i))
    return arrNumber

# check if line is validate or not
def validate_line(line):
    arrNumber = read_number_in_line(line)
        
    if (len(arrNumber) == 6):
        return is_equivalence_classes(arrNumber[0], arrNumber[1]
                                      , arrNumber[2], arrNumber[3]
                                      , arrNumber[4], arrNumber[5])

    if (len(arrNumber) == 4):
        return is_equivalence_classes(arrNumber[0], arrNumber[1]
                                      , arrNumber[2], arrNumber[3])

    if (len(arrNumber) == 2):
        return True

    if ((len(arrNumber) % 2 == 1) | (len(arrNumber) > 6)):
        return False
    
# validate docstring
def validate_docstring(docstring):
    print "Validating input..."
    validated = True
    lines = docstring.expandtabs().splitlines()
    for line in lines[1:]:
        if (validate_line(line) == False):
            validated = False

    if validated:
        print "OK."
        return True
    else:
        raise Exception, "wrong input"

# read docstring and return result array
def read_docstring(docstring):
    if validate_docstring(docstring):
        print "Reading input..."
        lines = docstring.expandtabs().splitlines()

        arrResult = []
        for line in lines[1:]:
            arrNumber = read_number_in_line(line)
            arr = []
            if arrNumber != []:
                for i in xrange(len(arrNumber)):
                    if i % 2 == 0:
                        averange = int((arrNumber[i]+arrNumber[i+1])/2)
                        arr.append(averange)
                arrResult.append(arr)
        print "OK."
        return arrResult

# return result after combinate two arrays
def combinate_two_array(arr1, arr2):
    row = len(arr1)

    fo = []

    for i in arr2:
        for j in xrange(row):
            k = []

            for ek in arr1[j]:
               k.append(ek)

            k.append(i)
            fo.append(k)
           
    return fo

# return result after combinate arrays
def combinate_arrays(arr):
    totalTests = 1
    for e in arr:
        totalTests = totalTests * len(e)
    print "Preparing variables for %d test cases..." % totalTests
    
    arrInit = []

    for i in arr[0]:
        k = []
        k.append(i)
        arrInit.append(k)

    if len(arr) == 1:
        print "OK."
        return arrInit
    else:
        if len(arr) == 2:
            print "OK."
            return combinate_two_array(arrInit, arr[1])
        else:
            arrStart = combinate_two_array(arrInit, arr[1])
            for i in range(2, len(arr)):
                arrStart = combinate_two_array(arrStart, arr[i])
            print "OK."
            return arrStart

# class to test main function
class MainTest(unittest.TestCase):
    pass

# function to generate test cases
def test_generator(params):
    paramsLen = len(params)
    def test(self):
        try:
            if (paramsLen == 0):
                main()
            if (paramsLen == 1):
                main(params[0])
            if (paramsLen == 2):
                main(params[0], params[1])
            if (paramsLen == 3):
                main(params[0], params[1]
                     , params[2])
            if (paramsLen == 4):
                main(params[0], params[1]
                     , params[2], params[3])
            if (paramsLen == 5):
                main(params[0], params[1]
                     , params[2], params[3]
                     , params[4])
            if (paramsLen == 6):
                main(params[0], params[1]
                     , params[2], params[3]
                     , params[4], params[5])
            if (paramsLen == 7):
                main(params[0], params[1]
                     , params[2], params[3]
                     , params[4], params[5]
                     , params[6])
            if (paramsLen == 8):
                main(params[0], params[1]
                     , params[2], params[3]
                     , params[4], params[5]
                     , params[6], params[7])
            if (paramsLen == 9):
                main(params[0], params[1]
                     , params[2], params[3]
                     , params[4], params[5]
                     , params[6], params[7]
                     , params[8])
            if (paramsLen == 10):
                main(params[0], params[1]
                     , params[2], params[3]
                     , params[4], params[5]
                     , params[6], params[7]
                     , params[8], params[9])
        except:
            self.fail("Raised an exception.")
    return test
    
# run test
if __name__ == '__main__':
    arrInput = read_docstring(main.__doc__)
    arrOutput = combinate_arrays(arrInput)

    print "Generating test cases..."
    i = 0
    for arrArgs in arrOutput:
        i = i + 1
        test_name = 'test_%d' % i
        test = test_generator(arrArgs)
        setattr(MainTest, test_name, test)
    print "OK."
    print "Running test..."
    unittest.main()
