import fitz

pdf_path = "/home/toymsi/documents/examination/大學入學考試/raw/114/學科能力測驗/自然/114學測自然試題定稿.pdf"
doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    text = page.get_text()
    if "化合物甲與乙是啤酒苦味" in text:
        print(f"Found on page index: {i}")
