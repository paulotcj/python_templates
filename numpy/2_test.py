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