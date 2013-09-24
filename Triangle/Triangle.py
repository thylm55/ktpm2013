MIN_VALUE = 2.2250738585072014e-308
MAX_VALUE = 1.7976931348623157e+308
EPSILONE = 1e-14

# convert input to number
def toNumber(arg):
    if isinstance(arg, str):
        try:
            return int(arg)
        except ValueError:
            try:
                return float(arg)
            except ValueError:
                return False
    else:
        return arg

# check if a number in valid range
def isValidRange(number):
    if (number > MIN_VALUE) & (number <= MAX_VALUE):
        return True
    else:
        return False

# validate input
def validateInput(arg):
    result = toNumber(arg)
    if (result != False) & (isValidRange(result) == True):
        return result
    else:
        return False

def validate3Inputs(arg1, arg2, arg3):
    result1 = validateInput(arg1);
    result2 = validateInput(arg2);
    result3 = validateInput(arg3);
    if (result1 != False) & (result2 != False) & (result3 != False):
        if (isinstance(arg1, str)):
            print "warning: input #1 should be a integer or float"
        if (isinstance(arg2, str)):
            print "warning: input #2 should be a integer or float"
        if (isinstance(arg3, str)):
            print "warning: input #3 should be a integer or float"
        return True
    else:
        return False

# case 5: normal triangle
def isATriangle(arg1, arg2, arg3):
    if (arg1 + arg2 - arg3 > EPSILONE) & (arg1 + arg3 - arg2 > EPSILONE) & (arg2 + arg3 - arg1 > EPSILONE):
        return True
    else:
        return False

# case 4: isosceles triangle
def isIsoscelesTriangle(arg1, arg2, arg3):
    if isATriangle(arg1, arg2, arg3):
        if (abs(arg1 - arg2) < EPSILONE) | (abs(arg2 - arg3) < EPSILONE) | (abs(arg3 - arg1) < EPSILONE):
            return True
        else:
            return False
    else:
        return False

# case 3: right triangle
def isRightTriangle(arg1, arg2, arg3):
    if isATriangle(arg1, arg2, arg3):
        if (arg1 * arg1 >= EPSILONE) & (arg2 * arg2 >= EPSILONE) & (arg3 * arg3 >= EPSILONE):
            if (abs(arg1 * arg1 + arg2 * arg2 - arg3 * arg3) < arg3*EPSILONE):
                return True
            if (abs(arg2 * arg2 + arg3 * arg3 - arg1 * arg1) < arg3*EPSILONE):
                return True
            if (abs(arg3 * arg3 + arg1 * arg1 - arg2 * arg2) < arg3*EPSILONE):
                return True
            return False
        else:
            return False
    else:
        return False

#case 2: isosceles right triangle
def isIsoscelesRightTriangle(arg1, arg2, arg3):
    if isATriangle(arg1, arg2, arg3):
        if (abs(arg1 * arg1 + arg2 * arg2 - arg3 * arg3) < arg3*EPSILONE) & (abs(arg1 - arg2) < EPSILONE):
            return True
        if (abs(arg2 * arg2 + arg3 * arg3 - arg1 * arg1) < arg1*EPSILONE) & (abs(arg2 - arg3) < EPSILONE):
            return True
        if (abs(arg3 * arg3 + arg1 * arg1 - arg2 * arg2) < arg2*EPSILONE) & (abs(arg3 - arg1) < EPSILONE):
            return True
        return False
    else:
        return False

# case 1: equilateral triangle
def isEquilateralTriangle(arg1, arg2, arg3):
    if isATriangle(arg1, arg2, arg3):
        if (abs(arg1 - arg2) < EPSILONE) & (abs(arg2 - arg3) < EPSILONE) & (abs(arg3 - arg1) < EPSILONE):
            return True
        else:
            return False
    else:
        return False
    
# CLASSIFY TRIANGLE
def getTriangleType(arg1="", arg2="", arg3=""):
    result1 = validateInput(arg1)
    result2 = validateInput(arg2)
    result3 = validateInput(arg3)

    result = validate3Inputs(arg1, arg2, arg3)
    
    if (result == True):
        if (isEquilateralTriangle(result1, result2, result3)):
            return 'equilateral triangle'
        else:
            if (isIsoscelesRightTriangle(result1, result2, result3)):
                return 'isosceles right triangle'
            else:
                if (isRightTriangle(result1, result2, result3)):
                    return 'right triangle'
                else:
                    if (isIsoscelesTriangle(result1, result2, result3)):
                        return 'isosceles triangle'
                    else:
                        if (isATriangle(result1, result2, result3)):
                            return 'triangle'
                        else:
                            return 'not identified'
    else:
        return 'error: invalid input'
