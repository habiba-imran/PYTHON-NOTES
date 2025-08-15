# INDEXING IN PANDAS FOR SERIES
import pandas as pd
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1[0]) # same as of python and numpy # prints 10
print(s1[0:2]) # prints 0    10    1    20 # indices with their values

# iloc: location based indexing # works for NUMERICAL INDEXES   
print(s1.iloc[0]) # prints 10
print(s1.iloc[[0, 1 ,2]]) # prints indices with their values at idx 0, 1, 2
# rn indicing is of numbers wth 0 as for 1st row(not including the header)
# consider the series of calories in fruits and we want fruits name instead of 0, 1, 2
new_index = ["apple", "banana", "pineapple", "apricot", "peach"]
s1.index = new_index
s1.name = "calories"
print(s1)
# apple        10
# banana       20
# pineapple    30
# apricot      40
# peach        50
# Name: calories, dtype: int64
print(s1['pineapple']) # prints 30
# print(s1.iloc['pineapple']) # gives error coz iloc is for numbers
print(s1.iloc[2]) # this gives 30

# therefor we have loc: label based indexing
print(s1.loc['pineapple']) # gives 30
print(s1.loc[['apple', 'pineapple']]) # prints apple and pineapple with values
# in loc, start and stop values both are included in output
print(s1['apple':'pineapple']) # prints apple, banana, pineapple with calories




