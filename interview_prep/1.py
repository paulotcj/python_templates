

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

