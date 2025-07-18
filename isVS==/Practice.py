# both are comparison operators comapring objects
# == compares 2 values, and is compares two exact locations in a memory
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True # same value
print(a is b) # False # diff locations
print(a is a) # True
# BUT
c = 4
d = 4
print(c == d) # True
print(c is d) # True # bcz both have a value of 4 (constant)
# so python will not waste any other memory location for d
# this applies for immutable objects
# for tuple if a b have same values, a is b is true # immutable
# for string if a b have same values, a is b is true # immutable
# for list if a b have same values, a is b is false # mutable
e = None
f = None
print(e == f) # True
print(e is f) # True
print(e is None) # true 
# None is also considered immutable