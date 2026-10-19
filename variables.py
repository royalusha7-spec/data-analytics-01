Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=2
print(a)
2
b=5
print(b)
5
x=90
print(X)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
90
Z=50
print(Z)
50
print(z)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined. Did you mean: 'Z'?
9=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a9=20
print(a9)
20
9a=9
SyntaxError: invalid decimal literal
a0123456789=100
print(a0123456789)
100
name="pooja"
print(name)
pooja
print("name")
name
city="vij"
print(city)
vij
country="india")
SyntaxError: unmatched ')'
country="india"
print(country)
india
@=8
SyntaxError: invalid syntax
$=10
SyntaxError: invalid syntax
_=40
print(_)
40
_a=30
print(_a)
30
 a=60
 
SyntaxError: unexpected indent
if=30
SyntaxError: invalid syntax
else=90
SyntaxError: invalid syntax
int=80
print(int)
80
a=5,b=10
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;b=10
print(a+b)
15
a=3
b=6
print(a+b)
9
a,b=3,4
print(a+b)
7
a=2,3,4,5,6,7,8
print(a)
(2, 3, 4, 5, 6, 7, 8)
a,b,c=3,4,5,6,7,7,8,8
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a,b,c=3,4,5,6,7,7,8,8
ValueError: too many values to unpack (expected 3)
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
a=2 3 5 6 7 8 9
SyntaxError: invalid syntax
first name="pooja"
SyntaxError: invalid syntax
first_name="pooja"
print(first_name)
pooja
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname+""+lname)
poojach
print(fname+" "+lname)
pooja ch
print(fname,lname)
pooja ch
>>> NAME="pooja"
>>> print(NAME)
pooja
>>> Name="pooja"
>>> print(Name)
pooja
>>> name="pooja"
>>> print(name)
pooja
>>> a,b,c=100
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a,b,c=100
TypeError: cannot unpack non-iterable int object
>>> a=b=c=100
>>> print(a,b,c)
100 100 100
>>> fname=hari
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    fname=hari
NameError: name 'hari' is not defined
>>> midname=phani
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    midname=phani
NameError: name 'phani' is not defined
>>> fname="har"
>>> midname="phani"
>>> lname="sri"
>>> print(lname+midname+lname)
sriphanisri
>>> a=10000
>>> print(a)
10000
