import numpy as np

print('----------------------------------------------')

arr = np.array([1,2,3])

for x in arr:
    print(x)
    
print('----------------------------------------------') 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 

for x in arr:
    print(x)
    
print('-----') 

for x in arr:
    for y in x:
        print(y)
       
print('----------------------------------------------')       
arr = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]
    ])
for x in arr:
    print(x)
print('-----') 

for x in arr:
    for y in x:
        print(y)
print('-----')
for x in arr:
    for y in x:
        for z in y:
            print(z)
            

print('----------------------------------------------') 

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])   
print(f'number of dimensions: {arr.ndim}')      

for x in np.nditer(arr):
    print(x)   
    
print('----------------------------------------------') 
arr = np.array([1, 2, 3])    

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
    
print('----------------------------------------------') 

arr = np.array([1,2,3,'A'])

print(arr)


print('----------------------------------------------') 
arr = np.array([1,2,3,4,5,6,7,8])

for x in np.nditer(arr[::2]):
    print(x)

print('----------------------------------------------') 
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

for x in np.nditer(arr[::,::2]):
    print(x)


print('----------------------------------------------') 
arr = np.arange(1,28).reshape(3,3,3) # 3X3X3
print(arr)
print('-----')
# arr[::2] -> since we have a 3x3x3, we would pring [1]x3x3 and [2]x3x3
# arr[::,::2] -> would print [0]x[0]x?, [0]x[2]x? ; [1]x[0]x?, [1]x[2]x? ; [2]x[0]x?, [2]x[2]x?
# arr[::,::,::2] -> would print [0]x[0]x[0], [0]x[0]x[2]; [0]x[1]x[0], [0]x[1]x[2]; [0]x[2]x[0], [0]x[2]x[2] ...
for x in np.nditer(arr[::,::,::2]):
    print(x)

print('----------------------------------------------') 
arr = np.arange(1,28).reshape(3,3,3)
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print('-----')
for idx, x in np.ndenumerate(arr):
  print(arr[idx])

print('----------------------------------------------') 

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

print('----------------------------------------------') 

arr1 = np.arange(1,5).reshape(2,2)

arr2 = np.arange(5,9).reshape(2,2)
print(arr1)
print(arr2)
print('-----')
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print('-----')
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)


print('----------------------------------------------')


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis = 1)
print(arr)
print('-----')
arr = np.stack((arr1, arr2), axis = 0)
print(arr)

print('----------------------------------------------')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1,arr2))

print(arr)
print('----------------------------------------------')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))


print(arr)

print('----------------------------------------------')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1,arr2))

print(arr)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6])

arr1 = np.array_split(arr, 3)
print(arr1)
print(type(arr1))

print('----------------------------------------------')
arr = np.array([1, 2, 3, 4, 5, 6])

arr1 = np.array_split(arr, 5)
print(arr1)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6])
arr1 = np.array_split(arr, 3)
print(arr1)
print(arr1[0])
print(arr1[1])
print(arr1[2])


print('----------------------------------------------')
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(f'num dimensions of arr: {arr.ndim}')
newarr = np.array_split(arr, 3)
for x in newarr:
    print(x)
    print('-----')


print('----------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

for x in newarr:
    print(x)
    print('-----')

print('----------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
for x in newarr:
    print(x)
    print('-----')

print('----------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
for x in newarr:
    print(x)
    print('-----')

print('----------------------------------------------')

#               0  1  2  3  4  5  6
arr = np.array([1, 2, 3, 4, 5, 4, 4])

result = np.where(arr == 4)
print(type(result))
print(result)
print('-----')
print('each of the results below should be 4')
for x in result: #x is a tuple containing an array with the indexes where arr == 4
    for y in x: #y is the actual element in the array
        print(arr[y])

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result = np.where(arr%2 == 0)
print(result)
for x in result:
    for y in x:
        print(arr[y])

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result = np.where(arr%2 == 1)
print(result)
for x in result: 
    for y in x: print(arr[y])

print('----------------------------------------------')

#               0  1  2  3  
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
print(x)

x = np.searchsorted(arr, 7.5)
print(x)

x = np.searchsorted(arr, 8)
print(x)


x = np.searchsorted(arr, 8.5)
print(x)

print('----------------------------------------------')

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
print(x)

x = np.searchsorted(arr, 7, side='right')
print(x)

print('----------------------------------------------')

#               0  1  2  3
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)


print('----------------------------------------------')

arr = np.array([3, 2, 0, 1])
sorted_asc = np.sort(arr)
sorted_desc = np.sort(arr)[::-1]
print(arr)
print(sorted_asc)
print(sorted_desc)

print('----------------------------------------------')
arr = np.array(['banana', 'cherry', 'apple', 'aa', 'a', 'aab'])

print(np.sort(arr))

print('----------------------------------------------')

arr = np.array([True, False, True]) #false can be considered 0 and true = 1, so we should see False, True, True

print(np.sort(arr))
