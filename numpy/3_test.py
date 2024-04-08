import numpy as np
from numpy import random


for _ in range(10):
    print(random.randint(100))

print('----------------------------------------------')

for _ in range(10):
    print( random.rand())

print('----------------------------------------------')

rand_arr = random.randint(100, size=(5))
print(rand_arr)

print('----------------------------------------------')
x = random.randint(100, size=(3, 5)) # 3rows, 5 elements in each

print(x)

print('----------------------------------------------')
x = random.rand(5)
print(x)

print('----------------------------------------------')

arr = [3, 5, 7, 9]
x = random.choice(arr) #chose one from the array

print(x)

print('----------------------------------------------')
#from the array sample, choose 100 elements, each element has a different probability, for instance 9 has 0% probability
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) #note the sum of all probabilities should be 1

print(x)

# x = random.choice([3, 5, 7, 9], p=[0.1, 0.2, 0.2, 0.0], size=(100)) #ERROR

# print(x)

print('----------------------------------------------')


x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) #3 rows, 5 elements

print(x)

print('----------------------------------------------')


arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)


print(arr)

