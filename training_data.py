import random
import pandas as pd

from resources.job_descriptions import JOB_DESCRIPTIONS

print("Loading features dataset...")

df = pd.read_csv("datasets/features.csv")

training = []

categories = list(JOB_DESCRIPTIONS.keys())

for _, row in df.iterrows():

    resume_category = row["Category"]

    # Positive example
    if resume_category in JOB_DESCRIPTIONS:

        training.append({
            "Resume_Category": resume_category,
            "Job_Category": resume_category,
            "Label": 1
        })

    # Negative example
    negative = random.choice(categories)

    while negative == resume_category:
        negative = random.choice(categories)

    training.append({
        "Resume_Category": resume_category,
        "Job_Category": negative,
        "Label": 0
    })

training_df = pd.DataFrame(training)

training_df.to_csv(
    "datasets/training_data.csv",
    index=False
)

print("Training dataset created.")
print(training_df.head())