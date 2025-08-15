# Cleaning a dataset
import pandas as pd
import numpy as np
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Usman"],
    "Age": [23, np.nan, 22, 24, np.nan],
    "City": ["Lahore", "Karachi", np.nan, "Quetta", "Peshawar"]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull().sum()) # Name    0, Age     2, City    1 # no of Null values n each col
print(df.dropna()) # drops rows with Nan values
print(df.dropna(how = "any")) # is same is df.dropna()
print(df.dropna(how = "all")) 
# only drops the row with all null values # in this case, no rows were dropped
# the other way is to fill those null values 
print(df.fillna(0)) # 0 placed in place of Nan
# but this isn't that helpful method
# another way is to fill Nan with mean value of the column
print(df["Age"].fillna(df["Age"].mean())) # use inplace = True to modify original data
# another way is forward fill and backward fill:
# the Nan value is replaced with succeeding or preeceding value of the column
print(df['Age'].fillna(method = "ffill")) # 2nd nan was replaced with previous value
print(df['Age'].fillna(method = "bfill")) # last row didn't get replaced with the preeceding value
# we can use inplace = True to modify the original dataframe

# to replace an entry:
print(df['Name'].replace("Sara", "Habiba"))

# to deal with duplicate values
print(df[df.duplicated()]) # it does not give an output coz rn we don't have any duplicated rows
# duplicate functions only shows the 2nd repeated value, not the first one(BY DEFAULT)
print(df[df.duplicated(keep = "first")]) # it will show 2nd repeating element as duplicated
print(df[df.duplicated(keep = "last")]) # it will show 1st repeating element as duplicated
print(df.drop_duplicates()) # removes the duplicate values




