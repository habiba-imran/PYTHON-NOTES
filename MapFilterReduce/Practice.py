# -----MAP-----
def cube(x):
    return x * x * x
# to find cube of all items in a list:
list1 = [1, 2, 3, 4, 5, 6]
newl = []
for item in list1:
    newl.append(cube(item))
print(newl)
# to make it short, we use map:
newl = list(map(cube, list1)) # without list, it will return address
print(newl)
newl = list(map(lambda x: x * x * x, list1))
print(newl)
# -----FILTER-----
def filterfunction(a):
    return a > 2
newnewl = list(filter(filterfunction, list1))
print(newnewl)
# or
newnewnewl = list(filter(lambda x: x > 3, list1))
print(newnewnewl)
# -----REDUCE-----
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
# takes 1+2 adds them = 3, then 3+4 = 7 and so on
# we are reducing the list, 1 and 2 is reduced to 3


