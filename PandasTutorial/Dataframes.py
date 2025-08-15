import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
    "Age": [23, 25, 22, 24],
    "City": ["Lahore", "Karachi", "Quetta", "Quetta"]
}
df = pd.DataFrame(data)
print(df)
print(df.head(2)) # 2 if we only want first two rows, by dedault it's 5
print(df.tail(2)) # 2 if we only want last two rows, by dedault it's 5
print("1st and 2nd row: \n", df.iloc[1:3])
print("0th row and 2nd col value \n", df.iloc[0, 2])
print("1st and 3rd row \n", df.loc[[0, 2]])
# double [[]] for complete row, and single [] for only single value
# in loc, start and step values both are included
print("row 0, 1, 2, col only name and city \n", df.loc[0:2, ["Name", "City"]])
print("row 1, col 0 n 1 \n", df.iloc[1:2, :2])
print("to only access single col: \n", df["City"]) # prints all cities even if repeating
# to access multiple cols use [[]]
print("Multiple cols: \n", df[["Name", "City"]])

# to drop a particular col from a dataframe:
df.drop("City", axis = 1) # axis = 1, for col wise operation
print(df) # df printed as it is including city col
# but if we want to really delete an entire col, we pass another parameter
df.drop("City", axis = 1, inplace = True)
print("Modified df with city col removed: \n", df) 

print(df.shape) # prints row-col # here (4, 2)
print(df.info()) # prints data type, and other relevant information
print(df.describe()) # to get statistical information about a dataset

# if we want to increase age of every entry to 1
df["Age"] = df["Age"] + 1
print(df)

# Renaming columns:
df.rename(columns = {"Name" : "Students"}, inplace = True)
print(df)

# to check all unique values in a dataset in a particular column:
print(df["Age"].unique()) # [24 26 23 25], with no repititions

# now if we want to see occurrences of unique values in a particular col:
print(df["Age"].value_counts()) # 24    1, 26    1, 23    1, 25    1

# to add a new col:
df["Salry"] = df["Age"] * 100000
print(df) # a new salary column has been added



