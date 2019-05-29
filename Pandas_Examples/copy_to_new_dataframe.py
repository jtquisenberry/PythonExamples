import pandas as pd

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,18,24,81,63,6]
}

df = pd.DataFrame(data)
print(df)
print()

df2 = df[['FirstName','LastName']].copy()
print(df2)