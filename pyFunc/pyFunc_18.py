# positional + keyword - only arguments (available only from python 3.8)


def postionalKeywordArguments(a, b, /, z, w, *, x, y):
    print('a: {}, b: {}, z: {}, w: {}, x: {}, y:{}'.format(a, b, z, w, x, y))


postionalKeywordArguments(1, 2, 3, 4, x=5, y=6)
postionalKeywordArguments(1, 2, z=9, w=21, x=5, y=6

