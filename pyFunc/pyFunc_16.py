def multipleUnpacking(*args):
    print('Args: ', args)
    print('type of Args: ', type(args))


a = [1, 2, 3]
multipleUnpacking(*a)


b = (4, 5, 5)
multipleUnpacking(*b)


c = {1, 2, 3}
multipleUnpacking(*c)


r = range(100, 105)
multipleUnpacking(*r)


# print(*range(1,6), sep='')
print(*range(1,6), sep='\n')

# Python 3.5 ==> This feature is available only from python 3.5

