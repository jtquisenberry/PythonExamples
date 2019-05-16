import pandas as pd
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/51163975/pandas-add-column-name-to-results-of-groupby

# There are two ways to give a name to an aggregate column.
# It may be necessary to unstack a compound DataFrame first.

# Initial DataFrame
d = {'timeIndex': [1, 1, 1, 9, 1, 1, 1, 2, 2, 2], 'isZero': [0, 0, 0, 1, 1, 1, 1, 0, 1, 0]}
df = pd.DataFrame(data=d)
print(df)
print()

# Group by one column
# The sum aggregate function creates a series
# notice that the sum does not have a column header
df_agg = df.groupby('timeIndex', as_index=False)['isZero'].sum()
print(type(df_agg))
print(df_agg)
print()

# Unstack OPTION 1, set as_index=False
df_agg = df.groupby('timeIndex', as_index=False)['isZero'].sum()
print(type(df_agg))
print(df_agg)
print()

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,18,24,81,63,6]
}

df = pd.DataFrame(data)

# This format creates a compound DataFrame
df_agg = df.groupby(['FirstName']).agg({'Number': sum})
print(df_agg)
print()

# Unstack OPTION 1, set as_index=False
df_agg = df.groupby(['FirstName'], as_index=False).agg({'Number': sum})
print(df_agg)
print()

# Unstack OPTION 2, use to_frame
# The argument of to_frame is the name of the new field.
df2 = df.groupby(['FirstName'])['Number'].sum().to_frame('Number_Sum').reset_index()
print(df2)








