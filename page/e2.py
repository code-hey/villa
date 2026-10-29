#Data Preprocessing
#Aim: To handle missing values, encode categorical variables, and scale numerical features #using StandardScaler.

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Create dataset
data = {
    'Age': [20, 21, None, 23, 22],
    'Marks': [80, 75, 90, None, 85],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Encode categorical variable
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Scale numerical features
scaler = StandardScaler()
df[['Age', 'Marks']] = scaler.fit_transform(df[['Age', 'Marks']])

print("\nPreprocessed Data:")
print(df)