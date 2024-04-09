import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
import numpy as np

print('----------------------------------------------')
# Normal Distribution
x = random.normal(size=(2, 3))

print(x)

print('----------------------------------------------')
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape of the returned array.

x = random.normal(size=(2, 3)) #2 rows and 3 values in each row

print(x)

print('----------------------------------------------')
x = random.normal(loc=1, scale=2, size=(2, 3)) #the peak of the bell exists at 1, and the standard deviation is 2
print(x)

print('----------------------------------------------')
#Binomial Distribution - e.g.: coin toss
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

# 10 coin toss generate 10 data points:
x = random.binomial(n=10, p=0.5, size=10)

print(x)

print('----------------------------------------------')


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
arr3 = []
arr4 = []
for i , j in zip(arr1, arr2):
    print(f'i: {i}, j: {j}')
    arr3.append(i)
    arr3.append(j)
    arr4.append( i + j)

print(arr3)
print(arr4)


print('----------------------------------------------')


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

arr3 = np.add(arr1, arr2)

print(arr3)

print('----------------------------------------------')

def myAdd(param1 : int, param2 : int) -> int:
    return param1 + param2

x = myAdd(1, 2)
print(x)


my_add = np.frompyfunc(myAdd, 2, 1)

arr5 = None
arr5 = my_add([1, 2, 3, 4], [5, 6, 7, 8])
print(type(arr5))
print(arr5)

print(type(my_add))


print('----------------------------------------------')

arr1 = np.array([1, 2, 1, 2, 1, 2])
arr2 = np.array([2, 1, 2, 1, 2, 1])

newarr = np.add(arr1, arr2)

print(newarr)


print('----------------------------------------------')

arr1 = np.array([3, 4, 5, 6, 7, 8])
arr2 = np.array([1, 2, 3, 4, 5, 6])

newarr = np.subtract(arr1, arr2)
print(newarr)


print('----------------------------------------------')


arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([10, 11, 10, 11, 10, 11])

newarr = np.multiply(arr1, arr2)

print(newarr)

print('----------------------------------------------')


arr1 = np.array([3, 5, 5, 6, 8, 27])
arr2 = np.array([2, 4, 5, 2, 3, 3])

newarr = np.divmod(arr1, arr2)

print(newarr)

print('----------------------------------------------')
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

print('----------------------------------------------')

arr = np.array([-3.1666, 3.6667])
arr = np.trunc(arr)

print(arr)
print('----------------------------------------------')

arr = np.array([-3.1666, 3.6667])
arr = np.fix(arr)

print(arr)

print('----------------------------------------------')
arr = np.around(3.1666, 2)
print(arr)

print('----------------------------------------------')
arr = np.floor([-3.1666, 3.6667]) #the lower/floor value of -3.166 is -4, and for 3.6667 is 3
print(arr)

print('----------------------------------------------')
arr = np.ceil([-3.1666, 3.6667]) #the upper/ceil value of -3.166 is -3, and for 3.6667 is 4
print(arr)






