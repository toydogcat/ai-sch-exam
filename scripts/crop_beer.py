import fitz

pdf_path = "/home/toymsi/documents/examination/大學入學考試/raw/114/學科能力測驗/自然/114學測自然試題定稿.pdf"
doc = fitz.open(pdf_path)
page = doc[8]  # Page 9 is index 8

# Get page dimensions
rect = page.rect
width = rect.width
height = rect.height

# Let's crop from y=120 to y=320, x=100 to x=500
# We can export it as a high-res image using a zoom matrix
zoom = 300 / 72  # 300 dpi
mat = fitz.Matrix(zoom, zoom)

# Define the crop box in 72 dpi points
crop_rect = fitz.Rect(50, 120, width - 50, 320)
pix = page.get_pixmap(matrix=mat, clip=crop_rect)
from PIL import Image
import io

pix = page.get_pixmap(matrix=mat, clip=crop_rect)
img_bytes = pix.tobytes("png")
image = Image.open(io.BytesIO(img_bytes))
image.save("/home/toymsi/documents/examination/Github/ai-sch-exam/public/images/ceec/114/自然/beer_compounds.webp", "WEBP")
print("Saved beer compounds image as WEBP.")

