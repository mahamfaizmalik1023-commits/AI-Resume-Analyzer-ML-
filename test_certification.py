import pandas as pd

from certification_extractor import extract_certifications

df = pd.read_csv("datasets/nlp_resume.csv")

resume = df.iloc[0]["Resume"]

print(extract_certifications(resume))