

''' 
What's the difference between a tuple and a list?
Both tuples and lists are data structures in Python and hold a list of values. Unlike 
lists, tuples are immutable - they can't be changed.
'''

print('-------------------------------------------------------------------------')

'''
What is a dict and what's its most important limitation?
A dict is a structure akin a hash map. It stores key-value pairs, where keys are unique 
and it has O(1) access time. The most important limitation for a dict is that the keys must 
be hashable/immutable. Meaning, we can use a tuple as a key, but not a list.
'''

ditct1 = {}
ditct1[(1,1)] = 1
ditct1[(1,2)] = 2 

# ditct1 = {}
# ditct1[[1,1]] = 1 # This will raise an error
# ditct1[[1,2]] = 2

print('-------------------------------------------------------------------------')

'''
What is a "callable"?
A callable is an object we can call - function or an object implementing the 
__call__ special method. Any object can be made callable.
'''

print('-------------------------------------------------------------------------')
'''
Using list comprehension, print the odd numbers between 0 and 100.
[a for a in range(0, 100) if a%2]
'''

list1 = [ x for x in range(0, 100+1) if x%2] # odd numbers
print(list1)

list1 = [x for x in range(0, 100+1) if x%2 == 0] # even numbers - notice since the range is non inclusive we need to add +1
print(list1)

print('-------------------------------------------------------------------------')


'''
What is pickling/unpickling?
Pickling is converting an object to a string representation in python. Generally used for 
caching and transferring objects between hosts/processes.
'''

import pickle
# Example of pickling
data = {'key': 'value'}
with open('data.pkl', 'wb') as file: #open file data.pkl for writing in binary
    pickle.dump(data, file)

# Example of unpickling
with open('data.pkl', 'rb') as file: #open file data.pkl for reading in binary
    loaded_data = pickle.load(file)

print(loaded_data)

print('-------------------------------------------------------------------------')


'''
What's a generator?
A generator is a callable object that acts as an iterable (object you can iterate in for cycles etc).
'''

def simple_generator():
    yield 1
    yield 2
    yield 3

for v in simple_generator():
    print(f'v from simple generator: {v}')

def fibonacci_generator(n):
    a , b = 0 , 1
    for i in range(n):
        yield a
        a , b = b , a + b

# for v in fibonacci_generator(50):
for v in fibonacci_generator(5):
    print(f'v in fibonacci generator: {v}')


print('-------------------------------------------------------------------------')

'''
Explain the use of decorators.
Decorators in Python are used to modify or inject code in functions or classes. Using 
decorators, you can wrap a class or function method call so that a piece of code can 
be executed before or after the execution of the original code. Decorators can be used 
to check for permissions, modify or track the arguments passed to a method, logging the 
calls to a specific method, etc.
'''

#----------------------------
def simple_decorator(func):
    #----------------------------
    def wrapper():
        print(f'inside decorator and before function call')
        func()
        print(f'inside decorator and after function call')
    #----------------------------
    
    return wrapper
#----------------------------
#----------------------------
@simple_decorator
def greet():
    print('Hello from greet function')
#----------------------------

greet()

print('-------------------------------------------------------------------------')


'''
Suppose lst is [2, 33, 222, 14, 25], What is lst[-1]?
25. Negative numbers mean that you count from the right instead of the left. So, lst[-1] 
refers to the last element, lst[-2] is the second-last, and so on.
'''

lst = [2, 33, 222, 14, 25]

print(f'lst[-1]:{lst[-1]}')


print('-------------------------------------------------------------------------')

'''
Given the list lst = [1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7], return only the unique values 
in the list.

set(lst) - one answer. The limitation of this solution is that values should be hashable.
Another answer is to iterate through the list and use an intermediate list to store the 
current value. Then for every next value, check if it's added already.
'''

lst = [1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7]
# Option 1: Using set
unique_from_set = sorted(list( set(lst) ))
print(f'unique_from_set using set(): {unique_from_set}')

# Option 2: Using list comprehension and a temporary list
unique_values_list = []
[   
    unique_values_list.append(x)
    for x in lst
    if x not in unique_values_list
]
unique_values_list = sorted(unique_values_list)
print(f'unique_values_list using list comprehension:{unique_values_list}')
# exit()

