from semantic_matcher import semantic_similarity

resume = """
Python Developer

Skills:
Python
SQL
Docker
AWS
Machine Learning
Git
"""

job = """
We are looking for a Python Developer.

Required Skills:

Python
SQL
Docker
AWS
Git
"""

score = semantic_similarity(resume, job)

print("Semantic Similarity:", score)