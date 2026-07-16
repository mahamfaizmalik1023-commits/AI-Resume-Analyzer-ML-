import re

# Education keywords
EDUCATION_KEYWORDS = [
    "phd",
    "doctor of philosophy",
    "master",
    "masters",
    "m.sc",
    "msc",
    "m.tech",
    "mtech",
    "mba",
    "bachelor",
    "bachelors",
    "b.sc",
    "bsc",
    "b.tech",
    "btech",
    "be",
    "bs",
    "associate",
    "diploma",
    "intermediate",
    "high school",
    "matric"
]


def extract_education(text):

    if not isinstance(text, str):
        return []

    text = text.lower()

    found = []

    for keyword in EDUCATION_KEYWORDS:

        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, text):
            found.append(keyword)

    return sorted(list(set(found)))