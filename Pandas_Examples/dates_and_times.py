import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time



def convertJavaDateSerial(serial):
    epoch = datetime(year=1899,month=12,day=30)
    dt = epoch + timedelta(days = serial)
    return dt





if __name__ == '__main__':
    dt = convertJavaDateSerial(43290.535516)
    print('datetime: {0}'.format(dt))
    print('date: {0}'.format(dt.date()))
    print('time: {0}'.format(dt.time()))
    print('DONE')


'''
dt = datetime(year=2018,month=3,day=28)
print(dt)
dt2 = datetime(year=1899,month=12,day=30)
dt3 = timedelta(days=43290.535516)
dt4 = dt2 + dt3
print(dt4)
'''