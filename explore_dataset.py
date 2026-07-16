import pandas as pd

df = pd.read_csv("datasets/resume_text.csv")

print("=" * 50)
print("Dataset Information")
print("=" * 50)

print(df.info())

print("\nFirst 5 Rows")
print(df.head())

print("\nResume Categories")
print(df["Category"].value_counts())

print("\nMissing Values")
print(df.isnull().sum())