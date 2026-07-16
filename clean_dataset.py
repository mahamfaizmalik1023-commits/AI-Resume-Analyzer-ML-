import pandas as pd

df = pd.read_csv("datasets/resume_text.csv")

print("Before Cleaning:", len(df))

# Remove rows where Resume is empty
df = df.dropna(subset=["Resume"])

print("After Cleaning:", len(df))

df.to_csv("datasets/clean_resume.csv", index=False)

print("✅ clean_resume.csv created!")