import pandas as pd

data = {'a':[0,1,2,3,4,5,6,7,8,9], 'b':[0,1,2,3,4,5,6,7,8,9]}
df = pd.DataFrame(data)
df.index = pd.interval_range(start=0, end=6, periods=len(df))

# These keys fall within ranges.
# Find rows with the required ranges. Be sure to use .loc
print(df.loc[[2,3,5]])
# (1.7999999999999998, 2.4]  3  3
# (2.4, 3.0]                 4  4
# (4.8, 5.3999999999999995]  8  8

print()
print()

ts = pd.Series(df['a'].values, index=pd.interval_range(start=0, end=6, periods=len(df)))
print(ts)
# (0.0, 0.6]                   0
# (0.6, 1.2]                   1
# (1.2, 1.7999999999999998]    2
# (1.7999999999999998, 2.4]    3
# (2.4, 3.0]                   4
# (3.0, 3.5999999999999996]    5
# (3.5999999999999996, 4.2]    6
# (4.2, 4.8]                   7
# (4.8, 5.3999999999999995]    8
# (5.3999999999999995, 6.0]    9

a = 1