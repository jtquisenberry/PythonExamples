import pandas as pd

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,18,24,81,63,6]
}

df = pd.DataFrame(data)
print(df)
print()


# Sort by two columns, the first ascending and the second descending.
df.sort_values(by=['Number','FirstName'], ascending=[1,0], inplace=True)
print(df)