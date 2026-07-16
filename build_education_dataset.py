import pandas as pd

from education_extractor import extract_education

print("Loading dataset...")

df = pd.read_csv("datasets/nlp_resume.csv")

print("Extracting education...")

df["Education"] = df["Resume"].fillna("").apply(extract_education)

# Convert list into text
df["Education"] = df["Education"].apply(lambda x: ", ".join(x))

output = "datasets/education_resume.csv"

df.to_csv(output, index=False)

print("Education dataset created successfully!")
print(df[["Category", "Education"]].head())