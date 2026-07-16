import re

def load_skills(file_path="resources/skills.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        skills = [line.strip().lower() for line in f if line.strip()]
    return skills


SKILLS = load_skills()


def extract_skills(text):

    if not isinstance(text, str):
        return []

    text = text.lower()

    found = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found.append(skill)

    return sorted(list(set(found)))