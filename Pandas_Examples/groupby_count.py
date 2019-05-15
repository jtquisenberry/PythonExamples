import pandas as pd

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,2,3,4,5,6]
}

df = pd.DataFrame(data)
print(df)
print()

df_agg = df.groupby(['FirstName']).agg({'Number':sum})
print(df_agg)

# TODO unpack group by

a = 1