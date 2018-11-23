import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\testFile2.csv', header=None)

df.columns = ['guid','totalTime','gStart', 'gEnd', 'threadId', 'threadCount', 'fileSize', 'characterCount']


df['guidA'] = df.gStart.str[0:36]
df['guidB'] = df.gEnd.str[0:36]
df['startTime'] = df.gStart.str[37:]
df['endTime'] = df.gEnd.str[37:]
df['startTime'] = pd.to_numeric(df['startTime'], errors = 'coerce')
df['endTime'] = pd.to_numeric(df['endTime'], errors = 'coerce')
df['totalTime2'] = df.endTime - df.startTime

# Total records
totalRecords = df['guid'].count()
print(totalRecords)

# Records with expected guids.
print(df['guid'].loc[(df['guid'] == df['guidA']) & (df['guid'] == df['guidB'])].count())

# Records with expected time.
print(df['guid'].loc[df['totalTime'] == df['totalTime2']].count())
# Records with unexpected time.
print(df['guid'].loc[df['totalTime'] != df['totalTime2']].count())

'''
chunkSize = 100
numberOfChunks = totalRecords // chunkSize
firstBadChunk = 0
for i in range(numberOfChunks):
    df2 = df.loc[i * chunkSize:((i + 1) * chunkSize - 1), ['characterCount']]
    zeroCharacterItems = df2.loc[df2.characterCount == 0].count()
    zeroCharacterItems = zeroCharacterItems.values[0]
    if (i + 1) % (chunkSize * 10) == 0:
        print(i + 1)
    if zeroCharacterItems > 50:
        print('Cluster of 0s at {0} with {1} documents.'.format(i * chunkSize, zeroCharacterItems))
        firstBadChunk = i * chunkSize
        break
'''

#print(df[firstBadChunk:firstBadChunk + chunkSize])

df['isZero'] = 0
df['isZero'].loc[df.characterCount == 0] = 1

#Prepare for histogram

df5 = df[['endTime','isZero']]
df5['timeIndex'] = df5.endTime // 900000000000 # quarter-hour in nanoseconds
df6 = df5.groupby(['timeIndex'], as_index=False)['isZero'].sum()
#df6.columns = ['timeIndex','zeros']

d = {'times': ['15:45',
                  '16:00','16:15','16:30','16:45',
                  '17:00','17:15','17:30','17:45',
                  '18:00','18:15','18:30','18:45',
                  '19:00','19:15','19:30','19:45',
                  '20:00','20:15','20:30','20:45',
                  '21:00','21:15']}
frame = pd.DataFrame(data=d)
df6 = df6.join(frame)

# kind = 'barh'
#df6.plot( x='timeIndex', y='isZero', kind='bar', color = ['r','r'])
df6.plot( x='times', y='isZero', kind='bar', color = ['r','r'])

plt.show()
#plt.show()
#print(df6)
jjj  = 1

# Plotting attempt
'''
ts = pd.Series(df.isZero, index=pd.interval_range(start=5188509664358631,end=5209533203929358,periods=10))
ts = ts.cumsum()
'''
#df4.hist(column='isZero')



'''
countOfZeros = 0
for i in range(101):
    if df['characterCount'].values[0] == 0:
        countOfZeros += 1

    #if i + 1 % 20 == 0:

print(countOfZeros)
'''
'''
df3 = df[['guid','guid']].loc[df.characterCount == 0].copy()
df3.columns = ['GUID', 'Tag']
df3.Tag = 'JQ|ZeroCharacters'
df3['Comment'] = None
df3.to_csv('E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\zeros.csv', index = False)
'''


print(df.iloc[[50, 60], [10, 11]])


a = 1

