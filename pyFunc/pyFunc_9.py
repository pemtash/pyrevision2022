# args

def SumOfNumbers(a, b):
    print('result: ', a+b)

SumOfNumbers(3,4)

def SumOfNumbers2(*args): # * it is notation to tell that its tuple in aggregation
    print('Args: ', args)
    print('type(args): ', type(args))
    result = 0
    for item in args:
        result += item
    print('result: ',result )

SumOfNumbers2(1, 2)
SumOfNumbers2(1, 2, 3, 4, 5)