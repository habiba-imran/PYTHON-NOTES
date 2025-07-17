# lambda functions are like expressions
# def double(x):
#     return (2 * x)
# instead of this: we can also write:
double = lambda x: (x * 2) 
# function name = lambda arguments it takes: return statement
print(double(5))
# lambda functions are used for single expression functions
avg = lambda x, y: (x + y) / 2
print(avg(5, 10))
# we can also give function as an argument to another function
def hello(fx, value):
    return 2 + fx(value) # 2 + double(4)
print(hello(double, 4)) # prints 10
# or
print(hello(lambda x: x*2, 6))  # prints 14
# therefore lambda functions are also called anonymous functions

