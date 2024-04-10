import numpy as np

print('----------------------------------------------')

arr = np.array([1,2,3])

for filter_arr in arr:
    print(filter_arr)
    
print('----------------------------------------------') 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 

for filter_arr in arr:
    print(filter_arr)
    
print('-----') 

for filter_arr in arr:
    for y in filter_arr:
        print(y)
       
print('----------------------------------------------')       
arr = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]
    ])
for filter_arr in arr:
    print(filter_arr)
print('-----') 

for filter_arr in arr:
    for y in filter_arr:
        print(y)
print('-----')
for filter_arr in arr:
    for y in filter_arr:
        for z in y:
            print(z)
            

print('----------------------------------------------') 

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])   
print(f'number of dimensions: {arr.ndim}')      

for filter_arr in np.nditer(arr):
    print(filter_arr)   
    
print('----------------------------------------------') 
arr = np.array([1, 2, 3])    

for filter_arr in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(filter_arr)
    
print('----------------------------------------------') 

arr = np.array([1,2,3,'A'])

print(arr)


print('----------------------------------------------') 
arr = np.array([1,2,3,4,5,6,7,8])

for filter_arr in np.nditer(arr[::2]):
    print(filter_arr)

print('----------------------------------------------') 
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

for filter_arr in np.nditer(arr[::,::2]):
    print(filter_arr)


print('----------------------------------------------') 
arr = np.arange(1,28).reshape(3,3,3) # 3X3X3
print(arr)
print('-----')
# arr[::2] -> since we have a 3x3x3, we would pring [1]x3x3 and [2]x3x3
# arr[::,::2] -> would print [0]x[0]x?, [0]x[2]x? ; [1]x[0]x?, [1]x[2]x? ; [2]x[0]x?, [2]x[2]x?
# arr[::,::,::2] -> would print [0]x[0]x[0], [0]x[0]x[2]; [0]x[1]x[0], [0]x[1]x[2]; [0]x[2]x[0], [0]x[2]x[2] ...
for filter_arr in np.nditer(arr[::,::,::2]):
    print(filter_arr)

print('----------------------------------------------') 
arr = np.arange(1,28).reshape(3,3,3)
for idx, filter_arr in np.ndenumerate(arr):
  print(idx, filter_arr)

print('-----')
for idx, filter_arr in np.ndenumerate(arr):
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
arr_2 = np.array_split(arr, 3)
for filter_arr in arr_2:
    print(filter_arr)
    print('-----')


print('----------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

arr_2 = np.array_split(arr, 3)

for filter_arr in arr_2:
    print(filter_arr)
    print('-----')

print('----------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr_2 = np.array_split(arr, 3, axis=1)
for filter_arr in arr_2:
    print(filter_arr)
    print('-----')

print('----------------------------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr_2 = np.hsplit(arr, 3)
for filter_arr in arr_2:
    print(filter_arr)
    print('-----')

print('----------------------------------------------')

#               0  1  2  3  4  5  6
arr = np.array([1, 2, 3, 4, 5, 4, 4])

result = np.where(arr == 4)
print(type(result))
print(result)
print('-----')
print('each of the results below should be 4')
for filter_arr in result: #x is a tuple containing an array with the indexes where arr == 4
    for y in filter_arr: #y is the actual element in the array
        print(arr[y])

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result = np.where(arr%2 == 0)
print(result)
for filter_arr in result:
    for y in filter_arr:
        print(arr[y])

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result = np.where(arr%2 == 1)
print(result)
for filter_arr in result: 
    for y in filter_arr: print(arr[y])

print('----------------------------------------------')

#               0  1  2  3  
arr = np.array([6, 7, 8, 9])

filter_arr = np.searchsorted(arr, 7)
print(filter_arr)

filter_arr = np.searchsorted(arr, 7.5)
print(filter_arr)

filter_arr = np.searchsorted(arr, 8)
print(filter_arr)


filter_arr = np.searchsorted(arr, 8.5)
print(filter_arr)

print('----------------------------------------------')

arr = np.array([6, 7, 8, 9])

filter_arr = np.searchsorted(arr, 7)
print(filter_arr)

filter_arr = np.searchsorted(arr, 7, side='right')
print(filter_arr)

print('----------------------------------------------')

#               0  1  2  3
arr = np.array([1, 3, 5, 7])

filter_arr = np.searchsorted(arr, [2, 4, 6])

print(filter_arr)


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

print('----------------------------------------------')
arr = np.array([[3, 2, 4], [5, 0, 1]]) #the arrays itself won't be sorted, but its content will

print(np.sort(arr))  #exspected output: [[2 3 4] [0 1 5]]

print('----------------------------------------------')

#               0   1   2   3
arr = np.array([41, 42, 43, 44])

#    0     1      2     3
filter_arr = [True, False, True, False] #we will select 41 and 43

arr_2 = arr[filter_arr]
print(type(filter_arr))
print(filter_arr)
print('-----')
print(type(arr_2))
print(arr_2)

print('----------------------------------------------')

#               0 1 2 3 4 5
arr = np.array([1,2,3,4,5,6])
filter_arr = [2,4]
arr_2 = arr[filter_arr]
print(arr_2) #expected [3,5]

print('----------------------------------------------')
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

arr_2 = arr[filter_arr] #we should see 43 and 44

print(filter_arr)
print(arr_2)

print('----------------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr] # we should see 2, 4, 6

print(filter_arr)
print(newarr)

print('----------------------------------------------')

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42
print(filter_arr)
print('-----')

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print('----------------------------------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr] # we should see 2, 4, 6

print(filter_arr)
print(newarr)