import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats



from scipy.stats import lognorm
fig, ax = plt.subplots(1, 1)
s = 0.954
# s = .9
# x = np.linspace(lognorm.ppf(0.01, s), lognorm.ppf(0.99, s), 100)
data_lognormal = lognorm.rvs(s, size=1000)
ax.hist(data_lognormal, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
# ax.set_xlim([x[0], x[-1]])

data_normal = np.log(data_lognormal)
ax.hist(data_normal, density=True, bins='auto', histtype='stepfilled', alpha=0.2, color='red')

ax.legend(loc='best', frameon=False)
plt.show()


exit(0)




# Generate lognormal data (replace with your actual data)
mu = 2  # Mean of the underlying normal distribution
sigma = 0.5  # Standard deviation of the underlying normal distribution
data_lognormal = stats.lognorm.rvs(s=sigma, scale=np.exp(mu), size=1000)

# Transform the lognormal data to normal data
data_normal = np.log(data_lognormal)

shape = 0.5
scale = 7.39
loc = 0
mu = np.log(scale)
sigma = shape

# Create histograms
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Histogram of the lognormal data
axes[0].hist(data_lognormal, bins='auto', density=True, alpha=0.7, label='Lognormal Data')
axes[0].set_title('Lognormal Histogram')

# Histogram of the transformed normal data
axes[1].hist(data_normal, bins='auto', density=True, alpha=0.7, label='Transformed Normal Data')
axes[1].set_title('Transformed Normal Histogram')

# Overlay normal PDF on the transformed data
x = np.linspace(data_normal.min(), data_normal.max(), 100)
normal_pdf = stats.norm.pdf(x, loc=data_normal.mean(), scale=data_normal.std())
axes[1].plot(x, normal_pdf, 'r-', label='Normal PDF')

axes[1].legend()
plt.tight_layout()
plt.show()