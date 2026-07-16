import re


def extract_experience(text):
    """
    Extract years of experience from resume text.
    Returns the maximum number of years found.
    """

    if not isinstance(text, str):
        return 0

    text = text.lower()

    patterns = [
        r'(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs?',
        r'(\d+)\+?\s*year'
    ]

    years = []

    for pattern in patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            try:
                years.append(int(match))
            except ValueError:
                pass

    if years:
        return max(years)

    return 0