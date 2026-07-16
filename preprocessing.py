import re
import spacy

# Create a blank English NLP pipeline
nlp = spacy.blank("en")


def preprocess_text(text):

    if text is None:
        return ""

    text = str(text).lower()

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    doc = nlp(text)

    words = []

    for token in doc:
        if not token.is_space:
            words.append(token.text)

    return " ".join(words)