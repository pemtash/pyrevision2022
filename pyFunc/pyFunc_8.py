# INTERVIEW (VERY IMPORTANT)
# Function as a parameter

def mySquare(num):
    return num * num


# mySquare(10)

def myCube(n):
    return n * n * n

def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result


def WrapperFunction(funcAsParam, num):
    return funcAsParam(num)


result = WrapperFunction(mySquare, 5)
print('result:', result)

# Functions are also first class objects in python
# closures
# decorators

lstFunc = [mySquare, myCube, iterFactorial]

for item in lstFunc:
    print('result: ', item(5))