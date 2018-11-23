import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame based on a dictionary.
d = {'timeIndex': [1, 1, 1, 1, 1, 1, 1, 2, 2, 2], 'isZero': [0,0,0,1, 1, 1, 1 ,0,1,0],
     'isOne':[99,98,99,88,78,89,96,99,97,93], 'xTimes':[0,1,2,3,4,5,6,7,8,9]}
df = pd.DataFrame(data=d)
#print(df)

# Draw the first axis.
#ax1 = df['isZero'].plot(x='xTimes',  color='blue', grid=True, label='Count')
ax1 = df['isZero'].plot(x='xTimes',  color='blue', grid=True)

# Draw the second axis.
ax2 = df['isOne'].plot(x='xTimes',  color='red', grid=True, secondary_y=True, label='Plot 2')

# Set legend label here.
# Set location to upper-left
ax1.legend(['Plot 1'],loc=1)

# Legend label set above at plot()
# Location is coordinates.
#ax2.legend(loc=2)
ax2.legend(loc=(0,1.02))


# Adjust bottom margin
#plt.subplots_adjust(bottom = .20)

# Display the plot.
plt.show()

