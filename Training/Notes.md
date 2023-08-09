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

# Literal Error/ Value Error Here
```
```
x="10"
y=int(x)
print(y)

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

#<class 'range'>
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```
x=None
print(type(x))

#<class 'NoneType'>
```

```
x=None
x=5
print(x)

#5
```
