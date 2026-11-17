from fpdf import FPDF, XPos, YPos

def create_certificate(name, title, subtitle, text, image, out_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 24)
    pdf.cell(0, 20, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 0, title, align='C')
    pdf.cell(0,15, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font('Helvetica', '', 18)
    pdf.cell(0,0, subtitle, align='C')
    pdf.cell(0, 15, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font('Helvetica', 'U', 18)
    pdf.cell(0, 0, name, align='C')
    pdf.cell(0,15, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font('Helvetica', '', 18)
    pdf.multi_cell(0, 10, text, align='C')

    img_width = pdf.w
    img_height =  int(image.height / image.width * img_width)
    pdf.image(image.path, x=0, y=pdf.h - img_height - 30, w = pdf.w)
    pdf.output(out_path)
