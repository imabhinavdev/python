# By Dr. Rahul Dubey (HOD- CSE | SISTec)
# Assistant Prof: Amit Swami Sir 
# Notes - Abhinav Singh
## Table of Contents

1. [Variables](#variables)
2. [Data Types](#data-types)
3. [Operatos](#operators)
4. [Input and Output](#input-and-output)
5. [Flow Control](#flow-control)

# Variables
1. Only alphabets and digits
2. only one special symbol ' _ '
3. identifiers are case sensitive
4. keywords not allowed
5. no limit


# Data Types
## Fundamental Datatypes
int, float, complex, bool, str
## Advanced Datatype
tuples, list, dictionary, set, frozen, range, None

## Notes
[Anaconda Download](https://www.anaconda.com/download)
> **id** is a funtion which returns address of the variable and **type** is a function which return the type of variable

>**typeconvert** and **typecoersion** are the same thing.

> In python, everything is object!
```
x=5 
print(type(x))
 ```

> Reusability concept is used in Python.
```
x=5
y=5
print(id(x))
print(id(y))
```

> Python also uses immutability after 2^8
```
x=257
y=257
print(id(x))
print(id(y))
```

### Datatypes of binary, octa and hexa: 
```
x=0b101
y=0o753
z=0xA123
print(x,y,z)
print(bin(x),oct(y),hex(z))
```

You can use various format of integer in real part of complex numbers
```
x=0b101+2.5j
print(x)
```

### Bool DataType
```
x=True
y=False
print(x+y)
```
In python *true* is **1** and *false* is **0** so performing arithmetic function on bool will convert it in number.

---
### String
> Note: There is no word like **character** in python.

```
x='R'
print(x)
```
Python don't have anything like pointer but everything works on pointer only!

```
x='Rahul;
for i in x:
    print(id(i))

#Console:
# Prints many address.    
```
---
### Type Casting or Type Coersion

```
x=3.5
y=int(x)
print(y)
```

```
x="10.5"
y=int(x)
print(y)

#Console:
# Literal Error/ Value Error Here
```
```
x="10"
y=int(x)
print(y)

#Console:
# No Literal Error/ Value Error Here
```

>In python if there is **0** only, boolean will return ***false*** otherwise ***true*** for everything !
```
x=.25   #True
y=""    #False
z=-1    #True
a=" "   #True
```
---
### Concept of Immutability

```
x=5
print(id(x))
x=10
print(id(x))
```

``All the fundamental datatypes support immutability``

---
### Range

Range is a class in python and it's constructor is used to make range between two numbers. It is an advanced datatype!

```
x=range(1,10)
print(type(x))
print(list(x))

#Console:
#<class 'range'>
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```
x=None
print(type(x))

#Console:
#<class 'NoneType'>
```

```
x=None
x=5
print(x)

#Console:
#5
```
## Advanced DataTypes

### List
* List is container type of data type which contain **homo** or **non homogenious** data.
* It preserves the order of insertion and
* It support indexing
* It supports slicing
* It has a  growing nature means it is mutable.
```
l=[]
print(type(l))

#Console:
#class <list>
```

```
list1=[1,2,3,4,[5,6,7,['a','b']],{'name':'abhinav'}]
print((list1))

#Console:
#[1, 2, 3, 4, [5, 6, 7, ['a', 'b']], {'name': 'abhinav'}]
```

> In Python, indexing always starts with **0**.

```
list1=[1,2,3,4,[5,6,7,['a','b','c']],{'name':'abhinav'}]

print(list1[4][3][2])

#Console
#c
```
---
### Tuple
* It is a immutable list.
```
l=[1,2,3,4]
l.append(5)
print(l)

# [1, 2, 3, 4, 5]

t=(1,2,3,4)
t.append(5)
print(t)

# Cannot append Error Attribute Error
```
``If a tupple has only one integer, it should be separated be commma , ``
```
l=[]
print(type(l))  # <class 'list'>
t=()
print(type(t))  # <class 'tuple'>
t=(1)
print(type(t))  # <class 'int'>
t=(1,)
print(type(t))  # <class 'tuple'>
```

``Mutability is changing of data on the same address as previous``
>Tuple is mutable using new memory address
```
t=(1,2,3,4)
t1=(5,6)
print(id(t))
t=t+t1
print(t)
print(id(t))

# 2625484955360
# (1, 2, 3, 4, 5, 6)
# 2625482882688
```
---
### Dictionary & Set
* Key value pair
* Mutuable datatype
```
dict={'key':'value'}
```

```
dict={'key':'value'}
d={}
print(type(d))

q=set()
print(type(q))
q={1,2,3,4,5}

#<class 'dict'>
#<class 'set'> 
```
```
d={'1':'Abhinav Singh'}
a={(1,2,3,4):'Abhinav'}
print(a)
```

```
d={'1':'Abhinav Singh'}
a={(1,2,3,4):'Abhinav'}
print(a.keys())
print(a.values())
print(a.items())
```

```
d={'data':[1,2,3,4],'name':'Abhinav','age':20}
for keys,value in d.items():
    print(keys,value)

#data [1, 2, 3, 4]
#name Abhinav
#age 20
```

# Day-2

# Operators
1. Arithmetic
2. Relational or Comparision
3. Logical
4. Bitwise
5. Assignment
6. Special Operator

### Arithmetic
1. Addition (+)
2. Subtraction(-)
3. Division(/)
4. Multiplication(*)
5. Modulus(%)
6. #### Floor Division Operator
```
a=5
b=2
c=a//b
print(c)
```
If any number is *float* and we are doing floor division then the result is also a *float* number
```
a=5.0
b=2
c=a//b
print(c)
```
7. #### Power Operator/ Exponential operator
```
a=3
b=a**2
print(b)
```


---
### Relational Operator
1. Greater Than
2. Less Than
3. Equal
4. Greater equal to
5. Less equal to

>Only equal to operator does not take care of datatype, otherwise there will be a ***TypeError***
```
print(10>"abhi")

#TypeError
```
---
### Logical Operators
1. and
2. or
3. not

#### AND
If we are working with integer, first part is ***false*** or ***0*** means it is evaluated as ***false*** the output is the ***right*** part 
#### OR
If we are working with integer, first part is ***true*** or ***1*** means it is evaluated as ***true*** the output is the ***left*** part 

>x and y <br>
>If x is evaluated as ***false*** return x, otherwise return >y as the answer.

>x or y<br>
>If x is evaluted as ***True***, return x as the answer

``The python virtual machine always returns a string in single quotes '' ``

>**Zero Division Error** : when anything is divided by 0.
---
### Bitwise Operator
&, /, >>, <<

### Assignment operator
1. Normal Assignment
```
x=10
```
2. Compound Assignment
```
x+=10
```
``In  python, there is no ternary operator !``

### Special Operators
1. **Identity operators** (is and is not). Mainly for address com.
```
a=10
b=10
print(a is b)
print(a is not b)
```
2. **Membership** (in and not in to check membership)
```
s="abhinav"
print('b' in s)
```
```
d={1:'abhinav',2:"singh"}
print(2 in d)
print("abhinav" in d.values())
```
### Operator Precedence Image
![Precedence](image.png)

# Input and Output
### Input
```
x=input("Enter data: ")
print(x)
```

Multiple Input in python can be done using ***split*** method.

`` Split function returns the list of character``

```
x=input("Enter data: ")
l=x.split(',')
print(type(l))
sum=0 
for i in l:
    sum+=int(i)
print(sum)
```
#### List Comprehension
```
x=[int(i) for i in input("Enter data: ").split(',')]
```
---
### Command Line Arguments
sys is built-in module in python which contain a variable that is argv
```
print(type(argv))
```

#### Unpacking
```
a,b=input("Enter data").split(',')
```

### Separator attribute
```

print("abhinav","Singh",sep=",")

print("Abhinav",end=' ')
print("Singh")
```

### Print Formatted String
```
a,b,c,d=10,11.5,"Abhinav",{1:"Singh"}
print("It is an integer %i or %d"%(a,a))
print("It is an float %f"%(b))
print("It is an string %s"%(c))
print("It is an string %s"%(d))
```

### Format Method (f-string)
```
a="Abhinav"
b="Singh"
print("{0} and {1}".format(a,b))
print(f"{a} and {b}")
```
# Day-3
# **Flow Control**
![Flow Control](image-1.png)
>The Flow of a program is always sequential
---
### Conditional Statements
1. if
2. if-elif
3. if-elif-else
```
a=input("enter designation: ")
if a=="engineer":
    print("Hello Boss !")
    
elif a=="friend":
    print("Mera Bhai hai tu")
else:
    print("Good Morning")
```

`` There is no pre-increment and post-increment``

---
### Iterative Statements
#### 1. FOR
```
l=[1,2,3,4,5]
sum=0
for _ in l:
    print(_)
for _ in range(len(l)):
    sum+=l[_]
print("Sum is :",sum)
```
#### 2. WHILE 
```
inp=int(input("Enter any number: "))
i=0
while i<inp:
    print("The value of i",i)
    i+=1
```
---
### Transfer Statements
#### 1. Break
```
for i in range(10):
    if i==5:
        print("Reached 5")
        break
    print(i)
```
#### 2. Continue
```
for i in range(10):
    if i==5:
        print("Reached 5")
        continue
    print(i)
```

#### 3. Pass
```
for i in range(10):
    pass
```

#### For Else
```
cart=[10,20,30,40,100]
for item in cart:
    if item>400:
        print("we cannot process your order")
        break
else:
    print("all orders will be delivered!")
```
#### While Else
```
cart=[10,20,30,40,100]
i=0
while i<len(cart):
    if cart[i]>40:
        print("Your order can not be processed!")
        break
    i+=1
else:
    print("Order will be delivered !")
```

## String
String is immutable<br>
String supports indexing<br>
String support slicing


```
s1="abhinav"
s2="Singh"
print(s1+s2)
```
```
s1="abhinav"
s2="Singh"
print(s1+s2*2)
```
#### Slicing
Slicing is in 2 direction<br>
Forward Direction<br>
Back Direction

``There is no exception in slicing whether the end is given out of bound``

```
s ="Learning Python is very very easy!!!"
print(len(s))
print(s[1:7:1])
print(s[:7])
print(s[7:])
print(s[7:10000000000000000000000000])
print(s[::])
print(s[:])

s='abcdefghij'
print(s[1:6:2])
print(s[::1])
print(s[::-1])
print(s[3:7:-1])
print(s[7:4:-1])
print(s[0:10000:1])

```
---
### How to remove the space of string
#### Strip Function
1. .strip()
2. .lstrip()
3. .rstrip()

``In string there are some functions that are inplace and some are outplace``

```
x=input()
print(x)
removed=x.strip()
print(removed)
```
#### Finding sub string
1. find 
```
l="learning python is easy"
print(l.find("python"))
```
```
l="learning python is easy"
print(l.find("python")+len("python")-1)
```
>Find function returns **-1** if the sub string is not found!
```
l="learning python is easy"
print(l.find("python")+len("python")-1)
print(l.find("abhinav"))
print(l.find("abhinav",0,5))
```
2. index (value error exception)
```
l="learning python is easy"
print(l.find("python")+len("python")-1)
print(l.find("abhinav"))
print(l.find("abhinav",0,5))
print(l.index("python",0,5))
```

#### Replace Function
```
s="learning python is every easy"
print(s.replace("pyhton","html"))
```

#### Join function (Most Important method)
The container should be always the collection of string.
```
l=[1,2,3,4,5]
n=len(l)
print(l[n-1])
for i in l:
    if i==l[n-1]:
        print(i)
    else:
        print(i,end=",")
```

```
l=['1','2']
sep=",".join(l)
print(sep)
```

```
#Write a program to remove duplicate element from list
inp=input("Enter the data ").split()
l1=[]
for i in inp:
    if i not in l1:
        l1.append(i)

print(l1)

```

### Case Changing Methods
1. upper()To convert all characters to upper case<br>
2. lower()  To convert all characters to lower case<br>
3. swapcase()  Converts all lower case characters to upper case and all upper case
characters to lower case<br>
4. title()  To convert all character to title case. i.e first character in every word should
be upper case and all remaining characters should be in lower case.<br>
5. capitalize()  Only first character will be converted to upper case and all remaining
characters can be converted to lower case
6. isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
7. isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
8. isdigit(): Returns True if all characters are digits only( 0 to 9)
9. islower(): Returns True if all characters are lower case alphabet symbols
10. isupper(): Returns True if all characters are upper case aplhabet symbols
11. istitle(): Returns True if string is in title case
12. isspace(): Returns True if string contains only spaces

Program to reverse the string
```
s=input("enter string ")
print(s[::-1])
print("".join(reversed(s)))
```
 
Program to reverse the sentence
```
inp=input("Enter string ").split()
print(" ".join(reversed(inp)))
```
Reverse the words in string
```
inp=input("Enter string ").split()
for i in inp:
    print(i[::-1],end=" ")
```
Reverse even words: 
```
l=input("Enter string ").split()
l1=[]
i=0
while (i<len(l)):
    if i%2==0:
        l1.append(l[i][::-1])
    else:
        l1.append(l[i])
    i+=1
print(" ".join(l1))
```

If **input= a4k3b2** then **Output: aeknbd** :

```
inp=input("Enter string ")
i=0
s=''
for x in inp:
    if x.isalpha():
        s+=x
        previous=ord(x)
        
    if x.isdigit():
        s+=chr(previous+int(x))


print(s)
```

If **input= a1bc2d3** then **Output: abcd123** :
```
inp=input("Enter string ")
i=0
s=''
c=''
for x in inp:
    if x.isalpha():
        s+=x
        previous=ord(x)
        
    if x.isdigit():
        c+=x

s+=c;
print(s)
```
**Input= ABCDABBBCCCDDDFFF <br>
Output= ABCD**
```
s=input("enter string")
a=''
for i in s:
    if i not in a:
        a+=i
print(a)
```
**Input=e4d1<br>
output=de14**
```
inp=input("Enter string ")
l1=[]
l2=[]
for i in inp:
    if i.isalpha():
        l1.append(ord(i))
    else:
        l2.append(ord(i))    
l1=sorted(l1)
l2=sorted(l2)

final=l1+l2
st=''
for i in final:
    st+=chr(i)
print(st)
```
