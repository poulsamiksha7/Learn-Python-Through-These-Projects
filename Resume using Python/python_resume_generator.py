from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER
from datetime import datetime

file_name = r"D:\Projects 2026\Python Projects\Resume using Python\Samiksha_Poul_Resume.pdf"

doc = SimpleDocTemplate(
    file_name,
    pagesize=A4,
    rightMargin=36,
    leftMargin=36,
    topMargin=24,
    bottomMargin=24
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "name",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=18,
    spaceAfter=6
)

center_style = ParagraphStyle(
    "center",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    spaceAfter=6
)

section_style = ParagraphStyle(
    "section",
    parent=styles["Normal"],
    fontSize=11,
    leading=14,
    spaceBefore=8,
    spaceAfter=4,
    fontName="Helvetica-Bold"
)

normal = ParagraphStyle(
    "normal",
    parent=styles["Normal"],
    fontSize=9.5,
    leading=12
)

bold = ParagraphStyle(
    "bold",
    parent=styles["Normal"],
    fontSize=9.5,
    leading=12,
    fontName="Helvetica-Bold"
)

story = []

story.append(Paragraph("SAMIKSHA POUL", name_style))
story.append(Paragraph("Nanded, Maharashtra, India", center_style))
story.append(Paragraph(
    'samikshapoul@gmail.com | www.linkedin.com/in/samiksha-poul | github.com/poulsamiksha7',
    center_style
))
story.append(Spacer(1, 6))

story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
story.append(Paragraph(
    "MCA student and Python Backend Developer with hands-on experience building 25+ real-world applications. "
    "Specialized in backend logic, automation tools, and database-driven systems using Python and SQL. "
    "Demonstrated consistent delivery through daily coding practice and GitHub version control. "
    "Seeking internship opportunities in Backend Development.",
    normal
))

story.append(Spacer(1, 4))
story.append(Paragraph("TECHNICAL SKILLS", section_style))
skills = [
    "Languages: Python, SQL, HTML, CSS, JavaScript",
    "Backend: Backend Development, Application Logic Design, CRUD Operations, File Handling",
    "Databases: SQL (MySQL, Database Connectivity)",
    "Web: HTML, CSS, JavaScript, Bootstrap, PHP",
    "Tools: GitHub, Version Control, Debugging, Input Validation, XAMPP",
]
for s in skills:
    story.append(Paragraph(s, normal))

story.append(Spacer(1, 4))
story.append(Paragraph("PROJECTS", section_style))

def project(title, date, meta, bullets):
    story.append(Paragraph(f"<b>{title}</b> &nbsp;&nbsp; <i>{date}</i>", normal))
    story.append(Paragraph(meta, normal))
    story.append(ListFlowable(
        [ListItem(Paragraph(b, normal)) for b in bullets],
        bulletType="bullet",
        start="circle",
        leftIndent=12
    ))
    story.append(Spacer(1, 3))

project(
    "30 Days 30 Projects - HTML & CSS",
    "Sep 2025",
    "Frontend Development | GitHub: poulsamiksha7/30-Days-30-HTML-CSS",
    [
        "Built 30 responsive UI projects strengthening frontend fundamentals with HTML and CSS structured layouts",
        "Practiced daily delivery improving consistency and problem-solving through interface development from scratch",
    ]
)

project(
    "21 Days 21 Python Projects",
    "Jul 2025 - Aug 2025",
    "Python Development | GitHub: poulsamiksha7/21_Days_21_Python_Projects",
    [
        "Developed 21 Python applications including ATM simulation, authentication modules, and productivity utilities",
        "Implemented file handling, input validation, and workflow logic improving debugging and clean coding practices",
    ]
)

project(
    "Portfolio Website",
    "Dec 2024 - Jan 2025",
    "Full-Stack Development | HTML, CSS, Bootstrap, PHP, MySQL",
    [
        "Built responsive personal portfolio with integrated PHP and MySQL backend using XAMPP for database connectivity",
        "Designed project showcase system with clean UI/UX for professional presentation and dynamic content management",
    ]
)

project(
    "E-Pharmacy Website",
    "Mar 2024",
    "Full-Stack E-Commerce | HTML, CSS, Bootstrap, PHP, SQL",
    [
        "Developed e-commerce pharmacy platform with secure login, product management, and order processing",
        "Designed database schema for user authentication, product catalog, and order management with CRUD operations",
    ]
)

project(
    "MealsPoint - Food Ordering App",
    "Feb 2024",
    "Web Application | HTML, CSS, JavaScript, Backend Logic",
    [
        "Built meal ordering web application with dynamic menu selection, order tracking, and responsive UI",
        "Implemented backend workflow logic for order processing and state management with seamless user experience",
    ]
)

story.append(Paragraph("EDUCATION", section_style))
story.append(Paragraph("Master of Computer Applications (MCA) - Jan 2024 - May 2026", normal))
story.append(Paragraph("Swami Ramanand Teerth Marathwada University", normal))
story.append(Spacer(1, 2))
story.append(Paragraph("Bachelor of Computer Applications (BCA), Computer Science - Sep 2021 - May 2024", normal))
story.append(Paragraph("Swami Ramanand Teerth Marathwada University", normal))

story.append(Spacer(1, 4))
story.append(Paragraph("CERTIFICATIONS", section_style))
story.append(Paragraph("Python AI | SQL | Skill Academy Certified Python", normal))

doc.build(story)

print("✅ Resume PDF generated successfully:", file_name)
