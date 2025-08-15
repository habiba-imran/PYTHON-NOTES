# DICTIONARY DATASET:
import pandas as pd
fruitCalories = {
    "Apple": 20,
    "Banana": 40,
    "Pneapple": 60,
    "Grapes": 80,
    "Avacado": 100
}
s = pd.Series(fruitCalories, name = "calories") # dict gets converted to a series
print(s)
# to print rows where calories > 20:
print(s > 20) # Apple       False, all rows are printed with boolean values
print(s[s > 20]) # only rows and their values are printed where calories > 20

# CONDITIONAL INDEXING:
print([(s > 20) & (s < 80)]) # prints all rows with boolean values
print(s[(s > 20) & (s < 80)]) # prints only desired rows with values
print(s[~(s > 20)]) # prinst only apple, not operator
print(s[(s > 20) | (s == 20)]) # or operator

# MODIFYING SERIES
s['Grapes'] = 120
print(s)


