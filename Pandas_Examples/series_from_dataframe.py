import pandas as pd

d = {'a':[0,1,2,3,4,5, 6]}
df = pd.DataFrame(d)
ts = pd.Series(df.a, index=pd.interval_range(start=0, end=6, periods=2))
a = 1