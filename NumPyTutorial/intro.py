import numpy as np 
arraynp = np.array([1, 2, 3, 4, 5])
print(arraynp * 2) # [ 2  4  6  8 10]
list1 = [1, 2, 3, 4, 5]
print(list1 * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# numpy provides direct operations as seen here, for multiplying with 2, called vectorization
for i in list1:
    print(i * 2, end = " ") # gives: 2 4 6 8 10
# but for the list we have to loop through every element
# that's a difference between a list and a numpy array
# furthermore, numpy arrays are faster as compared to lists
# numpy is built on C, which is a low level language
# and takes less time as compared to python lists
# numpy is also memory efficient
# for a numpy array, all elements should have same data type unlike list
# if we keep diff data type elements into a numpy array, all are converted to string
print("\n", arraynp.ndim) # prints 1
print(arraynp.shape) # prints 5 indicating num of rows - cols, 5 rows only here
# for a single number, direction is 0
arr = np.array(32)
print(arr.ndim) # prinst 0
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.ndim)
print(arr2.shape) # prinst 2, 3, means 2 rows and 3 cols




