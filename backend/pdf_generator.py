from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(data, filename="analysis_report.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Code Flow Mapper Report", styles["Title"]))
    content.append(Spacer(1, 12))

    # Functions
    content.append(Paragraph("Functions", styles["Heading2"]))
    for f in data["functions"]:
        content.append(
            Paragraph(
                f"{f['name']} - {f['explanation']}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # Classes
    content.append(Paragraph("Classes", styles["Heading2"]))
    for c in data["classes"]:
        content.append(
            Paragraph(
                c["name"],
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # Imports
    content.append(Paragraph("Imports", styles["Heading2"]))
    for imp in data["imports"]:
        content.append(
            Paragraph(
                imp,
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # Viva Questions
    content.append(Paragraph("Viva Questions", styles["Heading2"]))
    for q in data["viva_questions"]:
        content.append(
            Paragraph(
                f"Q: {q['question']}<br/>A: {q['answer']}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # Project Tree
    content.append(Paragraph("Project Tree", styles["Heading2"]))
    for item in data["project_tree"]:
        content.append(
            Paragraph(
                item,
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # Flowchart
    content.append(Paragraph("Flowchart", styles["Heading2"]))
    for item in data["flowchart"]:
        content.append(
            Paragraph(
                item,
                styles["BodyText"]
            )
        )

    doc.build(content)

    return filename