import pandas as pd

# Update column values with apply


data = {
    'animal':['cow', 'pig', 'chicken', 'fish'],
    'number':[3,2,6,3]
}

df = pd.DataFrame(data)
print(df)
print()

df2 = df.loc[df['animal'] == 'cow']
print(df2)
print()

df2 = df.loc[(df['animal'] == 'cow') & (df['number'] == 3)]
print(df2)
print()

df2 = df.loc[(df['animal'] == 'cow') | (df['number'] == 3)]
print(df2)
print()
