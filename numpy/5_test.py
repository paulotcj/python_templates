import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

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

# print('----------------------------------------------')

# x = 
# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

# plt.show()