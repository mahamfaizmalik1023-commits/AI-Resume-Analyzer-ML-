import random
import pandas as pd

from resources.job_descriptions import JOB_DESCRIPTIONS

from semantic_matcher import semantic_similarity

from skill_extractor import extract_skills
from experience_extractor import extract_experience
from education_extractor import extract_education
from certification_extractor import extract_certifications

print("=" * 60)
print("Creating ATS Training Dataset")
print("=" * 60)

# Load resume dataset
df = pd.read_csv("datasets/nlp_resume.csv")

training = []

categories = list(JOB_DESCRIPTIONS.keys())


def calculate_skill_match(resume_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    matched = len(set(resume_skills) & set(job_skills))

    return round((matched / len(job_skills)) * 100, 2)


for index, row in df.iterrows():

    resume_text = str(row["Resume"])

    resume_category = row["Category"]

    # --------------------------
    # Resume Features
    # --------------------------

    resume_skills = extract_skills(resume_text)

    resume_exp = extract_experience(resume_text)

    resume_edu = extract_education(resume_text)

    resume_cert = extract_certifications(resume_text)

    # --------------------------
    # Positive Example
    # --------------------------

    if resume_category in JOB_DESCRIPTIONS:

        job = JOB_DESCRIPTIONS[resume_category]

        job_skills = extract_skills(job)

        job_exp = extract_experience(job)

        job_edu = extract_education(job)

        job_cert = extract_certifications(job)

        semantic = semantic_similarity(resume_text, job)

        skill_match = calculate_skill_match(
            resume_skills,
            job_skills
        )

        experience_match = min(
            resume_exp / max(job_exp, 1),
            1
        ) * 100

        education_match = (
            100 if len(set(resume_edu) & set(job_edu)) > 0 else 0
        )

        certification_match = (
            100 if len(set(resume_cert) & set(job_cert)) > 0 else 0
        )

        training.append({
            "Semantic": semantic,
            "Skill_Match": skill_match,
            "Experience_Match": experience_match,
            "Education_Match": education_match,
            "Certification_Match": certification_match,
            "Label": 1
        })

    # --------------------------
    # Negative Example
    # --------------------------

    wrong = random.choice(categories)

    while wrong == resume_category:
        wrong = random.choice(categories)

    job = JOB_DESCRIPTIONS[wrong]

    job_skills = extract_skills(job)

    job_exp = extract_experience(job)

    job_edu = extract_education(job)

    job_cert = extract_certifications(job)

    semantic = semantic_similarity(resume_text, job)

    skill_match = calculate_skill_match(
        resume_skills,
        job_skills
    )

    experience_match = min(
        resume_exp / max(job_exp, 1),
        1
    ) * 100

    education_match = (
        100 if len(set(resume_edu) & set(job_edu)) > 0 else 0
    )

    certification_match = (
        100 if len(set(resume_cert) & set(job_cert)) > 0 else 0
    )

    training.append({
        "Semantic": semantic,
        "Skill_Match": skill_match,
        "Experience_Match": experience_match,
        "Education_Match": education_match,
        "Certification_Match": certification_match,
        "Label": 0
    })

ats = pd.DataFrame(training)

ats.to_csv(
    "datasets/ats_training_data.csv",
    index=False
)

print()

print(ats.head())

print()

print("Dataset Size:", len(ats))

print()

print("ATS Training Dataset Created Successfully!")