import pandas as pd

data =  {'A':[3,2,6],'B':['three','two','six']}
df = pd.DataFrame(data)
print(df.head())
print()

# Append using dictionary
data_dict = {'A':[4,5],'B':['four','five']}
df = df.append(pd.DataFrame(data_dict), ignore_index=True)
print(df.head(7))
print()

# Append using list
data_list = [7,'seven']
df.loc[len(df)] = data_list
print(df.head(10))




