Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# SETS

# sets = unique collection of items, duplicate elements aren't allowed
# unordered
# {}

s = set{}
SyntaxError: invalid syntax
s = set()
s
set()
type(s)
<class 'set'>
a = set('bangalore')
a
{'g', 'o', 'l', 'a', 'e', 'n', 'b', 'r'}
len(a)
8
type(a)
<class 'set'>
b = set('singapore')
b
{'g', 'o', 'e', 'p', 'a', 'i', 'n', 's', 'r'}
c = {1,2,3,4}
c
{1, 2, 3, 4}
d = set(['rohit', 'bumrah', 'virat', 2,4,5])
d
{2, 4, 5, 'virat', 'bumrah', 'rohit'}
len(d)
6
'r' in a
True
2 in d
True
a[0]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable

# union
# a+b
a|b
{'g', 'o', 'i', 'p', 's', 'l', 'a', 'e', 'n', 'b', 'r'}
len(a|b)
11
a-b
{'b', 'l'}
b-a
{'s', 'i', 'p'}
a&b
{'g', 'o', 'a', 'e', 'n', 'r'}
a
{'g', 'o', 'l', 'a', 'e', 'n', 'b', 'r'}
a.add('new')
a
{'g', 'o', 'new', 'l', 'a', 'e', 'n', 'b', 'r'}
a+b
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a.update(b)
a
{'g', 'o', 'i', 'p', 'new', 's', 'l', 'a', 'e', 'n', 'b', 'r'}
b
{'g', 'o', 'e', 'p', 'a', 'i', 'n', 's', 'r'}
s
set()
a
{'g', 'o', 'i', 'p', 'new', 's', 'l', 'a', 'e', 'n', 'b', 'r'}
d
{2, 4, 5, 'virat', 'bumrah', 'rohit'}
d.update(a)
d
{2, 'g', 4, 5, 'o', 'p', 'e', 'b', 'virat', 'new', 'bumrah', 'rohit', 'l', 'a', 'i', 'n', 's', 'r'}


#RANGE

r = range(0,10)
r
range(0, 10)
type(r)
<class 'range'>
list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple(r)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# range and xrange
# py 2.7 , always used to create a list
# py3.x is actually xrange in python 2.7
r1 = range(3,10)
r1
range(3, 10)
type(r1)
<class 'range'>
list(r1)
[3, 4, 5, 6, 7, 8, 9]
set(r1)
{3, 4, 5, 6, 7, 8, 9}

r2 = range(5,51,10)
r2
range(5, 51, 10)
type(r2)
<class 'range'>
list(r2)
[5, 15, 25, 35, 45]

r3 = range(10,-6,-2)
list(r3)
[10, 8, 6, 4, 2, 0, -2, -4]
r2 = range(5,51,10)
# range = (start,stop, step)

range(3)[-1]
2
# range(3) - 0,1,2  [-1] - last element is 2
list(range(3))
[0, 1, 2]
list(range(11)[2:5])
[2, 3, 4]
