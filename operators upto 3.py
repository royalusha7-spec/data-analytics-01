Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic
>>> a=5
>>> b=8
>>> a+b
13
>>> print(a+b)
13
>>> print(a-b)
-3
>>> print(a*b)
40
>>> print(a//b)
0
>>> print(a/b)
0.625
>>> print(a**b)
390625
>>> print(a%b)
5
>>> #assignment operator
>>> a=4
>>> b=6
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+=b
>>> a
10
>>> b
6
>>> a-=4
>>> a
6
>>> a*2
12
>>> a//2
3
a/6
1.0
a**8
1679616
a%6
0
a=10
b=20
a+=b
b
20
a
30
b+=a
b
50
b-=5
b
45
b*2
90
b//5
9
b/3
15.0
b**10
34050628916015625
b**=10
b
34050628916015625
#comparison operator
a=5
b=15
a<b
True
b>a
True
a<=b
True
b>=a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a=20
b=40
a<b
True
b>a
True
a<=b
True
B>=a
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    B>=a
NameError: name 'B' is not defined. Did you mean: 'b'?
b>=a
True
a>b
False
b<a
False
a!=b
True
a==b
False
b!=a
True
b==a
False
