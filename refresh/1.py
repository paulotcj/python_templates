num_int = 123  # An integer assignment
num_flo = 1.23 # A floating point

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


print('----------------------------------------------')

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))


print('----------------------------------------------')

my_list = [1, 2, 3, 'example', 3.132, 10, 30]

print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'example'

print('----')

print(my_list[-1])  # Output: 30
print(my_list[-4])  # Output: 'example'
print('----')
print(my_list[2:5])  # Output: [3, 'example', 3.132] - 5 is not inclusive
print('----')
my_list[3] = 'changed'  # change the fourth element
print(my_list)
print('----')
print(my_list)
my_list.append('new item')  # add to the end
print('----')
my_list.insert(1, 'inserted item')  # insert at position 1
print(my_list)
my_list.insert(3, 'inserted item 2')  # insert at position 3
print(my_list)


print('----------------------------------------------')

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
print(list2)  # Output: [4, 5, 6]

print('----------------------------------------------')
list1 = ['a', 'b', 'c']
tuple1 = ('d', 'e', 'f')
list1.extend(tuple1)
print(list1)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
print('----------------------------------------------')
list1 = ['Hello', 'world']
str1 = '!' 
list1.extend(str1) # this is because strings are iterable
print(list1)  # Output: ['Hello', 'world', '!']
print('----------------------------------------------')
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy() #this is a shallow copy
original_list.append(6)
print('Original List:', original_list)  # Output: [1, 2, 3, 4, 5, 6]
print('Copied List:', copied_list)  # Output: [1, 2, 3, 4, 5]

#these lists will share the same nested 'OBJECT'

print('----------------------------------------------')

original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = original_list.copy()

original_list[0][0] = 'changed'

print(original_list)  # Output: [['changed', 2, 3], [4, 5, 6]]
print(copied_list)  # Output: [['changed', 2, 3], [4, 5, 6]]

print('----------------------------------------------')

original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = original_list.copy()

original_list[0] = 'test'

print(original_list)  # Output: ['test', [4, 5, 6]]
print(copied_list)  # Output: [[1, 2, 3], [4, 5, 6]]
print('----------------------------------------------')


list1 = [1, 2, 3, 2, 4, 2, 5]
#           ^     ^     ^      total 3
count = list1.count(2)
print(f'List count element 2: {count}')  # Output: 3

print('----------------------------------------------')
list1 = [(1, 2), (3, 4), (1, 2), (5, 6), (1, 2), (7, 8), (1, 2)]
#         ^               ^               ^               ^        total 4
count = list1.count((1, 2)) #count this tuple
print(f'List count tuple (1,2) : {count}')  # Output: 4


print('----------------------------------------------')
list1 = [1, 2, 3, 4, 5, 2]
index = list1.index(2) #return the index of the first element
print(f'The index of the first occurrence of 2: {index}')  # Output: 1
print('----------------------------------------------')

list1 = [(1, 2), (3, 4), (1, 2)]
index = list1.index((1, 2))
print(f'The index of the first occurrence of (1,2): {index}')  # Output: 0

print('----------------------------------------------')
list1 = [1, 2, 3, 2, 4, 2, 5]
#              [  ^     ]      -> it would be found at index 3
index = list1.index(2, 2, 5) #value, start, end
print(f'The index of the first occurrence of 2, starting to look from index 2 and ending at 5 is : {index}')  # Output: 3

print('----------------------------------------------')
list1 = [1, 2, 3, 2, 7, 2, 5]
#              [  ^     ]      
index = list1.index(7, 2, 5) #value, start, end
print(f'The index of the first occurrence of 7, starting to look from index 2 and ending at 5 is : {index}')  

print('----------------------------------------------')
list1 = [1, 2, 7, 2, 6, 2, 5]
#              [  ^     ]      
index = list1.index(7, 2, 5) #value, start, end
print(f'The index of the first occurrence of 7, starting to look from index 2 and ending at 5 is : {index}') 
print('----------------------------------------------')
list1 = [1, 2, 3, 2, 6, 7, 5]
#              [  ^     ]      
index = None
try:
    index = list1.index(7, 2, 5) #value, start, end
except Exception as e:
    print(f'This will result in an error because 5 is not inclusive')
print(f'The index of the first occurrence of 7, starting to look from index 2 and ending at 5 is : {index}')


print('----------------------------------------------')
list1 = [1, 2, 3, 4, 5]
print(f'Original List: {list1}')
popped_element = list1.pop()
print(f'Poped element: {popped_element}')  # Output: 5
print(f'List after pop: {list1}')  # Output: [1, 2, 3, 4]
print('----------------------------------------------')

#        0  1  2  3  4
list1 = [1, 2, 3, 4, 5]
popped_element = list1.pop(2)
print(f'Poped element: {popped_element}')  # Output: 3
print(f'List after pop: {list1}')  # Output: [1, 2, 4, 5]


print('----------------------------------------------')

#        0  1  2  3  4
list1 = [1, 2, 3, 4, 5]
popped_element = list1.pop(-1)
print(f'Poped element: {popped_element}')  
print(f'List after pop: {list1}')  

print('----------------------------------------------')

#        0  1  2  3  4
list1 = [1, 2, 3, 4, 5]
popped_element = list1.pop(-2)
print(f'Poped element: {popped_element}')  
print(f'List after pop: {list1}')  

print('----------------------------------------------')

list1 = [1, 2, 3, 4, 5]
min_value = min(list1)
print(f'min_value from a list of numbers: {min_value}')  # Output: 1

print('----------------------------------------------')

list2 = ['banana','apple', 'cherry']
min_value = min(list2)
print(f'min_value from a list of strings: {min_value}')  # Output: 'apple'


