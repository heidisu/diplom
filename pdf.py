from fpdf import FPDF

def create_certificate(name, title, subtitle, text, image, out_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 20, ln=1)
    pdf.cell(0, 0, title, align='C')
    pdf.cell(0,15, ln=1)
    pdf.set_font('Arial', '', 18)
    pdf.cell(0,0, subtitle, align='C')
    pdf.cell(0, 15, ln=1)
    pdf.set_font('Arial', 'U', 18)
    pdf.cell(0, 0, name, align='C')
    pdf.cell(0,15, ln=1)
    pdf.set_font('Arial', '', 18)
    pdf.multi_cell(0, 10, text, align='C')

    img_width = pdf.w
    img_height =  int(image.height / image.width * img_width)
    pdf.image(image.path, x=0, y=pdf.h - img_height - 30, w = pdf.w)
    pdf.output(out_path)
