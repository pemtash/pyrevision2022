def namedArgumentFunction(a, b, c):
    print("the values are a: {}, b: {}, c: {}".format(a,b,c))


namedArgumentFunction(100, 200, 300) # positional arguments
namedArgumentFunction(c=3, a=1, b=2) # named arguments
#namedArgumentFunction(181, a=102, b=103) # mix of position + name error
namedArgumentFunction(101, b=102, c=103) # mix of position + no error