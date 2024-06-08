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






