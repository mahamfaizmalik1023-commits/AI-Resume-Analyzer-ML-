from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(resume_text, job_description):
    """
    Compute semantic similarity between resume and job description.
    Returns a similarity score between 0 and 100.
    """

    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(similarity * 100, 2)