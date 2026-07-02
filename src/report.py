from reportlab.platypus import SimpleDocTemplate, Paragraph 
from reportlab.lib.styles import getSampleStyleSheet 

def create_report(result, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = [] 

    story.append(
        Paragraph("<b>Fake Job Detection Report</b>", styles["Heading1"])


    )

    for key, value in result.items():

        story.append(
            Paragraph(f"{key}: {value}", styles["Normal"])

        )

    doc.build(story)

    