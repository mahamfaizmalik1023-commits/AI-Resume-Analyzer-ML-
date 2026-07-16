from predict import predict_resume

resume = """
Python Developer

Skills:
Python
SQL
Docker
AWS
Git
Machine Learning

Education:
Bachelor of Computer Science

Experience:
3 years experience

Certifications:
AWS Certified Developer
"""

job = """
We are looking for a Python Developer.

Required Skills:
Python
SQL
AWS
Docker
Git
Kubernetes

Education:
Bachelor Degree

Experience:
3 years experience

Certification:
AWS Certification preferred
"""

result = predict_resume(resume, job)

print("\n" + "=" * 50)
print("ATS ANALYSIS")
print("=" * 50)

for key, value in result.items():
    print(f"{key}: {value}")