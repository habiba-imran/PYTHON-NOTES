# Concatenation: joining mutiple arrays
import numpy as np
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate((a, b))) # [1 2 3 4]

# to vertically stack two arrays in form of rows:
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
             [7, 8]])
result = np.vstack((a, b))
print(result)
# [[1 2] 
# [3 4]
# [5 6]
# [7 8]]

# hstack:
result = np.hstack((a, b))
print(result)
# [[1 2 5 6]
# [3 4 7 8]]

# stack:
print(np.stack((a, b), axis=0)) # axis = 0, row wise, axis = 1, col wise
# [[[1 2] 
# [3 4]]
#  [[5 6] 
# [7 8]]]

