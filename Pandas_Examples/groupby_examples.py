import pandas as pd
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/51163975/pandas-add-column-name-to-results-of-groupby

d = {'timeIndex': [1, 1, 1, 1, 1, 1, 1, 2, 2, 2], 'isZero': [0, 0, 0, 1, 1, 1, 1, 0, 1, 0]}
df = pd.DataFrame(data=d)
print(df)
print()

# Return a DataFrame, rather than a Series
# This gives a name to the aggregate column
df2 = df.groupby(['timeIndex'], as_index=False)['isZero'].sum()
print(type(df2))
print(df2)

# Groupby two fields and aggregate on one field.
df3 = df.groupby(['timeIndex','isZero'])['isZero'].sum()
print(type(df3))
print(df3)

# Plot the results of aggregating over a DataFrame
# kind = 'barh'
df2.plot( x='timeIndex', y='isZero', kind='bar', color = ['r','b'], yticks=[0,1,2,3,5], title ='My Title')
plt.show()
