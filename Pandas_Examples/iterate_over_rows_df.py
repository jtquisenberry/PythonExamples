import pandas as pd

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,18,24,81,63,6]
}

df = pd.DataFrame(data)
print(df)
print()

for index, row in df.iterrows():
    print(index, row['FirstName'])