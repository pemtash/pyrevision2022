def EmptyListAsParam(my_list=None):
    my_list = [] # its better to show empty list here
    my_list.append('$')
    return my_list


r = EmptyListAsParam()
print('returned output 1st iteration: ', r)


r1 = EmptyListAsParam()
print('returned output 2nd iteration: ', r1)


r2 = EmptyListAsParam()
print('returned output 2nd iteration: ', r2)