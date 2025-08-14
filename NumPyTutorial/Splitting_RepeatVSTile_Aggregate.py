# split
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]]) # (array, parts in which you want to split)
print(np.split(arr, 2)) # [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]])]
print(np.split(arr, 4)) # [array([[1, 2]]), array([[3, 4]]), array([[5, 6]]), array([[7, 8]])]
# print(np.split(arr, 3)) # generates an error coz, equal division can't happen

# repeat
print(np.repeat(arr, 2)) # [1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8], every element gets repeated 2 times

# tile
print(np.tile(arr, 2)) # repeats whole array twice
# [[1 2 1 2] [3 4 3 4] [5 6 5 6] [7 8 7 8]]

# aggregate: used to summarize, total, average, max, min etc
arr = np.array([10, 20, 30, 40, 50])
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr)) # standard deviation
print(np.var(arr)) # variance: sq of std
print(np.mean(arr))

# for 2d:
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]]) 
# to sum sum accross col only, axis = 1
print(np.sum(arr, axis = 1)) # [ 3  7 11 15]

# cummulative sum
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(np.cumsum(arr)) # [ 1  3  6 10 15 21 28]
# peoduct
print(np.cumprod(arr)) # [   1    2    6   24  120  720 5040]