print('----------------------------------------------')


list3 = [[1, 2, 3], [1,1,1], [1,0], [1, 0, 0]]
min_value = min(list3)
print(min_value)  # Output: [1, 0]

print('----------------------------------------------')
list1 = [5, 3, 1, 4, 2]
list1.sort()
print(list1)  # Output: [1, 2, 3, 4, 5]

print('----------------------------------------------')
list3 = [5, 3, 1, 4, 2]
list3.sort(reverse = True)
list3.sort(reverse= True)
print(list3)  # Output: [5, 4, 3, 2, 1]

print('----------------------------------------------')
list1 = [1, 2, 3, 1, 2, 1, 2, 3, 3, 3]
count = list1.count(3)
print(count)  # Output: 4

print('----------------------------------------------')
list2 = ['apple', 'banana', 'cherry', 'apple', 'cherry', 'cherry']
count = list2.count('cherry')
print(count)  # Output: 3


print('----------------------------------------------')
list3 = [[1, 2], [3, 4], [1, 2], [5, 6], [1, 2]]
count = list3.count([1, 2])
print(count)  # Output: 3

print('----------------------------------------------')

list1 = [1, 2, 3, 1, 2, 1, 2, 3, 3, 3]
count = list1.count(7)
print(count)  

print('----------------------------------------------')

list1 = [1,2,3,4,3,5]
# list1.remove(7) #this will result in an error
list1.remove(3) #removes only the first occurrence
print(list1) 


print('----------------------------------------------')
list3 = [[1, 2], [3, 4], [1, 2], [5, 6], [1, 2]]
list3.remove([1, 2])
print(list3)  # Output: [[3, 4], [1, 2], [5, 6], [1, 2]]

print('----------------------------------------------')

list3 = [{'cherry':1}, {'apple':2}, {'banana':3}, {'apple':2}]
list3.remove({'banana':3})
print(list3) 

print('----------------------------------------------')
list1 = [1,2,3,4,3,5]
if 7 in list1: #in order to avoid error
    list1.remove(7)
print(list1) 

print('----------------------------------------------')

list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)  # Output: [5, 4, 3, 2, 1]

print('----------------------------------------------')
list2 = ['apple', 'banana', 'cherry']
list2.reverse()
print(list2)  # Output: ['cherry', 'banana', 'apple']
print('----------------------------------------------')
list3 = [[1, 2], [3, 4], [5, 6]]
list3.reverse()
print(list3)  # Output: [[5, 6], [3, 4], [1, 2]]

print('----------------------------------------------')
list1 = [1, 3, 2, 5 , 4]
list1.reverse()
print(list1)


print('----------------------------------------------')

#         0  1  2  3  4  5  6  7
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8]
print(list1[2]) # Output: 3
print(list1[2:5]) # Output: [3, 4, 5] - 5 is not inclusive
print(list1[2:7:2]) # Output: [3, 5, 7] - 7 is not inclusive
print(list1[2:]) # Output: [3, 4, 5, 6, 7, 8]
print(list1[:5]) # Output: [1, 2, 3, 4, 5] - 5 is not inclusive
print(list1[:]) # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::2]) # Output: [1, 3, 5, 7]
print(list1[::3]) # Output: [1, 4, 7]
print(list1[::-1]) # Output: [8, 7, 6, 5, 4, 3, 2, 1]
print(list1[-1]) # Output: 8
print(list1[-3]) # Output: 6
print(list1[-3:]) # Output: [6, 7, 8]
print(list1[-3::-1]) # Output: [6, 5, 4, 3, 2, 1]
print(list1[:-3]) # Output: [1, 2, 3, 4, 5]

print('----------------------------------------------')
a = 10
b = 3
print(a / b)  # Output: 3.3333333333333335

print('----------------------------------------------')
a = 10
b = 3
print(a // b)  # Output: 3

print('----------------------------------------------')
a = 10
b = 3
print(a % b)  # Output: 3

print('----------------------------------------------')
a = 2
b = 3
print(a ** a)  # Output: 4
print(a ** b)  # Output: 4

print('----------------------------------------------')
a = 0  # In a boolean context, 0 is False
b = 5  # Non-zero values are True
print(a and b)  # Output: 0
print(a or b)   # Output: 5
print(not a)    # Output: True
print('----------------------------------------------')
a = 2
b = 3
print(a and b)  # Output: 0
print(a or b)   # Output: 5
print(not a)    # Output: True

print('----------------------------------------------')
print('bitwise AND')
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary
#              0000 1100

print( a & b ) # Output: 12 (0000 1100)

print('----------------------------------------------')
print('bitwise OR')
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary
#              0011 1101

print( a | b ) # Output: 61 (0011 1101)

print('----------------------------------------------')
print('bitwise XOR')
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary
#              0011 0001
print(a ^ b)  # Output: 49 (0011 0001)

print('----------------------------------------------')




names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)

print(zipped)

# Convert zipped object into a list to see the result
print(list(zipped))

print('----------------------------------------------')

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]

zipped = zip(names, ages)
print(list(zipped))

print('----------------------------------------------')

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)
# zipped = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

names2, ages2 = zip(*zipped)

print(names2)  # ('Alice', 'Bob', 'Charlie')
print(ages2)   # (25, 30, 35)


print('----------------------------------------------')
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

zipped = zip(names, ages, cities)
print(list(zipped))


print('----------------------------------------------')
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]

zipped = zip_longest(names, ages, fillvalue=None)
print(list(zipped))


zipped = zip_longest(names, ages, fillvalue='NOT PROVIDED')
print(list(zipped))



print('----------------------------------------------')
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

dictionary = dict(zip(keys, values))
print(dictionary)