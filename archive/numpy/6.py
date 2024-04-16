import numpy as np


#will generate an array of numbers from 1 to 11. The steps are around 0.2
x = np.linspace(1,11)
print(x)
print(len(x))

print('----------------------------------------------')

#generate an array with numbers ranging from 1 to 10. With 10 elements
x = np.linspace(1,10,10)
print(x)
print(len(x))

print('----------------------------------------------')

#generate an array with numbers ranging from 1 to 10. With 10 elements
# and reshape with 5 rows of 2 columns
x = np.linspace(1,10,10).reshape(5,2)
print(x)
print(len(x))

print('----------------------------------------------')

x = np.linspace(1,10,10) * 10
print(x)

print('----------------------------------------------')

x = np.array([[0,5,155,0,518],[0, 1870,616,317,325]])
y = x[ (x == 155) | (x > 500) ]
print(x)
print(y)