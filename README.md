# 📄 AI Resume Analyzer

An intelligent resume analysis web application built using **Python and Streamlit** that helps users evaluate their resumes, identify skills, receive improvement suggestions, and compare their resumes against specific job descriptions.

## 🚀 Project Overview

AI Resume Analyzer is a Python-based application designed to simplify the resume evaluation process. Users can upload their resumes in PDF or DOCX format and optionally provide a job description for comparison.

The application analyzes the uploaded resume and displays an overall score, job description match percentage, detected skills, category-wise score breakdown, and suggestions for improvement.

## ✨ Features

- **Resume Upload:** Upload resumes in PDF and DOCX formats.
- **Resume Text Extraction:** Extract readable text from uploaded documents.
- **Resume Scoring:** Calculate an overall resume score out of 100.
- **Job Description Matching:** Compare resume content with a provided job description.
- **Skills Detection:** Identify skills mentioned in the resume.
- **Section Analysis:** Process different sections of the resume.
- **Score Breakdown:** Display category-wise scores using progress bars.
- **Improvement Suggestions:** Provide recommendations to improve resume quality.
- **Error Handling:** Handle unreadable files and insufficient extracted text.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| PDF Processing | Extract text from PDF resumes |
| DOCX Processing | Extract text from Word resumes |
| Python Modules | Resume parsing and scoring |

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py              # Main Streamlit application
├── parser.py           # Resume text and section extraction
├── scorer.py           # Resume scoring and analysis
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

*Note: The parser.py, scorer.py and requirements.txt files should be included in the repository.*

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Resume-Analyzer
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install streamlit
```

Install the additional packages required by your `parser.py` and `scorer.py` modules.

If you have a requirements.txt file, use:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🖥️ How to Use

1. Open the AI Resume Analyzer application.
2. Upload your resume in PDF or DOCX format.
3. Paste a job description in the provided text area (optional).
4. Click the **Analyze** button.
5. Wait for the resume analysis to complete.
6. Review your overall resume score.
7. Check the job description match percentage, if available.
8. Review detected skills and category-wise scores.
9. Follow the suggestions to improve your resume.

## 📊 Analysis Output

The application provides the following results:

| Analysis Component | Description |
|---|---|
| Overall Score | Resume score out of 100 |
| Job Description Match | Percentage match with the provided job description |
| Score Breakdown | Category-wise resume evaluation |
| Skills Found | Skills detected in the resume |
| Suggestions | Recommendations for improvement |

## 🔄 Application Workflow

```text
       Start
         |
         v
   Open Application
         |
         v
    Upload Resume
         |
         v
  Enter Job Description
       (Optional)
         |
         v
    Click Analyze
         |
         v
   Extract Resume Text
         |
         v
    Validate Text
         |
         v
   Analyze Resume
         |
         v
   Calculate Score
         |
         v
  Display Analysis Results
         |
         v
        End
```

## 🎯 Project Objectives

- Automate basic resume evaluation.
- Help job seekers understand their resume quality.
- Identify relevant skills and resume sections.
- Compare resume content with job requirements.
- Provide useful suggestions for resume improvement.
- Demonstrate practical Python application development.

## 🔮 Future Enhancements

- Integration with advanced AI/NLP models.
- OCR support for scanned resumes.
- Downloadable resume analysis reports in PDF format.
- Resume recommendations based on specific job roles.
- User login and registration system.
- Resume history and analysis dashboard.
- Advanced keyword and ATS compatibility analysis.

## ⚠️ Limitations

- Scanned resumes may not be readable without OCR support.
- Analysis accuracy depends on the resume parsing and scoring modules.
- Automated resume scores should be treated as guidance rather than a guarantee of recruitment success.
- The application does not make final hiring decisions.

## 🎓 Academic Project Details

| Detail | Information |
|---|---|
| Project Name | AI Resume Analyzer |
| Project Type | Python Project |
| Programming Language | Python |
| Framework | Streamlit |
| Course | Master of Computer Applications (MCA) |
| University | Chandigarh University |
| Academic Session | 2026–2027 |

## 👨‍💻 Author

**Mausam Chaturvedi**

Master of Computer Applications (MCA)  
Chandigarh University, Punjab, India

## 📜 License

This project is developed for educational and academic purposes. You may modify and improve it with appropriate attribution.

---

⭐ **If you find this project useful, consider giving this repository a star!**
