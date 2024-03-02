from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./static/img/logo.jpg", 10, 5, 20, 20)
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30, 10, "TITULO EMPRESA", align="C")
        self.ln(20)
        self.cell(190, 0, "", "T")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.cell(190, 0, "", "T")
        self.ln(0)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 5, f"Pagina {self.page_no()}/{{nb}}", align="C")

def generate_pdf_productos(data):

    pdf = PDF('portrait', 'mm', 'A4')
    pdf.add_page()
    # font weigh bold
    pdf.set_font("Arial", size=15, style = "B")
    pdf.cell(200, 15, text="Reporte de productos", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    with pdf.table() as table:
        row_head = table.row()
        row_head.cell("Nombre")
        row_head.cell("Proveedor")
        row_head.cell("Stock")
        row_head.cell("Imagen")
        row_head.cell("Precio", align="R")

        for producto in data:
            row = table.row()
            row.cell(producto.nombre)
            row.cell(producto.proveedor)
            row.cell(str(producto.stock), align="C")
            row.cell(img='.'+producto.imagen.url, img_fill_width=True)
            row.cell('S/.'+str(producto.precio), align="R")
    
    return pdf.output()


