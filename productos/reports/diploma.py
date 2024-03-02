from fpdf import FPDF


def generate_Diploma(data):

    pdf = FPDF('landscape', 'mm', 'A4')
    pdf.set_page_background('./static/img/fondo-diploma.jpg')
    pdf.add_page()
    
    # font weigh bold
    pdf.set_font("Arial", size=25, style = "B")
    pdf.cell(270, 35, text="Diploma", ln=True, align="C")

    
    return pdf.output()
