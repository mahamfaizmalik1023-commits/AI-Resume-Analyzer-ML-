import pandas as pd
from preprocessing import preprocess_text

print("Loading dataset...")

# Read cleaned resumes
df = pd.read_csv("datasets/clean_resume.csv")

print("Processing resumes...")

# Apply NLP preprocessing
df["Processed_Resume"] = df["Resume"].fillna("").apply(preprocess_text)

# Save processed dataset
df.to_csv("datasets/nlp_resume.csv", index=False)

print("===================================")
print("NLP preprocessing completed!")
print("Total resumes:", len(df))
print("File saved as: datasets/nlp_resume.csv")
print("===================================")