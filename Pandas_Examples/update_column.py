import pandas as pd

# Update column values with apply

def concatenate(row):
    return str(row[0]) + str(row[1])

data = {
    'animal':['cow', 'pig', 'chicken', 'fish'],
    'number':[3,2,6,3]
}

df = pd.DataFrame(data)
print(df)
print()

# Update column
df['number'] = df['number'].apply(lambda x: x ** 2)
print(df)
print()

# Create new column and update it from ONE other column
df['number2'] = df['number'].apply(lambda x: x ** 2)
print(df)
print()

# Create new column and update it from ALL other columns
df['concat'] = df.apply(lambda x: concatenate(x), axis=1)
print(df)
print()