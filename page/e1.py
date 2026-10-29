#Exploratory Data Analysis (EDA)
#Aim: To calculate descriptive statistics, check missing values, and plot a histogram and #correlation matrix using the Iris dataset.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
df = sns.load_dataset('iris')

# Display first five rows
print(df.head())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Histogram
df.hist(figsize=(10, 6))
plt.show()

# Correlation matrix
sns.heatmap(df.select_dtypes(include='number').corr(),
            annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()