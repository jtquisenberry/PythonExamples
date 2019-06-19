"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

rectangles_per_group = 3

data1_heights = (20, 35, 30, 35, 27)
data1_errors = (2, 3, 4, 1, 2)

data2_heights = (25, 32, 34, 20, 25)
data2_errors = (3, 5, 2, 3, 3)

data3_heights = (15, 24, 32, 22, 18)


# X - positions of rectangles. Start with number of groups.
# Then add a fraction for each group.
# Set to number of rectangles or
# number of rectangles * width of rectangles.
width = 0.25       # the width of the bars
x_positions1 = [x + 0 * width for x in range(len(data1_heights))]
x_positions2 = [x + 1 * width for x in range(len(data2_heights))]
x_positions3 = [x + 2 * width for x in range(len(data3_heights))]

# Get default figure and subplot
fig, ax = plt.subplots()

# Add each group
rects1 = ax.bar(x_positions1, data1_heights, width, color='r', yerr=data1_errors)
rects2 = ax.bar(x_positions2, data2_heights, width, color='y', yerr=data2_errors)
rects3 = ax.bar(x_positions3, data3_heights, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks([(x + x + ((rectangles_per_group - 1) * width)) / 2 for x in x_positions1])
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()