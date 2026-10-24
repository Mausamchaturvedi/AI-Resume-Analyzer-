import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extend this list with more skills for better results
SKILLS = [
    "python", "java", "javascript", "typescript", "c++", "c#", "sql", "mysql",
    "postgresql", "mongodb", "html", "css", "react", "angular", "node.js",
    "django", "flask", "spring", "git", "github", "docker", "kubernetes", "aws",
    "azure", "linux", "machine learning", "deep learning", "nlp", "tensorflow",
    "pytorch", "pandas", "numpy", "scikit-learn", "data analysis", "excel",
    "power bi", "tableau", "rest api", "data structures", "algorithms", "oop",
    "communication", "teamwork", "leadership", "problem solving",
]

ACTION_VERBS = [
    "developed", "built", "designed", "implemented", "created", "led", "managed",
    "improved", "reduced", "increased", "analyzed", "optimized", "launched",
    "automated", "deployed", "collaborated", "organized", "achieved", "delivered",
]


def find_skills(text):
    low = text.lower()
    found = []
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, low):
            found.append(skill)
    return found


def jd_match(resume_text, jd_text):
    """TF-IDF cosine similarity between resume and job description (0-100)."""
    vec = TfidfVectorizer(stop_words="english")
    matrix = vec.fit_transform([resume_text, jd_text])
    return round(float(cosine_similarity(matrix[0], matrix[1])[0][0]) * 100, 1)


def score_resume(text, contact, sections, jd_text=""):
    tips = []
    breakdown = {}

    # 1. Contact info (10)
    pts = 4 * contact["email"] + 3 * contact["phone"] + 3 * (contact["linkedin"] or contact["github"])
    breakdown["Contact info"] = (pts, 10)
    if not contact["email"]:
        tips.append("Add a professional email address.")
    if not contact["phone"]:
        tips.append("Add a phone number.")
    if not (contact["linkedin"] or contact["github"]):
        tips.append("Add your LinkedIn or GitHub link.")

    # 2. Section completeness (20)
    required = ["education", "skills", "experience", "projects"]
    pts = 0
    for name in required:
        if sections[name].strip():
            pts += 5
        else:
            tips.append(f"Add a clear '{name.title()}' section.")
    breakdown["Sections"] = (pts, 20)

    # 3. Skills (30)
    resume_skills = find_skills(text)
    missing = []
    if jd_text.strip():
        jd_skills = find_skills(jd_text)
        if jd_skills:
            matched = [s for s in jd_skills if s in resume_skills]
            missing = [s for s in jd_skills if s not in resume_skills]
            pts = round(len(matched) / len(jd_skills) * 30, 1)
        else:
            pts = min(len(resume_skills) / 10, 1) * 30
        if missing:
            tips.append("Missing skills from the job description: " + ", ".join(missing))
    else:
        pts = round(min(len(resume_skills) / 10, 1) * 30, 1)
        if len(resume_skills) < 10:
            tips.append("List more relevant technical skills (aim for 10+).")
    breakdown["Skills"] = (pts, 30)

    # 4. Experience / project quality (25)
    body = (sections["experience"] + " " + sections["projects"]).lower()
    verbs = sum(1 for v in ACTION_VERBS if v in body)
    numbers = len(re.findall(r"\d+%?", body))
    pts = round(min(verbs / 8, 1) * 15 + min(numbers / 5, 1) * 10, 1)
    breakdown["Experience quality"] = (pts, 25)
    if verbs < 5:
        tips.append("Start bullet points with action verbs (developed, built, led...).")
    if numbers < 3:
        tips.append("Add measurable results, e.g. 'improved speed by 30%'.")

    # 5. Length (15)
    words = len(text.split())
    if 300 <= words <= 800:
        pts = 15
    elif words < 300:
        pts = round(words / 300 * 15, 1)
        tips.append("Resume looks too short. Add more detail.")
    else:
        pts = max(0, round(15 - (words - 800) / 100, 1))
        tips.append("Resume looks too long. Keep it to 1-2 pages.")
    breakdown["Length"] = (pts, 15)

    total = round(sum(p for p, _ in breakdown.values()), 1)
    return {
        "total": total,
        "breakdown": breakdown,
        "skills_found": resume_skills,
        "tips": tips,
        "jd_match": jd_match(text, jd_text) if jd_text.strip() else None,
    }