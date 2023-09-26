# Object Oriented Programming (29/8/23)

* In python everything is object
* Class is blueprint
* Classs is having attributes and behaviour
* properties
--> data, behaviour is methd
* properties
--> variable
* actions---> method


```python
class Student:
    """This is student class"""
    pass

print(Student.__doc__)

```

    This is student class
    

#### What is object ?
* object is a instance of class
* physical existence of class is nothing but its a object


```python
s=Student()
print(type(s))
```

    <class '__main__.Student'>
    

s is refrence variable pointing to student type of ojbect

#### Defining the constructor in Class

``self is mandatory argument for constructor and instance method of the class. we can use any name instead of self``


```python
class Student:
    """This is a student class"""
    def __init__(self,roll,name,marks):
        self.rollno=roll
        self.name=name
        self.marks=marks
    def info(self):
        print("My name is",self.name)
        

obj=Student(6,"Abhinav",7.78)
obj.info()        
```

    My name is Abhinav
    

1. self/ -- is the default variable which is always pointing to the current variable.
2. By using self/-- we can access the instance variable and instance method of the object.
3. Constructor is a special method in class. and self should be passes in every instance of the class
4. The main purpose of the Const. is to declare or initiliaze argument
5. Const. should have atleast one argument
6. Const. is optional, python provide by default constructor if we are not defining it


```python
class Test:
    def __init__(self):
        print("Constructor Executed !")

t1=Test()
```

    Constructor Executed !
    

### Types of variable
In python there are 3 types of variable
1. is intance variable (object level variable)
2. is Static variable (class level variable)
3. local variable(method level variable)

#### Instance Variable
if the value of a variable is varied object to object
then such type of variables are known as instance variablesf for every object a separate copy of instance varible  created.

##### Places to define
1. inside constructor using self/-- variable
2. inside instance method
3. outside the class.

## (12-09-23 )

### Instance variables 

#### Magic Method


```python
class Test:
    def __init__(self):
        #inside constructor
        self.a=10 #instance variable
    def m(self):
        #inside the instance method.
        self.b=20

t=Test()
print(t.__dict__)
t.m()
print(t.__dict__)
t.c=30
print(t.__dict__)
#declaring the variable outside the class

t1=Test()
print(t1.__dict__)
print(t1.__dict__)
t1.m()
print(t1.__dict__)
```

    {'a': 10}
    {'a': 10, 'b': 20}
    {'a': 10, 'b': 20, 'c': 30}
    {'a': 10}
    {'a': 10}
    {'a': 10, 'b': 20}
    

##### 1. How to access the instance variable
##### 2. outside the class using reference variable
##### 3. inside the class using self

#### Question:  


```python
class Student:
    def putData(self):
        self.name=input("Enter your name: ")
        self.enroll=input("Enter the enrollment number: ")
        self.age=int(input("Enter the age: "))
        self.branch=input('Enter your branch')
        self.sem=input('Enter your sem')
    def getData(self):
        print("Name ",self.name)
        print("Enrollment Number ",self.enroll)
        print("Age ",self.age)
        print("Branch ",self.branch)
        print("Sem: ",self.sem)
        print()

s1=Student()
s2=Student()
s1.putData()
s2.putData()
s1.getData()
s2.getData()
```

    Enter your name:  Abhinav
    Enter the enrollment number:  6
    Enter the age:  20
    Enter your branch cs
    Enter your sem 5
    Enter your name:  anushka
    Enter the enrollment number:  33
    Enter the age:  23
    Enter your branch cs
    Enter your sem 5
    

    Name  Abhinav
    Enrollment Number  6
    Age  20
    Branch  cs
    Sem:  5
    Name  anushka
    Enrollment Number  33
    Age  23
    Branch  cs
    Sem:  5
    


```python
class Book:
    def Input(self):
        self.book_no=int(input('enter book no: '))
        self.book_name=input('enter book name: ')
        self.book_price=int(input('enter book price: '))
    def totalCost(self,qty):
        return qty*self.book_price
    def purchase(self):
        qty=int(input('Enter the quantity: '))
        print('the total cost will be ',self.totalCost(qty))

user=Book()  
user.Input()
user.purchase()
        
```

    enter book no:  1
    enter book name:  Rich dad 
    enter book price:  50
    Enter the quantity:  4
    

    the total cost will be  200
    

### Static Variable
* inside class butoutside all method
* inside consstructor but using classname
* inside instacne method using classname
* inside static method using classname
* inside classmethod using class name
#### How to access Static variable
* inside constructor by using either self or classname
* inside instance method by using either self or class name
* inside class method by using either self or classname
* inside static method by using classname
* from outside of class by using either object reference or class name.


