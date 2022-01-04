Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
j = 'python programming'
print(j)
python programming
len(j)
18
# indexing = subscript operator
# []
print(j)
python programming
# index always starts from zero (0) to length of string = 1
j(0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    j(0)
TypeError: 'str' object is not callable
j[0]
'p'
# positive indexing

# negative indexing
j[-2]
'n'
j[-0]
'p'
j[-1]
'g'
msg = 'welcome to python programming class'
# slicing
# slicing always works from left to right
j[0:3]
'pyt'
j[3:7]
'hon '
# slicing [startpos:endpos, startpos is included, endpos is excluded
j[19]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    j[19]
IndexError: string index out of range
j[15:19]
'ing'
# doesnt show out of range
j[-3:5]
''
print(msg)
welcome to python programming class
msg[-5:-1]
'clas'
msg[-1]
's'
msg[-2:-1]
's'
msg[-5:]
'class'
folder = 'c\newfolder'
folder
'c\newfolder'
pront(folder)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    pront(folder)
NameError: name 'pront' is not defined. Did you mean: 'print'?
print(folder)
c
ewfolder
folder = r'c\newfolder'
print(folder)
c\newfolder
folder
'c\\newfolder'
# we use r = raw string
1+2
3
1*8
8
18\4
SyntaxError: unexpected character after line continuation character
18/4
4.5
18//4
4
