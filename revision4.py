Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
## DICTIONARY
## collection of key value pairs
## syntax {}

# {k1: v1, k2:v2, k3:v3, k4:v4, ,,,}
fruits = {'a':'apple', 'b':'bannana', 'c':'cherry'}
print(fruits)
{'a': 'apple', 'b': 'bannana', 'c': 'cherry'}
len(fruits)
3
type(fruits)
<class 'dict'>

## in dict , elements are access by key rather than index
fruits['a']
'apple'
fruits[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fruits[0]
KeyError: 0
fruits(0)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fruits(0)
TypeError: 'dict' object is not callable

# add elements to the dictionary
fruits = {'d':'dragon fruit'}
fruits
{'d': 'dragon fruit'}
fruits = {'a':'apple', 'b':'bannana', 'c':'cherry'}
fruits
{'a': 'apple', 'b': 'bannana', 'c': 'cherry'}
fruits['d'] = 'dragon fruit'
fruits
{'a': 'apple', 'b': 'bannana', 'c': 'cherry', 'd': 'dragon fruit'}

fruits.pop()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fruits.pop()
TypeError: pop expected at least 1 argument, got 0
fruits.pop('d')
'dragon fruit'
fruits
{'a': 'apple', 'b': 'bannana', 'c': 'cherry'}

ipl = {}
len(ipl)
0
ipl['mi'] = ['rohit','surya']
ipl
{'mi': ['rohit', 'surya']}

ipl['rcb'] = ['virat','abd']
ipl
{'mi': ['rohit', 'surya'], 'rcb': ['virat', 'abd']}
ipl['mi]
    
SyntaxError: unterminated string literal (detected at line 1)
ipl['mi']
    
['rohit', 'surya']
ipl['mi'].append('bumrah')
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah'], 'rcb': ['virat', 'abd']}
ipl['mumbai'] = ipl['mi']
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah'], 'rcb': ['virat', 'abd'], 'mumbai': ['rohit', 'surya', 'bumrah']}
ipl['mi'].append('hardik')
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik']}
ipl['bangalore']
    
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ipl['bangalore']
KeyError: 'bangalore'
ipl['bangalore'] = ['virat', 'abd']
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik'], 'bangalore': ['virat', 'abd']}
ipl['rcb'].append('yuzi')
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd', 'yuzi'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik'], 'bangalore': ['virat', 'abd']}

# IN operator
    
'mi' in ipl
    
True
 'MI' in ipl
    
SyntaxError: unexpected indent
'MI' in ipl
    
False

ipl.get('mi')
    
['rohit', 'surya', 'bumrah', 'hardik']
ipl.get('csk')
    
print(result)
    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined
ipl['csk']
    
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ipl['csk']
KeyError: 'csk'
result = ipl.get('csk', -1)
    
result
    
-1
ipl.items()
    
dict_items([('mi', ['rohit', 'surya', 'bumrah', 'hardik']), ('rcb', ['virat', 'abd', 'yuzi']), ('mumbai', ['rohit', 'surya', 'bumrah', 'hardik']), ('bangalore', ['virat', 'abd'])])
ipl.keys()
    
dict_keys(['mi', 'rcb', 'mumbai', 'bangalore'])
fruits
    
{'a': 'apple', 'b': 'bannana', 'c': 'cherry'}
fruits.items()
    
dict_items([('a', 'apple'), ('b', 'bannana'), ('c', 'cherry')])
fruits.items()[0]
    
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    fruits.items()[0]
TypeError: 'dict_items' object is not subscriptable
list(fruits.items()[0])
    
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(fruits.items()[0])
TypeError: 'dict_items' object is not subscriptable
list(fruits.items())[0]
    
('a', 'apple')
# pop
    
fruits.pop('csk')
    
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    fruits.pop('csk')
KeyError: 'csk'
fruits.pop('d')
    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    fruits.pop('d')
KeyError: 'd'
fruits
    
{'a': 'apple', 'b': 'bannana', 'c': 'cherry'}

# popitem
    
fruits.popitem()
    
('c', 'cherry')
fruits
    
{'a': 'apple', 'b': 'bannana'}
# last item got removed
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd', 'yuzi'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik'], 'bangalore': ['virat', 'abd']}
ipl['rcb'].remove('yuzi')
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik'], 'bangalore': ['virat', 'abd']}
ipl['csk'] = 'dhoni'
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik'], 'bangalore': ['virat', 'abd'], 'csk': 'dhoni'}
del ipl['csk']
    
ipl
    
{'mi': ['rohit', 'surya', 'bumrah', 'hardik'], 'rcb': ['virat', 'abd'], 'mumbai': ['rohit', 'surya', 'bumrah', 'hardik'], 'bangalore': ['virat', 'abd']}

alphabets = ['a':100, 'b':200]
    
SyntaxError: invalid syntax
alphabets = {'a':100, 'b':200}
    
alphabets
    
{'a': 100, 'b': 200}
fruits
    
{'a': 'apple', 'b': 'bannana'}
fruits.update(alphabets)
    
fruits
    
{'a': 100, 'b': 200}
