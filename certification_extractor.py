import re

# Certification keywords
CERTIFICATIONS = [
    "aws certified",
    "aws certified solutions architect",
    "azure administrator",
    "azure fundamentals",
    "microsoft certified",
    "google cloud",
    "google professional cloud",
    "oracle certified",
    "oracle java",
    "cisco",
    "ccna",
    "ccnp",
    "comptia",
    "security+",
    "network+",
    "pmp",
    "project management professional",
    "scrum master",
    "certified scrum master",
    "itil",
    "salesforce",
    "red hat",
    "rhce",
    "rhcsa",
    "kubernetes",
    "cka",
    "ckad",
    "tensorflow",
    "data science certification"
]


def extract_certifications(text):

    if not isinstance(text, str):
        return []

    text = text.lower()

    found = []

    for cert in CERTIFICATIONS:

        pattern = r"\b" + re.escape(cert) + r"\b"

        if re.search(pattern, text):
            found.append(cert)

    return sorted(list(set(found)))