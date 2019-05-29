import pandas as pd

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,18,24,81,63,6]
}

df = pd.DataFrame(data)
print(df)
print()

print(df.columns)

# Drop all but the specified columns
columns_to_keep = ['LastName','Number']
columns_to_drop = []
columns_to_drop = [column for column in list(df.columns) if column not in columns_to_keep]

df.drop(columns=columns_to_drop, inplace=True)

print(df.columns)
print()
print(df)

