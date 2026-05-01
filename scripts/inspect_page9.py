import fitz  # PyMuPDF
import sys

pdf_path = "/home/toymsi/documents/examination/大學入學考試/raw/114/學科能力測驗/自然/114學測自然試題定稿.pdf"
doc = fitz.open(pdf_path)

# Page 9 in the exam paper corresponds to index 8
page = doc[8]
pix = page.get_pixmap()
pix.save("page_9_inspect.png")
print("Saved page 9 inspect image.")
