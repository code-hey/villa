#Sampling Methods
#Aim: To perform simple random sampling and stratified sampling and compare the samples.



import pandas as pd
from sklearn.model_selection import train_test_split

# Create dataset
data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K'],
    'Marks': [70, 80, 60, 90, 75, 85,
              65, 95, 55, 88, 50],
    'Grade': ['Pass', 'Pass', 'Pass', 'Pass', 'Pass',
              'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail']
}

df = pd.DataFrame(data)

# Simple random sampling
random_sample = df.sample(n=5, random_state=42)

print("Simple Random Sample:")
print(random_sample)

# Stratified sampling
stratified_sample, _ = train_test_split(
    df,
    test_size=0.5,
    stratify=df['Grade'],
    random_state=42
)

print("\nStratified Sample:")
print(stratified_sample)

