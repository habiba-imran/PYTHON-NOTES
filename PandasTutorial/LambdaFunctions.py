# LAMBDA FUNCTIONS
# lambda input: output, normally in python:
square = lambda x : x**2 # 
print(square(4))
# now for the dataset:
import pandas as pd
data = {
    "Name": ["Ali_Ahmad", "Sara_Ali", "Ahmed_Fayyaz", "Fatima_Zeeshan", "Usman_Qureshi"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT"],
    "Age": [28, 25, 30, 27, 24],
    "Salary": [50000, 65000, 55000, 60000, 58000]
}
df = pd.DataFrame(data)
print(df)
# to add a new column of promoted salary:
df["Promoted Salary"] = df["Salary"].apply(lambda x: x + 50000)
print(df) # a new column is added: promoted salary
# OR, we can also use a condition here:
df["Pansion"] = df["Salary"].apply(lambda x: x + 5000 if x > 60000 else x)
print(df)

# right now we have names as firstname_lastname, to split it into columns of two:
df[["First Name", "Last Name"]] = df["Name"].str.split("_", expand = True)
# Without expand=True, Pandas would store lists inside the column 
# instead of splitting them into two separate columns.
print(df) # Name col also get printed, we can remove it too
df.drop(("Name"), axis = 1, inplace = True)
print(df)

def multiply_age(x):
    return x*2
df["Age"] = df["Age"].apply(multiply_age)
print(df) # age column gets multiplied by 2
df['Age'] = df['Age'].apply(lambda x: x / 2)
print(df)


