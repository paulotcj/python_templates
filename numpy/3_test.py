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