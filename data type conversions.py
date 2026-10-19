Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int()
int(9)
9
int(7.8)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(6+8j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float()
float(5.4)
5.4
float(5)
5.0
float(8.8)
8.8
float("hari")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hari")
ValueError: could not convert string to float: 'hari'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(false)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
float(False)
0.0
#str()
str("hari")
'hari'
str(8)
'8'
str(3.2)
'3.2'
str("phani")
'phani'
str(7+3j)
'(7+3j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex()
>>> complex(6+4j)
(6+4j)
>>> complex(1)
(1+0j)
>>> complex(7.3)
(7.3+0j)
>>> complex("sri")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex("sri")
ValueError: complex() arg is a malformed string
>>> complex(6+7+9j)
(13+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool()
>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(6.8)
True
>>> bool(6+1j)
True
>>> bool("chandu")
True
