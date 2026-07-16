import pandas as pd

from certification_extractor import extract_certifications

print("Loading dataset...")

df = pd.read_csv("datasets/nlp_resume.csv")

print("Extracting certifications...")

df["Certifications"] = df["Resume"].fillna("").apply(extract_certifications)

# Convert list to string
df["Certifications"] = df["Certifications"].apply(lambda x: ", ".join(x))

output = "datasets/certification_resume.csv"

df.to_csv(output, index=False)

print("Certification dataset created successfully!")
print(df[["Category", "Certifications"]].head())