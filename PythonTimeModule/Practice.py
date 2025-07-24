import time
print(time.time())  # Prints time from 1st Jan, 1970 in seconds
def usingWhile():
    i = 0
    while i < 50001:
        i = i + 1
def usingFor():
    for j in range(50001):
        pass
# Measure time for for-loop
init = time.time()
usingFor()
ForTime = time.time() - init
# Measure time for while-loop
init = time.time()
usingWhile()
WhileTime = time.time() - init
print("For loop time is: ", ForTime)
print("While loop time is: ", WhileTime)
# For loop time is:  0.009884119033813477
# While loop time is:  0.027620792388916016

print("hi")
time.sleep(2)
print("This is printed after 2 seconds")

t = time.localtime() # gives local time as
# time.struct_time(tm_year=2025, tm_mon=7, tm_mday=24, tm_hour=17, 
# tm_min=33, tm_sec=40, tm_wday=3, tm_yday=205, tm_isdst=0)
formatted_time = time.strftime('%Y-%m-%d') # prints year-month-date
print(formatted_time)
formatted_time = time.strftime("%H-%M-%S") # prints hour, minute second
print(formatted_time)




