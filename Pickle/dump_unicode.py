import pickle
import pandas as pd

infile = r"C:\Temp"


data = {'A':['a','b'], 'B':['q','𠀁']}

# Unicode in dictionary
# With some sorts of data, the load operation fails.
pickle.dump(data, open(infile + '\\' + 'dict001.pkl', 'wb'))
data_loaded = pickle.load(open(infile + '\\' + 'dict001.pkl', 'rb'))

# Unicode in DataFrame
df = pd.DataFrame(data)
# This should prevent the pickle load from failing
df['B'] = df['B'].astype('unicode')
df.to_pickle(infile + '\\' + 'dict002.pkl')
df_loaded = pd.read_pickle(infile + '\\' + 'dict002.pkl')


a = 1