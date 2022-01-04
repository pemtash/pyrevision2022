Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# lists
# ordered collection of items/elements
# syntax in []
languages = ['python', 'c', 'c++', 'java']
print(languages)
['python', 'c', 'c++', 'java']
type(languages)
<class 'list'>

# finding the length of the list
len(languages)
4

# access the elements of the list
# [] => subscript operator

languages[0]
'python'
languages[0][2]
't'

langugaes[-1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    langugaes[-1]
NameError: name 'langugaes' is not defined. Did you mean: 'languages'?
languages[-1]
'java'
languages[0][-2:]
'on'
languages [0:2]
['python', 'c']


# append
# add an element at the end of the list
languages.append('ruby')
print(languages)
['python', 'c', 'c++', 'java', 'ruby']
len(languages)
5

#insert
languages.insert(1, 'pascal')
languages
['python', 'pascal', 'c', 'c++', 'java', 'ruby']

# delete operation
languages.remove('java')
print(languages)
['python', 'pascal', 'c', 'c++', 'ruby']

langugages.pop(1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    langugages.pop(1)
NameError: name 'langugages' is not defined. Did you mean: 'languages'?
languages.pop(1)
'pascal'

languages
['python', 'c', 'c++', 'ruby']
'pascal'
'pascal'
# pop remove baso on index value

numlist = [100,200,300]
languages.append(numlist)
print(languages)
['python', 'c', 'c++', 'ruby', [100, 200, 300]]
len(languages)
5

anlist = [1,2,3,4]
languages.extend(anlist)
print(languages)
['python', 'c', 'c++', 'ruby', [100, 200, 300], 1, 2, 3, 4]
# extend add the elements by ekements

teams = ['rcb', 'csk']
languages.insert(2,teams)
print(languages)
['python', 'c', ['rcb', 'csk'], 'c++', 'ruby', [100, 200, 300], 1, 2, 3, 4]
s = 'welcome'
languages.append(s)
print(languages)
['python', 'c', ['rcb', 'csk'], 'c++', 'ruby', [100, 200, 300], 1, 2, 3, 4, 'welcome']
languages.extend(s)
print(languages)
['python', 'c', ['rcb', 'csk'], 'c++', 'ruby', [100, 200, 300], 1, 2, 3, 4, 'welcome', 'w', 'e', 'l', 'c', 'o', 'm', 'e']
len(languages)
18
languages[-1]
'e'

languages.count('e')
2
languages.pop(len(languages)-3)
'o'
languages.pop()
'e'
print(languages)
['python', 'c', ['rcb', 'csk'], 'c++', 'ruby', [100, 200, 300], 1, 2, 3, 4, 'welcome', 'w', 'e', 'l', 'c', 'm']

del lanfuages[1]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    del lanfuages[1]
NameError: name 'lanfuages' is not defined. Did you mean: 'languages'?
del languages[1]
languages
['python', ['rcb', 'csk'], 'c++', 'ruby', [100, 200, 300], 1, 2, 3, 4, 'welcome', 'w', 'e', 'l', 'c', 'm']

languages[-5:]
['w', 'e', 'l', 'c', 'm']
languages.clear()
languages
[]
print(languages)
[]
# it clears all the elements in languages

languages = ['golang', 'c#']
languages
['golang', 'c#']

# mutable vs immutables
# list are mutable, can be changed/modified
# strings are immutable, can't be changed

s
'welcome'
s[0] = 'w'
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s[0] = 'w'
TypeError: 'str' object does not support item assignment
































































