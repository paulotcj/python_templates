import numpy

arr = numpy.array([1,2,3,4,5])

print(arr)

print('----------------------------------------------')

import numpy as np

arr2 = np.array([1,2,3,4,5])
print(arr2) 

print('----------------------------------------------')

print(np.__version__)

print('----------------------------------------------')

arr3 = np.array([1,2,3,4,5])
print(arr3)
print(type(arr3))


print('----------------------------------------------')

arr4 = np.array((1,2,3,4,5))
print(arr4)
print('----------------------------------------------')

arr5 = np.array(42)
print(arr5)
print('----------------------------------------------')
arr6 = np.array([[1,2,3],[4,5,6]])
print(arr6)
print('----------------------------------------------')
arr7 = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6]
        ], 
        [
            [1, 2, 3], 
            [4, 5, 6]
        ]
    ])

print(arr)

print('----------------------------------------------')

a = np.array(42) # 0D array, or scalar
b = np.array([1, 2, 3, 4, 5]) # 1D array
c = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
d = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6]
        ], 
        [
            [1, 2, 3], 
            [4, 5, 6]
        ]
    ]) # 3D array

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


print('----------------------------------------------')

arr = np.array([1, 2, 3, 4])
print(f'number of dimensions: {arr.ndim}' )
print('----')
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(f'number of dimensions: {arr.ndim}' )

print('----------------------------------------------')