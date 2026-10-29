#Bootstrap Confidence Interval
#Aim: To generate bootstrap samples and calculate a 95% confidence interval for the mean.

import numpy as np

# Original data
data = np.array([20, 25, 30, 35, 40, 45, 50])

# Bootstrap sampling
np.random.seed(42)
bootstrap_means = []

for i in range(1000):
    sample = np.random.choice(data, size=len(data), replace=True)
    bootstrap_means.append(np.mean(sample))

# Calculate 95% confidence interval
lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)

print("Original Mean:", np.mean(data))
print("95% Confidence Interval:", lower, "to", upper)