from datetime import *


dt_now = datetime.now()
d_now = datetime.now().date()
t_now = datetime.now().time()

# Basic printing
print('datetime = {0}'.format(dt_now))
print('date = {0}', d_now)
print('time = {0}', t_now)

# Truncating and padding
print('datetime2 {:10.4}'.format(str(dt_now)))

# 20180813-202750
print('datetime3 {0}'.format(dt_now.strftime('%Y%m%d-%H%M%S')))

# Add negative time
dt2 = dt_now + timedelta(seconds = -300)
print("dt2", dt2)

# Required argument 'year' (pos 1) not found
#dt3 = dt_now + datetime(seconds = -300)

# Add fractional time
dt4 = dt_now + timedelta(days=0.1)
print(dt4)

