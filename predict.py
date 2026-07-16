import joblib

from semantic_matcher import semantic_similarity
from skill_extractor import extract_skills
from experience_extractor import extract_experience
from education_extractor import extract_education
from certification_extractor import extract_certifications


# Load trained ATS model
model = joblib.load("models/ats_xgboost_model.pkl")


def calculate_skill_match(resume_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    matched = len(set(resume_skills) & set(job_skills))

    return round((matched / len(job_skills)) * 100, 2)


def predict_resume(resume_text, job_text):

    # Resume features
    resume_skills = extract_skills(resume_text)
    resume_exp = extract_experience(resume_text)
    resume_edu = extract_education(resume_text)
    resume_cert = extract_certifications(resume_text)

    # Job features
    job_skills = extract_skills(job_text)
    job_exp = extract_experience(job_text)
    job_edu = extract_education(job_text)
    job_cert = extract_certifications(job_text)

    # Feature calculations
    semantic = semantic_similarity(
        resume_text,
        job_text
    )

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

    features = [[
        semantic,
        skill_match,
        experience_match,
        education_match,
        certification_match
    ]]

    prediction = model.predict_proba(features)[0][1]

    ats_score = round(prediction * 100, 2)

    return {
        "ATS Score": ats_score,
        "Semantic Score": semantic,
        "Skill Match": skill_match,
        "Experience Match": experience_match,
        "Education Match": education_match,
        "Certification Match": certification_match,
        "Matched Skills": list(
            set(resume_skills) & set(job_skills)
        ),
        "Missing Skills": list(
            set(job_skills) - set(resume_skills)
        )
    }