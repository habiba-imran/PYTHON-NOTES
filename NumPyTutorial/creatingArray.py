import numpy as np
import random

# we can use range using arange as follows:
arr = np.arange(1, 100, 2) # 1 to 99 with step = 2
print(arr)

# or using linspace
arr2 = np.linspace(0, 1, 5) # 5 values printed between 0 and 1
print(arr2) # prints [0.   0.25 0.5  0.75 1.  ]

# or using logspace: logrithmic space array
arr3 = np.logspace(1, 3, 3) # 10^1 to 10^3 and only 3 values 
print(arr3) # prints: [  10.  100. 1000.]

# or using zeros
arr4 = np.zeros(5)
print(arr4) # prints [0. 0. 0. 0. 0.]
arr5 = np.zeros([2, 3]) # creates 2d arr with 2 ros and 3 cols
print(arr5) # prints [[0. 0. 0.] [0. 0. 0.]]
 
# or using ones
arr6 = np.ones(5, dtype = int) # by default data type is float
print(arr6) # [1 1 1 1 1]

# creating an array with same values:
arr7 = np.full(10, 7)
print(arr7) # [7 7 7 7 7 7 7 7 7 7]
arr8 = np.full([2, 3], 7)
print(arr8) # 2 by 3 array with all values = 7

# to create uninitialized array:
arr9 = np.empty([2, 3]) # pass 1 number for 1 d
print(arr9) # prints garbage values 2 rows - 3 cols

# random numbers
arr9 = np.random.rand(2, 3) # for 1d pass a single number
print(arr9) # prints 2d array with random values

arr10 = np.random.randn(10) # produce 10 values with mean = 0 and SD = 1
print(arr10) # for 2d pass (2, 3) without []

arr11 = np.random.randint(10, 100)
print(arr11) # prints any random int number between 10 and 100
arr13 = np.random.randint(10, 100, size = (2, 3)) # start, stop, dimension/number of elements
print(arr13)
arr14 = np.random.randint(10, 100, 2)
print(arr14) # prints 2 random numbers between 10 and 100