```python
class Test:
    x=10

t=Test()
print(t.__dict__)
print(Test.__dict__)
```

    {}
    {'__module__': '__main__', 'x': 10, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
    

* Where we can modify the Value of Static Variable:
* 
Anywhere either with in the class or outside of class we* 
can modify by using classname. But inside class method, by using cls variabl
### Local Variables:
⚽ Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,
such type of variables are called local variable or temporary variables. 

⚽ Local variables will be created at the time of method execution and destroyed once method completes.

⚽ Local variables of a method cannot be accessed from outside of method.e



```python
class Test:
    def m1(self):
        a=1000
        print (a)
    def m2(self):
        b=2000
        # print (a) #create an  error
        print (b)
t=Test()
t.m1()
t.m2()
```

    1000
    2000
    

#### Types of Method
1. Instance Method
2. Class Method
3. Static Method

#### **Instance Method**:
* The method inside which we use the instance variable is known as the instance method.
* The method inside which we use the instance variable is known as the instance method
*  inside instance method declaration has to pas
*  self argument
* by the self-lf variable inside the method we can access
*  instance variable to call its method inside we use-self variable
* outside using object reference variable


```python
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def s_add(self,add):
        self.add=add
        return(self.add)
    def display(self):
        print("name",self.name)
        print("marks",self.marks)
        print("address of studnet",self.s_add("durga nagar"))
s=Student("rahul",100)
s.display()
```

    name rahul
    marks 100
    address of studnet durga nagar
    

#### Class Method

Inside method implementation if we are using only class variables (static variables), then such types of methods should be declared as class methods.

⚽ We can declarthe e class method explicitly by usinthe g @classmethod decorator.

⚽ the For class method we should provthe ide cls variable at the time of declaration 

⚽ We canthe  call  classmethod by the using  classname or object reference variable.

Program to track the Number of Objects created for a Class


```python
class Test:
    count=0
    def __init__(self):
        Test.count+=1
    @classmethod
    def displayCount(cls):
        print("The number of objects are: ",cls.count)
t=Test()
t1=Test()
t2=Test()
t3=Test()
t3.displayCount()
```

    The number of objects are:  4
    

#### Static Method


⚽ In general these methods are general utility methods.

⚽ Inside these methods we won't use any instance or class variables. 

⚽ Here we won't provide self or cls arguments at the time of declaration.

⚽ We can declare static method explicitly by using @staticmethod decorator 

⚽ We can access static methods by using classname or object reference



```python
class Abhinav:
    p=10
    q=20
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(self.p+self.q)
        
    @staticmethod
    def add(x,y):
        print("the sum is ",x+y)
    @staticmethod
    def mul(x,y):
        print("the mul is ",x*y)

abhi=Abhinav(5,6)
abhi.add(5,6)
abhi.mul(5,6)
```

    30
    the sum is  11
    the mul is  30
    

## Garbage Collection


```python
import gc
print(gc.isenabled())
# gc.disable()
print(gc.isenabled())
```

    False
    False
    

#### Destructor


```python
import time
class Test:
    def __init__(self):
        print("Object Initialization")
    def __del__(self):
        print("Kya tumhari koi icha hai ? ")

t=Test()
t=None
time.sleep(5)
print("Shut Down")

```

    Object Initialization
    Kya tumhari koi icha hai ? 
    Shut Down
    

# Part -II
Using one class member inside another class

#### Composition


```python
import time
class Engine:
    etype="four stroke"
    def __init__(self):
        self.company="tata"
    def __del__(self):
        print("releasing all engine resources")
    def detail(self):
        print("engine functionality")
class Car:
    def __init__(self):
        self.engine=Engine()
    def __del__(self):
        print("releasing all car resources")
        time.sleep(3)
    def car_detail(self):
        self.engine.detail()
        print(self.engine.etype)
        
c=Car()
c.car_detail()
del c
```

    engine functionality
    four stroke
    releasing all car resources
    releasing all engine resources
    

#### aggregation


```python
class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __del__(self):
        print("car is releasing resources")
    def car_info(self):
        print(self.name,self.color)
class Emp:
    def __init__(self,name,add,car):
        self.name=name
        self.add=add
        self.car=car
    def __del__(self):
        print("emp release")
    def emp_car_info(self):
        self.car.car_info()
        
c=Car("TUV","black")
emp=Emp("rahul","vidisha",c)
emp.emp_car_info()
del emp
c.car_info()
```

    TUV black
    emp release
    TUV black
    


```python

```
