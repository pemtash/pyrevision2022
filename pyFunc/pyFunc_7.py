# Lambda function
# Anonymous functions
# function which have got no names,
# they are used to write one-line functions
def mySquare(num):
    return num * num


print(mySquare(7))

f = lambda num: num * num
print(f)
print(type(f))
result = f(5)
print('square of number : ', result)


print('square of number', (lambda num: num*num)(10))
# lambda is a small function (writing a

f = lambda x, y : x if x > y else y
print("Max of 3,5:", f(3, 5))