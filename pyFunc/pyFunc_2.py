# write a function to find maximum of two numbers

def findMaxMin(x , y):
    if x > y:
        return x
    else:
        return y
result = findMaxMin(3,5)
print(result)