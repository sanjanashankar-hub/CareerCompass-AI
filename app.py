import streamlit as st
from reportlab.pdfgen import canvas
from recommendation import calculate_match
from assessment import calculate_score
from roadmap import show_roadmap
from resources import show_resources

if "guidance_done" not in st.session_state:
    st.session_state.guidance_done = False
from database import save_result
import pandas as pd

career_data = pd.read_csv("careers.csv")

st.set_page_config(

    page_title="AI Career Guidance",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<div style="background: linear-gradient(135deg, #7C3AED, #4F46E5);
padding: 30px; border-radius: 15px; color: white; text-align: center;">
<h1 style="color: white;">Welcome to CareerCompass AI 🚀</h1>
<p style="font-size: 18px;">Discover your strengths, explore career paths, and build your future.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; gap: 15px; margin-top: 20px;">

<div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #E5E7EB; flex: 1;">
<h3 style="color: #7C3AED;">🔎 Explore Careers</h3>
<p style="color: #475569;">Discover career paths that match your interests and skills.</p>
</div>

<div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #E5E7EB; flex: 1;">
<h3 style="color: #7C3AED;">🧠 Assess Your Skills</h3>
<p style="color: #475569;">Understand your strengths and identify skills to improve.</p>
</div>

<div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #E5E7EB; flex: 1;">
<h3 style="color: #7C3AED;">🗺️ Build Your Roadmap</h3>
<p style="color: #475569;">Create a step-by-step plan for your future career.</p>
</div>

</div>
""", unsafe_allow_html=True)
st.title("🎓 AI Career Guidance")
st.write("Find career options based on your interests and skills.")

st.divider()

name = st.text_input("👤 Enter your name")

interest = st.selectbox(
    "💡 What are you interested in?",
    [
        "Select an interest",
        "Technology",
        "Cybersecurity",
        "Business",
        "Teaching",
        "Design",
        "Healthcare"
    ]
)

skill = st.selectbox(
    "⭐ What is your strongest skill?",
    [
        "Select a skill",
        "Communication",
        "Problem Solving",
        "Creativity",
        "Leadership",
        "Technical Skills"
    ]
)

work = st.selectbox(
    "💼 What type of work do you prefer?",
    [
        "Select work preference",
        "Work from home",
        "Office work",
        "Hybrid work"
    ]
)
st.subheader("🧠 Career Assessment")

q1 = st.radio(
    "1. Which activity do you enjoy most?",
    [
        "Solving technical problems",
        "Helping and communicating with people",
        "Creating designs and visuals",
        "Managing and organizing things"
    ]
)

q2 = st.radio(
    "2. Which subject do you enjoy most?",
    [
        "Computer Science",
        "Business",
        "Arts and Design",
        "Teaching and Education"
    ]
)

q3 = st.radio(
    "3. What type of task do you prefer?",
    [
        "Working with computers",
        "Working with people",
        "Creating new ideas",
        "Planning and managing"
    ]
)
if st.button("🔍 Get Career Guidance") or st.session_state.guidance_done:

    score = calculate_score(q1, q2, q3)

    if name == "" or interest == "Select an interest" or skill == "Select a skill" or work == "Select work preference":
        st.warning("Please answer        all the questions.")

    else:
        st.session_state.guidance_done = True
        st.success(f"Hello {name}! Here are some career options for you.")

        st.subheader("👤 Your Career Profile")

        st.write("**Name:**", name)
        st.write("**Interest:**", interest)
        st.write("**Strongest Skill:**", skill)
        st.write("**Work Preference:**", work)
        st.write("**Assessment Score:**", score)
        save_result(name, interest, skill, work, score)

        if q1 == "Solving technical problems" or q2 == "Computer Science" or q3 == "Working with computers":
            category = "Technology"

        elif q1 == "Helping and communicating with people" or q3 == "Working with people":
            category = "People"

        elif q1 == "Creating designs and visuals" or q2 == "Arts and Design" or q3 == "Creating new ideas":
            category = "Creative"

        else:
            category = "Business"
# Better career recommendation based on assessment
        if interest == "Cybersecurity" or (
            q1 == "Solving technical problems"
            and q2 == "Computer Science"
            and q3 == "Working with computers"
        ):
            careers = [
                "Cybersecurity Analyst",
                "Security Specialist",
                "Cyber Forensics Analyst"
            ]

        elif interest == "Technology":
            careers = [
                "IT Support Specialist",
                "Web Developer",
                "Software Tester"
            ]

        elif interest == "Business" or (
            q1 == "Managing and organizing things"
            or q2 == "Business"
            or q3 == "Planning and managing"
        ):
            careers = [
                "Business Analyst",
                "Marketing Executive",
                "HR Executive"
            ]

        elif interest == "Teaching" or (
            q1 == "Helping and communicating with people"
            or q2 == "Teaching and Education"
            or q3 == "Working with people"
        ):
            careers = [
                "Teacher",
                "Tutor",
                "Lecturer"
            ]

        elif interest == "Design" or (
            q1 == "Creating designs and visuals"
            or q2 == "Arts and Design"
            or q3 == "Creating new ideas"
        ):
            careers = [
                "UI/UX Designer",
                "Graphic Designer",
                "Web Designer"
            ]

        elif interest == "Healthcare":
            careers = [
                "Healthcare Administrator",
                "Medical Coder",
                "Health Information Technician"
            ]

        else:
            careers = [
                "IT Support Specialist",
                "Data Entry Specialist",
                "Administrative Assistant"
            ]
        st.session_state.careers = careers
        st.subheader("🎯 Recommended Career Options")
        for career in careers:
            match_percentage = calculate_match(
    career,
    interest,
    skill,
    q1,
    q2,
    q3
)

            st.write(f"✅ {career} — {match_percentage}% Match")
            st.progress(match_percentage / 100)



        st.subheader("📚 Career Details")
        career_details = {
            "Cybersecurity Analyst": {
                "Qualification": "BCA, B.Sc. Cybersecurity or related degree",
                "Skills": "Networking, Security Basics, Problem Solving",
                "Learning": "Cybersecurity, Networking, Ethical Hacking",
                "Job": "IT Companies, Security Firms, Banks"
            },

            "Security Specialist": {
                "Qualification": "Degree in Cybersecurity, IT or Computer Science",
                "Skills": "Network Security, Risk Analysis, Problem Solving",
                "Learning": "Information Security, Network Security",
                "Job": "IT Companies, Banks, Security Organizations"
            },

            "Cyber Forensics Analyst": {
                "Qualification": "Degree in Cybersecurity, Digital Forensics or related field",
                "Skills": "Investigation, Computer Skills, Attention to Detail",
                "Learning": "Digital Forensics, Cybercrime Investigation",
                "Job": "Cybersecurity Firms, Police Departments, Forensic Labs"
            },

            "IT Support Specialist": {
                "Qualification": "BCA, B.Sc. Computer Science or related degree",
                "Skills": "Troubleshooting, Communication, Computer Skills",
                "Learning": "Computer Networks, Hardware, Operating Systems",
                "Job": "IT Companies, Schools, Offices"
            },

            "Web Developer": {
                "Qualification": "BCA, B.Sc. Computer Science or related degree",
                "Skills": "HTML, CSS, JavaScript, Problem Solving",
                "Learning": "Web Development, Frontend and Backend",
                "Job": "IT Companies, Web Agencies, Freelance"
            },

            "Software Tester": {
                "Qualification": "BCA, B.Sc. Computer Science or related degree",
                "Skills": "Testing, Problem Solving, Attention to Detail",
                "Learning": "Software Testing, Manual Testing, Automation Basics",
                "Job": "Software Companies, IT Companies"
            },

            "Business Analyst": {
                "Qualification": "BCA, BBA, B.Com or related degree",
                "Skills": "Communication, Problem Solving, Analytical Skills",
                "Learning": "Business Analysis, Excel, SQL",
                "Job": "IT Companies, Consulting Firms, Businesses"
            },

            "Marketing Executive": {
                "Qualification": "BBA, B.Com, BA or related degree",
                "Skills": "Communication, Creativity, Marketing Skills",
                "Learning": "Digital Marketing, Social Media Marketing",
                "Job": "Marketing Agencies, Companies, Startups"
            },

            "HR Executive": {
                "Qualification": "BBA, B.Com, BA or related degree",
                "Skills": "Communication, Organization, People Skills",
                "Learning": "Human Resources, Recruitment, Payroll Basics",
                "Job": "Companies, HR Departments, Recruitment Firms"
            },

            "Teacher": {
                "Qualification": "Relevant degree with required teaching qualification",
                "Skills": "Communication, Patience, Presentation",
                "Learning": "Teaching Methods, Subject Knowledge",
                "Job": "Schools, Educational Institutions"
            },

            "Tutor": {
                "Qualification": "Degree or subject-specific qualification",
                "Skills": "Communication, Teaching, Patience",
                "Learning": "Teaching Methods, Online Teaching",
                "Job": "Coaching Centers, Online Platforms, Private Tutoring"
            },

            "Lecturer": {
                "Qualification": "Postgraduate degree in the relevant subject",
                "Skills": "Communication, Presentation, Subject Knowledge",
                "Learning": "Advanced Subject Knowledge, Teaching Methods",
                "Job": "Colleges, Universities, Educational Institutions"
            },

            "UI/UX Designer": {
                "Qualification": "Degree or diploma in Design, Computer Science or related field",
                "Skills": "Creativity, Design Thinking, Communication",
                "Learning": "UI/UX Design, Figma, User Research",
                "Job": "IT Companies, Design Agencies, Startups"
            },

            "Graphic Designer": {
                "Qualification": "Degree or diploma in Graphic Design or related field",
                "Skills": "Creativity, Visual Design, Communication",
                "Learning": "Graphic Design, Photoshop, Illustrator",
                "Job": "Design Agencies, Companies, Freelance"
            },

            "Web Designer": {
                "Qualification": "Degree or diploma in Web Design or related field",
                "Skills": "HTML, CSS, Creativity, Design",
                "Learning": "Web Design, UI Design, HTML and CSS",
                "Job": "IT Companies, Web Agencies, Freelance"
            },

            "Healthcare Administrator": {
                "Qualification": "BCA, BBA, Healthcare Management or related degree",
                "Skills": "Communication, Management, Computer Skills",
                "Learning": "Healthcare Management, Hospital Administration",
                "Job": "Hospitals, Clinics, Healthcare Companies"
            },

            "Medical Coder": {
                "Qualification": "Any degree with Medical Coding training",
                "Skills": "Medical Terminology, Computer Skills, Attention to Detail",
                "Learning": "Medical Coding, ICD and CPT basics",
                "Job": "Hospitals, Medical Coding Companies, RCM Companies"
            },

            "Health Information Technician": {
                "Qualification": "Degree or diploma in Health Information Management",
                "Skills": "Data Management, Computer Skills, Accuracy",
                "Learning": "Health Information Systems, Medical Records",
                "Job": "Hospitals, Clinics, Healthcare Organizations"
            },

            "Data Entry Specialist": {
                "Qualification": "12th pass or any degree",
                "Skills": "Typing, Computer Skills, Accuracy",
                "Learning": "MS Office, Excel, Data Management",
                "Job": "Companies, Offices, BPOs"
            },

            "Administrative Assistant": {
                "Qualification": "12th pass or any degree",
                "Skills": "Organization, Communication, Computer Skills",
                "Learning": "MS Office, Documentation, Office Administration",
                "Job": "Companies, Schools, Offices"
            }
        }
        for career in careers:
            if career in career_details:
                st.write("### 💼", career)
                st.write("🎓 **Qualification:**", career_details[career]["Qualification"])
                st.write("🛠️ **Skills:**", career_details[career]["Skills"])
                st.write("📚 **What to Learn:**", career_details[career]["Learning"])
                st.write("🏢 **Job Opportunities:**", career_details[career]["Job"])
                st.write(
    "💡 **Why this career matches you:** "
    f"You selected {interest} as your interest, "
    f"{skill} as your strongest skill, "
    f"and prefer {work.lower()}."
)
                st.divider()

        selected_career = careers[0]
        show_roadmap(selected_career)
        career_row = career_data[career_data["Career"] == selected_career]

        st.subheader("🛣️ Career Roadmap")
        st.subheader("📚 Learning Resources")
        selected_career = careers[0]

        show_resources(selected_career)
       

        
        st.subheader("🔍 Skill Gap Analysis")
if "career_row" in locals() and not career_row.empty:
            required_skills = career_row.iloc[0]["Skills"].split(";")

            st.write(f"### Skills required for {selected_career}")

            for required_skill in required_skills:
                if required_skill.strip().lower() in skill.lower():
                    st.success(f"✅ {required_skill.strip()}")
                else:
                    st.warning(f"⚠️ {required_skill.strip()}")
                    

comparison_careers = st.multiselect(
    "Select careers to compare:",
    st.session_state.careers if "careers" in st.session_state else [],
    max_selections=3
)

if comparison_careers:
    comparison_data = career_data[
        career_data["Career"].isin(comparison_careers)
    ]

    st.dataframe(
        comparison_data[
            ["Career", "Qualification", "Skills", "Learning", "Job Opportunities"]
        ],
        use_container_width=True
    )
st.subheader("📄 Career Report")

if st.button("📥 Generate Career Report"):

    pdf_file = "AI_Career_Guidance_Report.pdf"
    c = canvas.Canvas(pdf_file, pageCompression=1)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 800, "AI CAREER GUIDANCE REPORT")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 760, "PERSONAL INFORMATION")

    c.setFont("Helvetica", 11)
    c.drawString(50, 735, f"Name: {name}")
    c.drawString(50, 715, f"Interest: {interest}")
    c.drawString(50, 695, f"Strongest Skill: {skill}")
    c.drawString(50, 675, f"Work Preference: {work}")

    score = calculate_score(q1, q2, q3)
    c.drawString(50, 655, f"Assessment Score: {score}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 615, "RECOMMENDED CAREERS")

    y = 590
    c.setFont("Helvetica", 11)

    careers = st.session_state.get("careers", [])

    if careers:
        for career in careers:
            match_percentage = calculate_match(
                career,
                interest,
                skill,
                q1,
                q2,
                q3
            )

            if y < 100:
                c.showPage()
                y = 800
                c.setFont("Helvetica", 11)

            c.drawString(
                50,
                y,
                f"{career} - {match_percentage}% Match"
            )
            y -= 22
    else:
        c.drawString(50, y, "No careers found. Complete the assessment first.")
        y -= 22

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 10, "CAREER ROADMAP")

    y -= 35
    c.setFont("Helvetica", 11)

    roadmap = [
        "Step 1: Learn Computer Networking",
        "Step 2: Learn Cybersecurity Basics",
        "Step 3: Learn Ethical Hacking",
        "Step 4: Practise with Cybersecurity Tools",
        "Step 5: Prepare for Cybersecurity Jobs"
    ]

    for step in roadmap:
        if y < 60:
            c.showPage()
            y = 800
            c.setFont("Helvetica", 11)

        c.drawString(50, y, step)
        y -= 22

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 10, "SKILL GAP ANALYSIS")

    y -= 35
    c.setFont("Helvetica", 11)

    for item in ["Networking", "Security Basics", "Problem Solving"]:
        if y < 60:
            c.showPage()
            y = 800
            c.setFont("Helvetica", 11)

        c.drawString(50, y, item)
        y -= 22

    c.save()

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="⬇️ Download PDF Career Report",
            data=file.read(),
            file_name="AI_Career_Guidance_Report.pdf",
            mime="application/pdf"
        )

   
    
