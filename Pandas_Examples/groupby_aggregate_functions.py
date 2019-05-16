import pandas as pd

class AggregateFunction:
    def __init__(self, number_of_elements=0):
        self.number_of_elements = number_of_elements

    def make_partial_list(self, series):
        return list(series)[:self.number_of_elements]


data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles'],
    'Number': [1,18,24,81,63,6]
}

df = pd.DataFrame(data)
print(df)
print()

# Built-in function STYLE 1
print('BUILT-IN STYLE 1')
df_agg = df.groupby(['FirstName'], as_index=False)['Number'].sum()
print(df_agg)
print()

# Built-in function STYLE 2 - using agg()
print('BUILT-IN STYLE 2')
df_agg = df.groupby(['FirstName'], as_index=False).agg({'Number': sum})
print(df_agg)
print()

# Custom function - using agg()
print('CUSTOM FUNCTION')
af = AggregateFunction(number_of_elements=3)
df_agg = df.groupby(['FirstName'], as_index=False).agg({'Number': af.make_partial_list})
print(df_agg)
print()





