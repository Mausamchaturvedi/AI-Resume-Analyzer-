import re
import pdfplumber
import docx

EMAIL = r"[\w\.-]+@[\w\.-]+\.\w+"
PHONE = r"(?:\+?\d{1,3}[\s-]?)?\d{10}|\+?\d[\d\s\-()]{8,}\d"
LINKEDIN = r"linkedin\.com/[^\s]+"
GITHUB = r"github\.com/[^\s]+"

SECTION_HEADINGS = {
    "education": ["education", "academics", "academic background", "qualification"],
    "skills": ["skills", "technical skills", "key skills", "core competencies"],
    "experience": ["experience", "work experience", "internship", "internships",
                   "professional experience", "employment"],
    "projects": ["projects", "academic projects", "personal projects"],
    "certifications": ["certifications", "certificates", "courses"],
    "summary": ["summary", "objective", "career objective", "profile", "about me"],
}

def extract_text(file, filename):
    """Read text from an uploaded PDF or DOCX file."""
    name = filename.lower()
    if name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join((page.extract_text() or "") for page in pdf.pages)
    if name.endswith(".docx"):
        document = docx.Document(file)
        return "\n".join(p.text for p in document.paragraphs)
    raise ValueError("Please upload a PDF or DOCX file.")


def extract_contact(text):
    """Find email, phone, LinkedIn and GitHub links."""
    low = text.lower()
    return {
        "email": bool(re.search(EMAIL, text)),
        "phone": bool(re.search(PHONE, text)),
        "linkedin": bool(re.search(LINKEDIN, low)),
        "github": bool(re.search(GITHUB, low)),
    }


def split_sections(text):
    """Split resume text into sections based on heading lines."""
    sections = {name: "" for name in SECTION_HEADINGS}
    current = None
    for line in text.splitlines():
        clean = re.sub(r"[^a-z ]", "", line.lower()).strip()
        matched = None
        if clean and len(clean) < 35:
            for name, words in SECTION_HEADINGS.items():
                if clean in words:
                    matched = name
                    break
        if matched:
            current = matched
        elif current:
            sections[current] += line + "\n"
    return sections