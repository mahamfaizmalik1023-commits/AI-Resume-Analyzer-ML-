from skill_extractor import extract_skills
from experience_extractor import extract_experience
from education_extractor import extract_education
from certification_extractor import extract_certifications


def parse_job(job_description):
    """
    Extract all important information
    from a Job Description.
    """

    data = {}

    # Skills
    data["skills"] = extract_skills(job_description)

    # Experience
    data["experience"] = extract_experience(job_description)

    # Education
    data["education"] = extract_education(job_description)

    # Certifications
    data["certifications"] = extract_certifications(job_description)

    return data