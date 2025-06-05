from fitter import Fitter
from scipy import stats
import numpy as np

# Generate sample data (replace with your actual data)
data = stats.gamma.rvs(2, loc=1.5, scale=2, size=100000)

# Create a Fitter object
# f = Fitter(data, distributions=['gamma', 'rayleigh', 'uniform']) # You can specify distributions or let Fitter try all
f = Fitter(data) # You can specify distributions or let Fitter try all

# Fit the distributions
f.fit()

# Print the summary of the best distributions
f.summary()

# Get the best fitting distribution
best_distribution = f.get_best()
print(f"\nBest distribution: {best_distribution}")