import streamlit as st
from parser import extract_text, extract_contact, split_sections
from scorer import score_resume

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
st.title("📄 Resume Analyzer")

file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
jd = st.text_area("Paste a job description (optional)", height=150)

if st.button("Analyze") and file:
    try:
        text = extract_text(file, file.name)
    except Exception as e:
        st.error(f"Could not read file: {e}")
        st.stop()

    if len(text.strip()) < 50:
        st.error("No text found. The file may be a scanned image.")
        st.stop()

    result = score_resume(text, extract_contact(text), split_sections(text), jd)

    st.metric("Overall score", f"{result['total']} / 100")
    if result["jd_match"] is not None:
        st.metric("Job description match", f"{result['jd_match']}%")

    st.subheader("Breakdown")
    for name, (pts, mx) in result["breakdown"].items():
        st.write(f"**{name}**: {pts} / {mx}")
        st.progress(min(pts / mx, 1.0))

    st.subheader("Skills found")
    st.write(", ".join(result["skills_found"]) or "None detected")

    st.subheader("Suggestions")
    for tip in result["tips"] or ["Looks good!"]:
        st.write("• " + tip)