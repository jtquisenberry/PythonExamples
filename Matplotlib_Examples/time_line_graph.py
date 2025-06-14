import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(12, 6))

x = np.linspace(0, 9, 10)
y1 = np.array([0, 2, 2, 5, 7, 15, 28, 55, 84, 155])
y2 = np.array([1, 1, 2, 3, 5, 8, 13, 21, 35, 56])

ax.plot(x, y1, color='blue', marker='d', label='Line 1', linewidth=3, markersize=6)
ax.plot(x, y2, color='red', marker='d', label='Line 2')
ax.set_title("Title")

ax.set_xlabel("Label X")
ax.set_ylabel("Label Y")
ax.set_xlim(x.min(), x.max() + 1)
ax.set_ylim(y1.min(), y1.max() + 10)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.grid(True)

ax.legend(loc='best', frameon=True)
plt.show()