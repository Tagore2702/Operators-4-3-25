Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic
>>> a=4
>>> b=7
>>> a
4
>>> b
7
>>> print(a+b)
11
>>> print(b-a)
3
>>> print(a*b)
28
>>> print(a//b)
0
>>> print(a/b)
0.5714285714285714
>>> print(a**b)
16384
>>> print(a%b)
4
>>> #assignment
>>> c=3
>>> d=6
>>> c+=d
>>> c
9
>>> d+=c
>>> d
15
>>> c-=d
>>> c
-6
>>> d-=c
>>> d
21
>>> #comparision
>>> a<b
True
>>> b>a
True
b<a
False
a>b
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
#logical
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b!=a
True
a!=b or b>a
True
a==b or b==a
False
not True
False
not False
True
#identify
if type(a) is int:
    print("it is int")

    
it is int
if type(b) is float:
    print("it is int")

    
if type(a) is not float:
    print("it is int")

    
it is int
if type(b) is not int:
    print("it is not int")

    
#membership
    
z=2,3,4,5,6,7,8,9
if 3 in z:
    print(3)

    
3
if 10 in z:
    print(10)

    
if 10 not in z:
    print(10)

#Bitwise operators    
10
e=2
f=5
e&f
0
bin(e)
'0b10'
bin(5)
'0b101'
a=11
b=12
a&b
8
bin(a)
'0b1011'
bin(b)
'0b1100'
a|b
15
a=3
~a
-4
a^b
15
a=4
b=5
a^b
1
a=7
b=9
a^b
14
a=1
b=4
a^b
5

