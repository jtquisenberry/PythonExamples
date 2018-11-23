import pandas as pd
import matplotlib.pyplot as plt


d = {'timeIndex': [1, 1, 1, 1, 1, 1, 1, 2, 2, 2], 'isZero': [0,0,0,1, 1, 1, 1 ,0,1,0]}
df = pd.DataFrame(data=d)
print(df)
#df2 = df.groupby(['timeIndex'])['isZero'].sum()

df2 = df.groupby(['timeIndex'], as_index=False)['isZero'].sum()

# kind = 'barh'
df2.plot( x='timeIndex', y='isZero', kind='bar', color = ['r','b'], yticks=[0,1,2,3,5], title ='My Title')

aaa = plt

plt.show()

print(df2)