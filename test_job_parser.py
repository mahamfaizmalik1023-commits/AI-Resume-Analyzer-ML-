from job_parser import parse_job

job = """
We are looking for a Python Developer.

Requirements:

Python
SQL
Docker
AWS
Machine Learning

Bachelor Degree

3 years experience

AWS Certification preferred.
"""

result = parse_job(job)

print(result)