import numpy

arr = numpy.array([1,2,3,4,5])

print(arr)

print('----------------------------------------------')

import numpy as np
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

arr = np.array([1, 2, 3, 4])
print(arr[1])

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4])
print(arr[1] + arr[2])

print('----------------------------------------------')

#               r:0| 0 1 2 3 4  r:1| 0 1 2 3 4
arr = np.array([   [ 1,2,3,4,5],   [ 6,7,8,9,10]])
#                                        ^
print(f'Row 1 element 2 : {arr[1,2]}')
print('----------------------------------------------')

arr = np.array([
        [ #0,x,x
            [1, 2, 3], #0,0,x
            [4, 5, 6]  #0,1,x
        ], 
        [ #1,x,x
            [7, 8, 9],    #1,0,x
            [10, 11, 12]  #1,1,x
        ]
    ])

print(arr[0,0,1]) #2
print(arr[0,1,2]) #6
print(arr[1,1,2]) #12

print('----------------------------------------------')

arr = np.array(
    [
        [1,2,3,4,5],
        [6,7,8,9,10]
     ])
print(f'The last element from the 2 dim array is {arr[1,-1]}')

print(f'The last element from the 2 dim array is {arr[-1,-1]}')

print(f'3rd element of the last array {arr[-1,2]}')


print('----------------------------------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7])

result = arr[1:5]
print(result)


print('----------------------------------------------')
arr = np.array([[1, 2, 3, 4, 5, 6, 7],[8,9,10,11,12,13,14]])

result = arr[1,1:5]
print(result)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7])
result = arr[4:]
print(result)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7])
result = arr[:4]
print(result)


print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# from begiing to end -> that means beginning at -3 and ending at -1
#  so it starts at 5 and end at 6
# Slice from the index 3 from the end to index 1 from the end
result = arr[-3:-1]

print(result)


print('----------------------------------------------')

#               0  1  2  3  4  5  6
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#                  |--------|--x idx 5 is not included
result = arr[1:5] # 5 idx is not included

print(result)
print(type(result))
print('----------------------------------------------')

#               0  1  2  3  4  5  6
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#                  |--------|--x idx 5 is not included
# since the step is 2, we would see 2 and 4 as results
result = arr[1:5:2]

print(result)


print('----------------------------------------------')

#                  jump 2
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#               ^     ^     ^     ^
result = arr[::2]
print(result)


print('----------------------------------------------')
arr = np.array(
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10]
        #   |-----|---x
     ])

result = arr[1, 1:4]

print(result)
print('----------------------------------------------')


arr = np.array(
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10]
    ])

# from arrays 0 to 1 (2 not included), get the element at index 2
result = arr[0:2, 2]
print(result) # [3 8]


print('----------------------------------------------')

arr = np.array(
    [
        #0  1  2  3  4
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10]
    ])

# from arrays 0 to 1 (2 not included), get the element at index from 1 to 3 (4 not included)
result = arr[0:2, 1:4] #[2,3,4] [7,8,9] , will this be a single array???? nope!

print(arr[0:2, 1:4])

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4])

result = arr.dtype

print(result)

print('----------------------------------------------')
arr = np.array(['apple', 'banana', 'cherry'])

result = arr.dtype

print(result)

print('----------------------------------------------')
arr = np.array([1, 2, 3, 4], dtype='S')
result = arr.dtype

print(result)


print('----------------------------------------------')
arr = np.array([1, 2, 3, 4], dtype='i4') #integer with 4 bytes
# 4 bytes = 4 * 8 bits = 32 bits

result = arr.dtype
print(result)

print('----------------------------------------------')

# arr = np.array(['a', '2', '3'], dtype='i') #integer

# result = arr.dtype
# print(result)

# print('----------------------------------------------')


arr = np.array([1.1, 2.1, 3.1])

new_arr = arr.astype('i')

print(new_arr)
print(new_arr.dtype)

print('----------------------------------------------')


arr = np.array([1.1, 2.1, 3.1])

new_arr = arr.astype(int)

print(new_arr)
print(new_arr.dtype)


print('----------------------------------------------')


arr = np.array([1.1, 2.1, 3.1, 0])

new_arr = arr.astype(bool)

print(new_arr)
print(new_arr.dtype)


print('----------------------------------------------')

arr = np.array([1,2,3,4,5])
arr_copy = arr.copy()


arr[0] = 42

print(arr)
print(arr_copy)

print('----------------------------------------------')


arr = np.array([1, 2, 3, 4, 5])
arr_view = arr.view()
arr_view_2 = arr

arr[0] = 42


print(arr)
print(arr_view)
print(arr_view_2)


print('----------------------------------------------')


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
w = arr

print(f'x.base: {x.base}')
print(f'y.base: {y.base}')
print(f'w.base: {w.base}')


print('----------------------------------------------')

arr = np.array(
    [
        [1, 2, 3, 4], 
        [5, 6, 7, 8]
     ])

print(arr.ndim)
print(arr.shape)

print('----------------------------------------------')

arr = np.array([1,2,3,4], ndmin= 5)

print(arr.ndim)
print(arr.shape)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(4, 3)
print(new_arr)
print('---')
new_arr = arr.reshape(3,4)
print(new_arr)

print('----------------------------------------------')


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(2,3,2)

print(new_arr)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = arr.reshape(2, 4)
print(new_arr.base) #returns view

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2,4)
print(new_arr)
print('---')
new_arr = arr.reshape(2,-1)
print(new_arr)
print('---')
new_arr = arr.reshape(2, 2, -1)
print(new_arr)
print('---')
# new_arr = arr.reshape(2, -1, -1)
# print(new_arr)
print('----------------------------------------------')

arr = np.array(
    [
        [1, 2, 3], 
        [4, 5, 6],
        [2, 1, 0]
     ])

new_arr = arr.reshape(-1)

print(new_arr)

print('----------------------------------------------')

arr = np.array(
    [
        [1, 2, 3], 
        [4, 5, 6],
        [2, 1, 0]
     ])
new_array = arr.flatten()
print(new_array)

print('----------------------------------------------')

arr = np.array([[1,2,3], [4,5,6]])

new_arr1 = arr.flatten('F')
new_arr2 = arr.flatten()
new_arr3 = arr.flatten('C')

print(new_arr1)
print(new_arr2)
print(new_arr3)

print('----------------------------------------------')
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])


concatenated_array = np.concatenate((arr1.flatten(), arr2.flatten()))

print(arr1)
print(arr2)
print(concatenated_array)

print('----------------------------------------------')

arr = np.array([[1, 2, 3],
                           [4, 5, 6]])

arr_zeros = np.zeros_like(arr)

print(arr_zeros)

arr_flatten_zeroes = np.zeros_like(arr.flatten())
print(arr_flatten_zeroes)   