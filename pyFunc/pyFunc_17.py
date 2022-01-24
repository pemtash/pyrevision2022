# Positional = only arguments (available only from Python 3.8)


def positionalArguments(a, b, /, z): # / indicates positional arguments not named argument
    print('a: {}, b: {}, z: {}'.format(a, b, z))


positionalArguments(1, 2, 3)
positionalArguments(1, 2, z = 3)
positionalArguments(a= 1, b=2, z=3)
