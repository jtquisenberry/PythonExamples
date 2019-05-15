import pandas as pd

data = {
    'FirstName':['Tom', 'Tom', 'David', 'Alex', 'Alex', 'Tom'],
    'LastName': ['Jones', 'Jones', 'Smith', 'Thompson', 'Thompson', 'Chuckles']
}

df = pd.DataFrame(data)
print(df)
print()

df = df.assign(id=(df['LastName'] + '_' + df['FirstName']).astype('category').cat.codes)
print(df)
print()

df = df.assign(id=(df['LastName']).astype('category').cat.codes)
print(df)
print()

df['Group_ID'] = df.groupby(['FirstName', 'LastName']).grouper.group_info[0]
print(df)

'''

df = df.assign(id=(df['LastName'] + '_' + df['FirstName']).astype('category').cat.codes)
>>> df
  FirstName  LastName  id
0       Tom     Jones   0
1       Tom     Jones   0
2     David     Smith   1
3      Alex  Thompson   2
4      Alex  Thompson   2
'''