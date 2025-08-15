# JOINS AND MERGES
# Joins: inner, outer, left, right
# join is used where e.g., we have to join two sheets of same information
# e.g., sheet 1 has info about interior of a house, sheet 2 has info about exterior
# inner: Keeps only coomon cols in both DataFrames.
# left:	Keeps all rows from the left DataFrame only, ignoreing common, A - B
# right: B - A
# outer: Keeps all rows from both DataFrames, filling missing values with NaN.

# IN MERGE: keeps the common col as for one and other cols in both data sheets
import pandas as pd

# First dictionary → df1
data1 = {
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
    "Age": [28, 25, 30, 27]
}
# Second dictionary → df2
data2 = {
    "ID": [3, 4, 5, 6],
    "Department": ["Finance", "Marketing", "IT", "HR"],
    "Salary": [55000, 60000, 58000, 50000]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("DataFrame 1:\n", df1, "\n")
print("DataFrame 2:\n", df2)

print(pd.concat((df1, df2))) # Nan is appeared where a col does not match other sheet
#    ID    Name   Age Department   Salary
# 0   1     Ali  28.0        NaN      NaN
# 1   2    Sara  25.0        NaN      NaN
# 2   3   Ahmed  30.0        NaN      NaN
# 3   4  Fatima  27.0        NaN      NaN
# 0   3     NaN   NaN    Finance  55000.0
# 1   4     NaN   NaN  Marketing  60000.0
# 2   5     NaN   NaN         IT  58000.0
# 3   6     NaN   NaN         HR  50000.0
print(pd.concat([df1, df2], axis = 1))
#    ID    Name  Age  ID Department  Salary
# 0   1     Ali   28   3    Finance   55000
# 1   2    Sara   25   4  Marketing   60000
# 2   3   Ahmed   30   5         IT   58000
# 3   4  Fatima   27   6         HR   50000
print("MERGED BSED ON COL ID: \n", pd.merge(df1, df2, on = "ID"))
# based on ID, where it was same in both sheets
#     ID    Name  Age Department  Salary
# 0   3   Ahmed   30    Finance   55000
# 1   4  Fatima   27  Marketing   60000


