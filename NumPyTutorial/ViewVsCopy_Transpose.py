# VIEW: original array is going to be changed
# COPY: creates a copy, no changes in original array
import numpy as np
# VIEW
arr = np.array([1, 2, 3, 4, 5])
view_arr = arr[0: 3]
print(view_arr) # prints 1, 2, 3
view_arr[0] = 100
print(view_arr) # prints 100, 2, 3
print(arr) # prints 100, 2, 3, 4, 5 
# the original array has also been changed

# COPY
arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr[0:3].copy()
print(copy_arr) # prints 1, 2, 3
copy_arr[0] = 100
print(copy_arr) # prints 100 2 3
print(arr) # prints 1, 2, 3, 4, 5

# TRANSPOSE
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.transpose()) # prints the transpose

# SWAPAXES: use to swap dimensions of an array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Original:\n", arr)
print("Shape:", arr.shape) # prinst 2, 3
swapped = np.swapaxes(arr, 0, 1) # 0->2, 1->3 in shape of original array
print("\nSwapped:\n", swapped)
print("Shape:", swapped.shape) # prints 2, 3
# array was initially 2 rows 3 cols
# after swapping it became 3 row 2 col
# can also be performed for 3d array




