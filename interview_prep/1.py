

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
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

print('-------------------------------------------------------------------------')

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def compute_square(n):
    return [i * i for i in range(n)]

compute_square(10000)