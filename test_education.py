import pandas as pd

from education_extractor import extract_education

df = pd.read_csv("datasets/nlp_resume.csv")

resume = df.iloc[0]["Resume"]

print(extract_education(resume))