import pandas as pd

print("=" * 50)
print("Feature Engineering")
print("=" * 50)

# Load datasets
skills = pd.read_csv("datasets/skills_resume.csv")
experience = pd.read_csv("datasets/experience_resume.csv")
education = pd.read_csv("datasets/education_resume.csv")
certification = pd.read_csv("datasets/certification_resume.csv")

# Create a new dataframe
features = pd.DataFrame()

# Category (Target Label)
features["Category"] = skills["Category"]

# Number of Skills
features["Skill_Count"] = skills["Skills"].fillna("").apply(
    lambda x: len(str(x).split(",")) if str(x).strip() != "" else 0
)

# Experience
features["Experience"] = experience["Experience"]

# Number of Degrees
features["Education_Count"] = education["Education"].fillna("").apply(
    lambda x: len(str(x).split(",")) if str(x).strip() != "" else 0
)

# Number of Certifications
features["Certification_Count"] = certification["Certifications"].fillna("").apply(
    lambda x: len(str(x).split(",")) if str(x).strip() != "" else 0
)

# Resume Length
features["Resume_Length"] = skills["Resume"].fillna("").apply(len)

print(features.head())

# Save dataset
features.to_csv("datasets/features.csv", index=False)

print("\n✅ features.csv created successfully!")