import pandas as pd

data = {'A':[1,1,1,2,3,4], 'B':[2,2,2,2,2,2]}
df = pd.DataFrame(data)
print(df)
print()

df.drop_duplicates(inplace=True)
print(df)