# Option 3: Using a dictionary to maintain order
unique_values_list = list( dict.fromkeys(lst) )
print(f'unique_values_list using a dict:{unique_values_list}')


print('-------------------------------------------------------------------------')
'''
What's lambda?
Lambda in Python is an anonymous function created at runtime.
'''

add_lambda = lambda x,y: x+y

result_lambda = add_lambda(x = 3 , y = 5)
print(f'The result of the lambda function is: {result_lambda}')

print('-------------------------------------------------------------------------')


'''
Explain *args and **kwargs
Although, there is no formal rule on calling them *args/**kwargs, people tend to name them 
that way. When a function is declared def my_func(*args, **kwargs), args is a tuple with 
all positional arguments passed to the function and kwargs is a dict with all keyword 
arguments. They can be named anything as long as the unpack operators * and ** are used.
* unpacks a tuple and ** unpacks a dict.
'''

def example_args_kwards(*args, **kwargs):
    print(f'Positional arguments (args): {args}')
    print(f'Keyword arguments (kwargs): {kwargs}')

example_args_kwards(1,2,3, a = 4, b = 5)

print('-------------------------------------------------------------------------')



'''
Is this valid in Python and why?

def my_function():
    print my_function.what
my_function.what = "right?"
my_function() # Prints "right?"
-------------
It is valid. In Python, everything is an object, including functions. But if we don't 
have what defined, we will get an Attribute error.
'''

def my_weird_function():
    print(f'my_weird_function.weird_part: {my_weird_function.weird_part}')

my_weird_function.weird_part = "This is weird isn't it?"

my_weird_function()


print('-------------------------------------------------------------------------')


'''
Given variables a and b, switch their values so that b has the value of a, and a has the 
value of b without using an intermediary variable.

a, b = b, a
'''

x = 3
y = 5
print(f'x:{x}, y:{y}')

x , y = y , x
print('after swap')
print(f'x:{x}, y{y}')

print('-------------------------------------------------------------------------')


'''

How would you xor in Python?
XOR Truth Table:
A | B | A XOR B
--|---|--------
0 | 0 |   0
0 | 1 |   1
1 | 0 |   1
1 | 1 |   0
'''

print('XOR using ^')
for x in (True, False):
    for y in (True, False):
        result = x ^ y
        print(f'x:{x}\t\ty:{y}\t\tresult:{result}')

import operator

print('\n\nXOR using operator operator.xor()')
for x in (True, False):
    for y in (True, False):
        result = operator.xor(y,x)
        print(f'x:{x}\t\ty:{y}\t\tresult:{result}')

print('\n\nXOR using IF')
for x in (True, False):
    for y in (True, False):
        if (x == True and y == True) or (x == False and y == False):
            result = False
        elif (x == False and y == True) or (x == True and y == False):
            result = True
        
        print(f'x:{x}\t\ty:{y}\t\tresult:{result}')

print('\n\nXOR using logic')
for x in (True, False):
    for y in (True, False):
        result = x != y
        print(f'x:{x}\t\ty:{y}\t\tresult:{result}')



print('-------------------------------------------------------------------------')

'''
What is introspection/reflection and does Python support it?

Introspection is the ability to examine an object at runtime. Python has a dir() function that 
supports examining the attributes of an object, type() to check the object type, isinstance(), etc.
While introspection is passive examination of the objects, reflection is a more powerful tool 
where we could modify objects at runtime and access them dynamically. E.g.
    setattr() adds or modifies an object's attribute;
    getattr() gets the value of an attribute of an object.

It can even invoke functions dynamically - getattr(my_obj, "my_func_name")()
'''

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return f'My value is {self.value}'

obj = MyClass(10)
print(obj.my_method())


#introspection
# Using dir() to list attributes and methods
print(f'Attributes and methods of obj: {dir(obj)}')

# Using type() to get the type of the object
print(f'Type of obj: {type(obj)}')

# Using isinstance() to check if obj is an instance of MyClass
print(f'Is obj an instance of MyClass? {isinstance(obj, MyClass)}')

# reflection
# Using getattr() to get the value of an attribute
print(f'Value of obj.value: {getattr(obj, "value")}')

# Using setattr() to set the value of an attribute
setattr(obj, 'value', 20)
print(f'New value of obj.value: {obj.value}')

# Using hasattr() to check if an attribute exists
print(f'Does obj have attribute "value"? {hasattr(obj, "value")}')

