# 🤖 AI Resume Analyzer using NLP & Machine Learning

An intelligent **AI-powered Resume Screening System** that analyzes resumes against job descriptions using **Natural Language Processing, Sentence Transformers, and XGBoost Machine Learning**.

The system automatically extracts resume information, compares it with job requirements, predicts ATS compatibility, identifies missing skills, and provides improvement suggestions.

---

# 🚀 Features

## 📄 Resume Analysis

- Upload resume in PDF format
- Automatic resume text extraction
- NLP-based text preprocessing
- Resume information extraction
- Temporary processing without permanent storage

## 🧠 AI Resume Matching

Uses:

- Sentence Transformer embeddings
- Semantic similarity calculation
- Context-based resume-job matching

The system understands meaning instead of only matching exact keywords.

Example:

```
Resume:
Machine Learning Model Development

Job Description:
AI Model Building Experience
```

The model recognizes both concepts as related.

## 🔍 Information Extraction

Extracts:

✅ Technical Skills  
✅ Work Experience  
✅ Education  
✅ Certifications  

## 📊 ATS Evaluation

Generates:

- ATS Score
- Semantic Similarity Score
- Skill Match Percentage
- Experience Match
- Education Match
- Certification Match
- Matched Skills
- Missing Skills

---

# 🏗️ System Architecture

```
                 Resume PDF Upload
                         |
                         ↓
                    Flask App
                         |
                         ↓
                    PDF Parser
                         |
                         ↓
               NLP Text Processing
                         |
                         ↓
        ---------------------------------
        |              |                |
     Skills       Experience       Education
   Extraction     Extraction      Extraction
        |
        ↓
   Feature Engineering
        |
        ↓
 Sentence Transformer
        |
        ↓
 Semantic Similarity
        |
        ↓
   XGBoost Classifier
        |
        ↓
   ATS Analysis Report
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Backend

- Flask

## Machine Learning

- XGBoost
- Scikit-learn

## Natural Language Processing

- spaCy
- Sentence Transformers
- all-MiniLM-L6-v2

## Data Processing

- Pandas
- NumPy

## PDF Processing

- PyPDF2

## Frontend

- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```
AI Resume Analyzer (ML)

│
├── app.py
├── analyzer.py
├── parser.py
├── preprocessing.py
│
├── skill_extractor.py
├── experience_extractor.py
├── education_extractor.py
├── certification_extractor.py
│
├── feature_engineering.py
├── semantic_matcher.py
├── train_model.py
├── predict.py
│
├── resources/
│   ├── skills.txt
│   ├── education_keywords.txt
│   ├── certifications.txt
│   └── job_descriptions.py
│
├── datasets/
│   ├── resume_text.csv
│   ├── clean_resume.csv
│   ├── features.csv
│   └── training_data.csv
│
├── models/
│   └── xgboost_model.pkl
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
│
└── static/
    ├── css/
    └── js/
```

---

# 📊 Dataset

## Source

The original resume dataset was obtained from **Kaggle**.

Source:

https://www.kaggle.com/

---

## Resume Dataset

Total resumes:

```
2484
```

Dataset contains:

- Resume text
- Professional categories

Used for:

- NLP preprocessing
- Skill extraction
- Feature generation

---

# 🔄 Data Processing Pipeline

```
Kaggle Resume Dataset
          |
          ↓
    Text Cleaning
          |
          ↓
   NLP Processing
          |
          ↓
Information Extraction
          |
          ↓
 Feature Engineering
          |
          ↓
 ML Training Dataset
```

---

# 🧹 NLP Preprocessing

Implemented using:

```
spaCy
```

Operations:

- Lowercase conversion
- Removing emails
- Removing phone numbers
- Removing special characters
- Stopword removal
- Lemmatization

Example:

Before:

```
Developing Python Applications
```

After:

```
develop python application
```

---

# 🧩 Feature Engineering

Extracted features:

```
Skill_Count
Experience
Education_Count
Certification_Count
Resume_Length
Semantic_Score
```

Generated dataset:

```
training_data.csv
```

Size:

```
3185 samples
```

---

# 🧠 Semantic Matching

Model:

```
Sentence Transformer
all-MiniLM-L6-v2
```

Purpose:

To compare resume and job description based on meaning.

Example:

```
Resume:
Cloud deployment experience

Job:
AWS infrastructure management
```

The model identifies semantic similarity.

---

# 🤖 Machine Learning Model

## XGBoost Classifier

Selected because:

- Performs well on structured data
- Handles nonlinear relationships
- Provides strong classification results
- Efficient training

---

# 📈 Model Training Results

Dataset:

```
3185 samples
```

Train-Test Split:

| Dataset | Samples |
|---|---:|
| Training Set | 2548 |
| Testing Set | 637 |

Split:

```
80% Training
20% Testing
```

Reason:

The training set allows the model to learn patterns, while the testing set evaluates performance on unseen resumes.

---

# 🏆 Model Performance

## ATS Prediction Model

Accuracy:

```
89.17%
```

Classification Result:

```
              Precision  Recall  F1-score

Class 0          0.90     0.96     0.93

Class 1          0.83     0.64     0.72
```

Confusion Matrix:

```
[[479 18]
 [51 89]]
```

---

# 🧠 Semantic Matching Results

Sentence Transformer Performance:

```
88% - 90%
```

Example:

```
Semantic Similarity:
90.45%
```

---

# 🧪 Sample Prediction Output

```
========== ATS REPORT ==========

ATS Score:
99.51%

Semantic Score:
90.45%

Skill Match:
83.33%

Experience Match:
100%

Education Match:
100%

Certification Match:
0%


Matched Skills:

Python
SQL
AWS
Docker
Git


Missing Skills:

Kubernetes
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone <repository-url>

cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download spaCy model:

```bash
python -m spacy download en_core_web_sm
```

Run application:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# ⚠️ Limitations

- Dataset size can be increased for better generalization
- Skill extraction depends on the skill database
- Experience extraction is rule-based
- Certification matching can miss variations
- Complex PDF layouts may affect parsing
- Sentence Transformer is a general-purpose model, not recruitment-specific
- ATS score is an ML prediction and not an official company ATS score

---

# 🔮 Future Improvements

- Fine-tune Sentence Transformer on resume-job matching datasets
- Add OCR support for scanned resumes
- Improve extraction using BERT-based NLP models
- Add candidate ranking system
- Add recruiter dashboard
- Add personalized skill improvement recommendations
- Integrate job market skill trends

---

# 🎯 Project Outcome

The project successfully implements an end-to-end AI resume screening pipeline:

```
Resume PDF
     ↓
Text Extraction
     ↓
NLP Processing
     ↓
Feature Extraction
     ↓
Semantic Matching
     ↓
Machine Learning Prediction
     ↓
ATS Report
```

## Achievements

✅ Automated resume analysis  
✅ 89.17% ATS prediction accuracy  
✅ 90% semantic matching capability  
✅ Skill gap identification  
✅ Complete Flask web application  

---

# 👨‍💻 Built With

Python • NLP • Machine Learning • Flask • XGBoost • Sentence Transformers
