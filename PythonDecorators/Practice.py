# A decorator is just a function that takes another function as input, adds some functionality, and returns it.
def decorator_func(fx):
    def modified_fx():
        print("before the function")
        fx()
        print("after the function")
    return modified_fx
@decorator_func
def original_func():
    print("the original fuction")

original_func()
# it is short for: original_func = decorator_func(original_func) 
# ordecorator_func(original_func)()
print("\n")
# -----PRACTICAL USE-CASE-----logging
def extra_func(fx):
    def mfx(*args, **kwargs): # args allow to pass arguments as tuple
        print("befor") # kwargs allow to pass arguments as dictionary
        fx(*args, **kwargs)
        print("after")
    return mfx
@extra_func
def add(a, b):
    print(a + b)
    return a + b
(add(1, 2))



