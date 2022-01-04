Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# TUPLES
# ordered collection of items/ elements
# immutable
# syntax ()

players = ('rohit','virat','rahane')
players
('rohit', 'virat', 'rahane')
print(players)
('rohit', 'virat', 'rahane')
type(players)
<class 'tuple'>
len(players)
3
players(0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    players(0)
TypeError: 'tuple' object is not callable
# to access we need to use []
players[0]
'rohit'
players[-1]
'rahane'
players[:2]
('rohit', 'virat')

players.count('virat')
1
players.index('virat')
1
t=(100,[1,2,3],'March',2022)
len(t)
4
t[1]
[1, 2, 3]
t[1].append(4)
t
(100, [1, 2, 3, 4], 'March', 2022)
# here we can append in tuple where its consisting of list

t[0].append(200)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t[0].append(200)
AttributeError: 'int' object has no attribute 'append'
t2 = (2,4,6,8,1,3)
t2
(2, 4, 6, 8, 1, 3)
type(t2)
<class 'tuple'>


## SHALLOW COPY
#list , [:], copy
team_a = ['Dhawan', 'rahane', 'ashwon']
team_b = team_a
team_b
['Dhawan', 'rahane', 'ashwon']
team_a.append('axar')
team_a
['Dhawan', 'rahane', 'ashwon', 'axar']
team_b
['Dhawan', 'rahane', 'ashwon', 'axar']
team_b.append('choenyi')
team_b
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi']
team_a
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi']


team_c = team_a[:]
team_c
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi']
team_a
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi']
team_b
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi']
team_a.append('tenzin')
team_a
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi', 'tenzin']
team_c
['Dhawan', 'rahane', 'ashwon', 'axar', 'choenyi']
id(team_c)
2177803506816
id(team_a)
2177836106624
id(team_b)
2177836106624
# here id of team_a = team_b != team_c


======================= RESTART: Shell ======================
# shallow copy

team_a
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    team_a
NameError: name 'team_a' is not defined
team_a = ['Dhawan', 'rahane', 'ashwon']
team_a
['Dhawan', 'rahane', 'ashwon']
team_d = list(team_a)
team_d
['Dhawan', 'rahane', 'ashwon']
team_a.append('pema')
team_a
['Dhawan', 'rahane', 'ashwon', 'pema']
team_d
['Dhawan', 'rahane', 'ashwon']
team_c = team_a.copy()
team_c
['Dhawan', 'rahane', 'ashwon', 'pema']

team_a.append('tashi')
team_a
['Dhawan', 'rahane', 'ashwon', 'pema', 'tashi']
team_c
['Dhawan', 'rahane', 'ashwon', 'pema']
len(team_c)
4
lst = [1,2,3,4,5,6,7,8,9]
len(lst)
9
lst[9]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    lst[9]
IndexError: list index out of range
lst[8]
9
lst.append(100)
lst
[1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
lst.append([12,34,56])
lst
[1, 2, 3, 4, 5, 6, 7, 8, 9, 100, [12, 34, 56]]
lst.append('pema')
lst
[1, 2, 3, 4, 5, 6, 7, 8, 9, 100, [12, 34, 56], 'pema']
len9lst)
SyntaxError: unmatched ')'
len(lst)
12
lst[9]= 7
lst
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema']
lst_copy = lst.copy()
lst_copy
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema']
lst.append(20,000)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    lst.append(20,000)
TypeError: list.append() takes exactly one argument (2 given)
lst.append(20000)
lst
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema', 20000]
lst_copy
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema']
lst.insert(2,1000)
lst
[1, 2, 1000, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema', 20000]
lst_copy
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema']
lst.pop()
20000
lst
[1, 2, 1000, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema']
lst.remove(2,7)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    lst.remove(2,7)
TypeError: list.remove() takes exactly one argument (2 given)

lst.remove(2)
lst
[1, 1000, 3, 4, 5, 6, 7, 8, 9, 7, [12, 34, 56], 'pema']
lst.remove(7)
lst
[1, 1000, 3, 4, 5, 6, 8, 9, 7, [12, 34, 56], 'pema']
lst.remove(9)
lst
[1, 1000, 3, 4, 5, 6, 8, 7, [12, 34, 56], 'pema']
team_a
['Dhawan', 'rahane', 'ashwon', 'pema', 'tashi']
team_a.append(lst)
team_a
['Dhawan', 'rahane', 'ashwon', 'pema', 'tashi', [1, 1000, 3, 4, 5, 6, 8, 7, [12, 34, 56], 'pema']]
len(team_a)
6
team_b
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    team_b
NameError: name 'team_b' is not defined. Did you mean: 'team_a'?
team_c
['Dhawan', 'rahane', 'ashwon', 'pema']
team_c.extend(lst)
team_c
['Dhawan', 'rahane', 'ashwon', 'pema', 1, 1000, 3, 4, 5, 6, 8, 7, [12, 34, 56], 'pema']
len(team_c)
14
