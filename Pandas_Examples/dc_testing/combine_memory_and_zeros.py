import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Plot a jconsole.exe log of memory utilization (heap).

def convertToTime(time):
    time = time % 1
    hours = (time * 24) // 1
    minutes = (((time * 24) % 1) * 60) // 1
    seconds = (((time * 24 * 60) % 1) * 60) // 1
    hundredths = (((time * 24 * 60 * 60) % 1) * 100) // 1
    return ("%d:%02d:%02d.%02d" % (hours, minutes, seconds, hundredths))

def convertJavaDateSerial(serial):
    epoch = datetime(year=1899,month=12,day=30)
    dt = epoch + timedelta(days = serial)
    return dt

def setTimeBin(start_time, time_index, minutes):
    return start_time + timedelta(minutes = (time_index * minutes))






def readMemoryData():
    #x = convertToTime(0.60915)
    #df = pd.read_csv("E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\memory.csv")
    #df = pd.read_csv("data\\memory.csv")
    df = pd.read_csv("E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\20180709-001_308_Mod001.csv")
    df['clockTime'] = df['Time'].apply(convertJavaDateSerial)

    #Fails because passes the entire series.
    #df['clockTime'] = convertToTime(df['Time'])
    df['GBs'] = df['Used'] / 1024 / 1024 / 1024

    return df

def readZeros(start_time):
    #df = pd.read_csv('E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\testFile2.csv', header=None)
    df = pd.read_csv('E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\testFile_20180709-001_308Mod.csv', header=None)
    df.columns = ['guid', 'totalTime', 'gStart', 'gEnd', 'threadId', 'threadCount', 'fileSize', 'characterCount']

    df['startTime'] = df.gStart.str[37:]
    df['endTime'] = df.gEnd.str[37:]
    df['startTime'] = pd.to_numeric(df['startTime'], errors='coerce')
    df['endTime'] = pd.to_numeric(df['endTime'], errors='coerce')
    df['totalTime2'] = df.endTime - df.startTime

    # Total records
    totalRecords = df['guid'].count()
    #print(totalRecords)

    # Prepare to get the count of zero-character items.
    df['isZero'] = 0
    df['isZero'].loc[df.characterCount == 0] = 1

    # Prepare for histogram
    df5 = df[['endTime', 'isZero']].copy()
    df5['timeIndex'] = df5.endTime // 900000000000  # quarter-hour in nanoseconds

    earliestTime = df5['timeIndex'].min()
    df5['timeIndex'] = df5['timeIndex'] - earliestTime





    df6 = df5.groupby(['timeIndex'], as_index=False)['isZero'].sum()
    # df6.columns = ['timeIndex','zeros']
    #df6['timeIndex'] = df6['timeIndex'].apply(setTimeBin(start_time=earliestTime,minutes=15))
    df6['timeIndex'] = df6['timeIndex'].apply(lambda time_index: setTimeBin(start_time, time_index, 15))

    return df6



if __name__ == '__main__':
    df = readMemoryData()

    #zerosStartTime = datetime(year=2018,month=7,day=6,hour=14,minute=37,second=10)
    zerosStartTime = datetime(year=2018, month=7, day=9, hour=12, minute=51, second=8)
    df6 = readZeros(zerosStartTime)
    df6 = df6.set_index('timeIndex')

    # Draw the first axis.
    # ax1 = df['isZero'].plot(x='xTimes',  color='blue', grid=True, label='Count')
    df = df.set_index('clockTime')
    ax1 = df['GBs'].plot(color='blue', grid=True)

    # Draw the second axis.
    ax2 = df6['isZero'].plot(color='red', grid=True, secondary_y=True, label='Zeros')
    #ax2 = df6['isZero'].plot(x='timeIndex', color='red', grid=True, secondary_y=True, label='Plot 2')
    #ax2 = df6.plot(x='timeIndex', y= 'isZero', color='red', grid=True, secondary_y=True, label='Plot 2')

    # Set legend label here.
    # Set location to upper-left
    #ax1.legend(['GBs'], loc=1)
    ax1.legend(['GBs'], loc=(0, 1.02))

    # Legend label set above at plot()
    # Location is coordinates.
    # ax2.legend(loc=2)
    ax2.legend(loc=(0.82, 1.02))

    # Adjust bottom margin
    # plt.subplots_adjust(bottom = .20)

    # Display the plot.
    plt.show()















'''
    #df.plot(x='clockTime', y='Used', kind='bar', color=['r', 'r'])
    z = df.plot(x='clockTime', y='GBs', rot=30, figsize=(9, 4), legend=False)
    z.set_xlabel('')

    plt.subplots_adjust(bottom = .20)

    #x0, x1, y0, y1 = plt.axis()

    plt.show()
    a = 1

    df6.plot(x='times', y='isZero', kind='bar', color=['r', 'r'])

    plt.show()
    # plt.show()
    # print(df6)
    jjj = 1


'''