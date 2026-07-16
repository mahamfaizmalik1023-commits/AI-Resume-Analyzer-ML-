import pandas as pd
from skill_extractor import extract_skills

df = pd.read_csv("datasets/nlp_resume.csv")

sample = df.iloc[0]

print("Category:")
print(sample["Category"])

print("\nSkills:")
print(extract_skills(sample["Processed_Resume"]))