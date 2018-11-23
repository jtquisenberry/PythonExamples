import pandas as pd
import matplotlib.pyplot as plt

# Plot a jconsole.exe log of memory utilization (heap).

def convertToTime(time):
    time = time % 1
    hours = (time * 24) // 1
    minutes = (((time * 24) % 1) * 60) // 1
    seconds = (((time * 24 * 60) % 1) * 60) // 1
    hundredths = (((time * 24 * 60 * 60) % 1) * 100) // 1
    return ("%d:%02d:%02d.%02d" % (hours, minutes, seconds, hundredths))


def readMemoryData():
    #x = convertToTime(0.60915)
    #df = pd.read_csv("E:\\specs\\DR_Data_Crawler\\CNA_Insurance\\testFile2\\memory.csv")
    df = pd.read_csv("data\\memory.csv")
    df['clockTime'] = df['Time'].apply(convertToTime)

    #Fails because passes the entire series.
    #df['clockTime'] = convertToTime(df['Time'])
    df['GBs'] = df['Used'] / 1024 / 1024 / 1024

    #df.plot(x='clockTime', y='Used', kind='bar', color=['r', 'r'])
    z = df.plot(x='clockTime', y='GBs', rot=30, figsize=(9, 4), legend=False)
    z.set_xlabel('')

    plt.subplots_adjust(bottom = .20)

    #x0, x1, y0, y1 = plt.axis()

    plt.show()
    a = 1

if __name__ == '__main__':
    readMemoryData()