import pandas as pd

# Update column values with apply


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

# Create new column
df['number2'] = df['number'].apply(lambda x: x ** 2)
print(df)
print()