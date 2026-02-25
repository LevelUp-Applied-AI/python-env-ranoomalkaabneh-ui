import pandas as pd

# Load the dataset
df = pd.read_csv("data/sample.csv")

# Print shape
print("Shape:")
print(df.shape)

# Print first few rows
print("\nHead:")
print(df.head())

# Print statistical summary
print("\nDescribe:")
print(df.describe())