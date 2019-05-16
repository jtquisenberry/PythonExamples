import pandas as pd

# dict to DataFrame
data = {'A':[0,1,2], 'B':[2,1,0]}
df = pd.DataFrame(data)
print(df)
print()

# DataFrame to dict
data2 = df.to_dict()
print(data2)

