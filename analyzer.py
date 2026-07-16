from parser import extract_text_from_pdf
from preprocessing import preprocess_text
from predict import predict_resume


def analyze_resume(pdf_path, job_description):
    """
    Analyze a resume against a job description.
    """

    # Extract text from PDF
    resume_text = extract_text_from_pdf(pdf_path)

    # Clean text
    clean_resume = preprocess_text(resume_text)

    # Predict ATS score
    result = predict_resume(
        clean_resume,
        job_description
    )

    return result