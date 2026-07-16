import os
import pandas as pd

from parser import extract_text_from_pdf

DATASET_PATH = "datasets/data/data"

resumes = []

for category in os.listdir(DATASET_PATH):

    category_path = os.path.join(DATASET_PATH, category)

    if os.path.isdir(category_path):

        print(f"Reading {category}")

        for file in os.listdir(category_path):

            if file.endswith(".pdf"):

                pdf_path = os.path.join(category_path, file)

                text = extract_text_from_pdf(pdf_path)

                resumes.append({
                    "Category": category,
                    "File": file,
                    "Resume": text
                })

df = pd.DataFrame(resumes)

print(df.head())

df.to_csv("datasets/resume_text.csv", index=False)

print("Done!")
print("Total resumes:", len(df))