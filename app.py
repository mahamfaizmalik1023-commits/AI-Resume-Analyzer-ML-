from flask import Flask, render_template, request
import os
import tempfile

from analyzer import analyze_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    job_description = request.form["job_description"]

    # Create a temporary PDF file
    suffix = os.path.splitext(resume.filename)[1] or ".pdf"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        resume.save(temp_file.name)
        temp_path = temp_file.name

    try:
        result = analyze_resume(
            temp_path,
            job_description
        )
    finally:
        # Delete the temporary file after analysis
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)