# DATA TYPES: for the numpy array, all elements should have same data type
import numpy as np
arr1 = np.array([1, 2, 3, 4.1]) # all converted to float
print(arr1) # [1.  2.  3.  4.1]
print(arr1.dtype) # float64

arr2 = np.array([1, 2, "habiba"]) # all converted to string
print(arr2) # ['1' '2' 'habiba']
print(arr2.dtype) # <U21
# U → means Unicode string.
# 21 → maximum number of characters per element

arr3 = np.array([1, 2, 3], dtype = np.float64)
print(arr3) # [1. 2. 3.]

arr4 = np.array([1, 2.2, "habiba", True], dtype = object)
print(arr4) # [1 2.2 'habiba' True]
print(arr4.dtype) # object

# TYPE CASTING:
arr3 = np.array([1, 2, 3])
new_arr = arr3.astype(np.float64)
print(new_arr)

# TYPE CASTING ERRORS
arr4 = np.array(["1", "2", "hello"])
# new_arr4 = arr4.astype(np.int64)
# print(new_arr4), it will give us an error


