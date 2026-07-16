import pandas as pd
from skill_extractor import extract_skills

print("=" * 50)
print("Building Skill Dataset")
print("=" * 50)

# Load NLP processed dataset
df = pd.read_csv("datasets/nlp_resume.csv")

# Replace missing values
df["Processed_Resume"] = df["Processed_Resume"].fillna("")

print("Extracting skills from resumes...")

# Extract skills
df["Skills"] = df["Processed_Resume"].apply(extract_skills)

# Convert list to comma-separated string
df["Skills"] = df["Skills"].apply(lambda x: ", ".join(x))

# Save new dataset
output_path = "datasets/skills_resume.csv"
df.to_csv(output_path, index=False)

print("\n✅ Skill dataset created successfully!")
print(f"Saved to: {output_path}")

print("\nFirst 5 Rows:")
print(df[["Category", "Skills"]].head())