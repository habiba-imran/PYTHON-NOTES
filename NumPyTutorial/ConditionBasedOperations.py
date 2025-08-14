# Conditional based operations:
import numpy as np
arr = np.array([10, 15, 20, 25, 30])

# where, condition, statement if true, if false
print(np.where(arr % 10 == 0, "divisible", "not divisble"))
# ['divisible' 'not divisble' 'divisible' 'not divisble' 'divisible']

# argwhere: returns a stacked 2D array of indices
print(np.argwhere(arr % 10 == 0)) # [[0] [2] [4]]

# logical_and and or
print(np.logical_and(arr > 15, arr < 25)) # [False False  True False False]
print(np.logical_or(arr > 15, arr < 25)) # [ True  True  True  True  True]

# for 2d:
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.argwhere(arr1 > 2))
# [[0 2] # condition satisfied for element at row 0 and col 2
#  [1 0] # same
#  [1 1]
#  [1 2]]


