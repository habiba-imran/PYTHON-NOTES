# UNIVERSAL FUNCTIONS
import numpy as np
arr1 = np.array([1, 4, 9, 16, 20])
print(np.sqrt(arr1)) # [1. 2. 3. 4. 4.47213595]
print(np.exp(arr1)) # prints e^(element in arr1) where 3 = 2.718...
print(np.sin(arr1)) # prints sin of every element in arr1

# INDEXING AND SLICING
print(arr1[0:3]) # 1 4 9
print(arr1[-4: -1]) # gives 4, 9, 16
print(arr1[-1:-4]) # prints []
# but if add a step value of -1, it will correctly give us an array
print(arr1[-1:-4:-1]) # gives 20, 16, 9
print(arr1[::-1]) # reverses the array

# MULTI-DIMENSIONAL SLICING
arr2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12] ])
# arr2d[row_slice, column_slice]
print(arr2d[0:2, 1:3]) # [[2 3], [6 7]]
print(arr2d[:, 1:3]) # all rows, but col 1 and col 2 # [[ 2  3], [ 6  7], [10 11]]
print(arr2d[::2, ::2]) # every 2nd row and every 2nd col # [[ 1  3], [ 9 11]]

# INDEXED ARRAYS: ADVANCED INDEXING
# np.take: to perform slicing and indexing:
arr1 = np.array([1, 4, 9, 16, 20])
idx = [0, 2]
print(np.take(arr1, idx)) # prints 1, 9

arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])  # [10 30 50]

arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Select specific rows
print(arr2d[[0, 2]])  # [[1 2 3], [7 8 9]]

# Select specific elements from each row
print(arr2d[[0, 1, 2], [2, 0, 1]])  # [3 4 8]

arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
print(mask)         # [False False  True  True  True]
print(arr[mask])    # [30 40 50]

# nditer
for x in np.nditer(arr): # loops irrespective of the dimension
    print(x, end = " ") # 10 20 30 40 50

# ndenumerate
for idx, x in np.ndenumerate(arr):
    print(idx, x) # prints index alongwith the value


    


