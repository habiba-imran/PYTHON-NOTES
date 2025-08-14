# TYPES OF DATA STRICTURES:
# 1. series: 1d, only one col and n rows
#       series is a homogenous datatype,
#       all entries in col should have same data type, if one string, other int, all will be treated as string
#       sizeimmutable: we can not delete a row, we can remove it explicitly 
#       by creating another variable stroing new dataset, with the specified col removed
#       same for addition of a row
import pandas as pd
s = pd.Series([10, 20, 30, 40, 50])
print(s) # printed alongwith an index, index always starts with 0
print(s.dtype) # prints int64
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
s1 = pd.Series([10, 20, 30, 40, "habiba"])
print(s1)
print(s1.dtype) # prints object

print(s.values) # [10 20 30 40 50]
print(s.index) # prints RangeIndex(start=0, stop=5, step=1)
print(s.name) # prints header, rn prints None, because there is no name assigned
s.name = "numbers"
print(s.name, "\n") # numbers
print(s) # series printed with numbers as name

# 2. dataframe: 2d, multiple columns and rows
#       heterogenous structure, multiple data types in a single col
#       size mutable: we can easily add or delete a row or col

w