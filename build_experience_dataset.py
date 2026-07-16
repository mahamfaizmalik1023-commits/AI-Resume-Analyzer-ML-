import pandas as pd

from experience_extractor import extract_experience

print("Loading dataset...")

df = pd.read_csv("datasets/nlp_resume.csv")

print("Extracting experience...")

df["Experience"] = df["Resume"].fillna("").apply(extract_experience)

df.to_csv("datasets/experience_resume.csv", index=False)

print("Done!")
print(df.head())