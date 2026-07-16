import fitz

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using PyMuPDF.
    """

    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()

    except Exception as e:
        print(f"Error reading {pdf_path}")
        print(e)

    return text