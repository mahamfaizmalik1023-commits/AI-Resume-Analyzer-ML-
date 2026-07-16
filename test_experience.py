import pandas as pd

from experience_extractor import extract_experience

df = pd.read_csv("datasets/nlp_resume.csv")

resume = df.iloc[0]["Resume"]

print("Years of Experience:")
print(extract_experience(resume))