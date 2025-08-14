# Creating a 2d numpy aray:
import numpy as np
arr1 = np.array([[1, 2, 3], 
                [4, 5, 8]])
print(arr1.ndim) # prints 2
print(arr1.shape) # prints (2, 3), 2 rows 3 cols
print(arr1.size) # prints 6, total no of elements
print(arr1.itemsize) # prints 8, maximum bytes taken by any element

# we can also reshape the 2-3 array tp 3-2 array
reshaped = arr1.reshape(3, 2)
print(reshaped) # [[1 2], [3 4], [5 8]]
reshaped2 = arr1.reshape(6) # 2d converted to 1d 
print(reshaped2) # [1 2 3 4 5 8]
print("\n")

# or we can use ravel or flatten to convert any dimension to 1d
newarr = arr1.flatten()
print(newarr) # [1 2 3 4 5 8]
newarr[0] = 100 
print(arr1) # [[1 2 3], [4 5 8]] # hence flatten does not modify original array
newarr = arr1.ravel()
print(newarr) # [1 2 3 4 5 8]
newarr[0] = 100 # modifications in ravel changes the original array
print(arr1) # [[100 2 3], [4 5 8]]