# Using getattr() to call a method dynamically
method = getattr(obj, 'my_method')
print(f'Result of calling obj.my_method(): {method()}')


# Using getattr() to call a method dynamically
method = getattr(obj, 'my_method')
obj = None
print(f'Result of calling obj.my_method(): {method()}')


print('-------------------------------------------------------------------------')


'''
One thing about python OOP is that it doesn't support true private attributes/methods. 
How do we circumvent this limitation?

There is a convention if we prefix the name with an underscore, it's considered private.
'''

print('-------------------------------------------------------------------------')


'''
What's a Mixin?

Mixin is a concept in Programming in which the class provides functionalities but it is 
not meant to be used for instantiation. The main purpose of the Mixin is to provide 
functionalities which are standalone and it would be best if the mixins themselves do 
not have inheritance with other mixins and also avoid state.
'''

class FlyMixin:
    def fly(self):
        return "I can fly!"

class SwimMixin:
    def swim(self):
        return "I can swim!"

class Bird(FlyMixin):
    def __init__(self, name):
        self.name = name

class Fish(SwimMixin):
    def __init__(self, name):
        self.name = name

class Duck(FlyMixin, SwimMixin):
    def __init__(self, name):
        self.name = name

# Usage
bird = Bird("Sparrow")
print(f'{bird.name}: {bird.fly()}')

fish = Fish("Goldfish")
print(f'{fish.name}: {fish.swim()}')

duck = Duck("Mallard")
print(f'{duck.name}: {duck.fly()} and {duck.swim()}')

print('-------------------------------------------------------------------------')


'''
What's a metaclass?

In Python, a metaclass is a class that defines the behavior of other classes.
It's a class of classes, responsible for creating class objects.
The default metaclass for all classes in Python is type.

In other words, all classes inherit from at least the class type
and Type defines certain methods such as __new__ and __init__
'''


print('-------------------------------------------------------------------------')


'''

What are the Dunder/Magic/Special methods in Python? Name a few.

Dunder (derived from double underscore) methods are special/magic predefined methods in Python, 
with names that start and end with a double underscore. There's nothing really magical about 
them. Examples of these include:
__init__ - constructor
__str__, __repr__ - object representation (casting to string, printing)
__len__, __next__... - generators
__enter__, __exit__ - context managers
__eq__, __lt__, __gt__ - operator overloading
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Values(x:{self.x}, y:{self.y})'

    def __add__(self, other_obj):
        return Point( x = self.x + other_obj.x, y = self.y + other_obj.y )
    
p1 = Point(x = 1, y = 2)
p2 = Point(x = 3, y = 4)

p3 = p1 + p2

print(f'p1: {p1}')
print(f'p1 + p2 = p3 = {p3}')
exit()

print('-------------------------------------------------------------------------')

'''
What is PEP8?

PEP8 is a generally recognized style guide for programming in Python. It covers formatting, 
comments, naming conventions, but also programming recommendations as well as useful tips 
on various topics. The main aim of PEP8 is to help developers improve code readability, 
reliability and maintainability.
'''

print('-------------------------------------------------------------------------')


'''
What is pip?

pip is a package installer for Python
Installs packages: It downloads and installs Python packages (libraries) from the 
Python Package Index (PyPI) and other sources.  
Manages packages: You can use pip to uninstall packages, update existing ones to 
the latest versions, and manage their dependencies. 
Essential for Python development: Most Python projects rely on external libraries for
 various functionalities (e.g., data science, web development, machine learning). pip 
 makes it easy to incorporate these libraries into your projects. 
'''



print('-------------------------------------------------------------------------')
'''
CheeseShop? What is that?

In the Python world, "CheeseShop" is a playful, unofficial term that refers to PyPI, the 
Python Package Index.
'''

print('-------------------------------------------------------------------------')
'''
What are virtualenvs?

A virtual environment is an isolated space where you can install and manage project-specific 
packages without affecting your system-wide Python installation or other projects.
'''


print('-------------------------------------------------------------------------')

'''
What are modules and packages in Python?

A module in Python is any file with .py extension. A package is a set of modules - a 
directory that contains one or many .py files, one of which is __init__.py
Both modules and packages define functions, classes or any kind of software functionality.
When we import something in Python, we import from packages and modules.
'''