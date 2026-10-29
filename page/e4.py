#Central Limit Theorem (CLT)
#Aim: To generate random data, repeatedly calculate sample means, and plot their #distribution.

import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.exponential(scale=2, size=10000)

# Calculate repeated sample means
means = []

for i in range(1000):
    sample = np.random.choice(data, size=50)
    means.append(np.mean(sample))

# Display sample mean
print("Mean of Sample Means:", np.mean(means))

# Plot distribution
plt.hist(means, bins=30, edgecolor='black')
plt.title("Central Limit Theorem")
plt.xlabel("Sample Means")
plt.ylabel("Frequency")
plt.show()