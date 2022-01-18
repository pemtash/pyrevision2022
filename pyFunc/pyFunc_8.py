# INTERVIEW (VERY IMPORTANT)
# Function as a parameter

def mySquare(num):
    return num * num


# mySquare(10)

# def myCube(n):
#    return n * n * n

def WrapperFunction(funcAsParam, num):
    return funcAsParam(num)


result = WrapperFunction(mySquare, 5)
print('result:', result)

# Functions are also first class objects in python