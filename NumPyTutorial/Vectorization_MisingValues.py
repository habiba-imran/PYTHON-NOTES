import numpy as np
# VECTORIZATION
# np.vectorize lets you take a scalar function and apply it element-wise to arrays:
# only to be used when you want to apply a custom function to arrays
def my_func(x, y):
    return x * y + 2
vec_func = np.vectorize(my_func)
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(vec_func(a, b))  # [12 42 92]

# DEALING WITH MISSING VALUES
# np.nan: not a number
# np.inf and -np.inf: positive and negative infinity values: apear where division/0 or overflow situation
a = np.array([1, -np.inf, 3, np.inf, 5, np.nan])
print(a) # [  1. -inf   3.  inf   5.  nan]

# np.isnan, np.isinf, np.isfinite
print(np.isinf(a)) # [False  True False  True False False]
print(np.isfinite(a)) # [ True False  True False  True False]
print(np.isnan(a)) # [False False False False False  True]
# we can also use logical_and and or for getting boolean values for any 2 functions
new_arr = np.nan_to_num(a)
print(new_arr) # all nan values are changed to 0
# [ 1.00000000e+000 -1.79769313e+308  3.00000000e+000  1.79769313e+308 5.00000000e+000  0.00000000e+000]

