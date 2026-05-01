import os
import glob
from pathlib import Path
from PIL import Image
import subprocess

raw_dir = Path("/home/toymsi/documents/examination/國中教育會考/raw/113")
output_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/images/cap/113")

subjects = ["國文", "寫作測驗", "數學", "社會", "自然", "英語聽力", "英語閱讀"]

def extract_and_convert():
    for sub in subjects:
        sub_dir = raw_dir / sub
        pdf_files = list(sub_dir.glob("*_試題.pdf"))
        if not pdf_files:
            continue
        pdf_file = pdf_files[0]
        
        # Create output dir
        sub_out = output_dir / sub
        sub_out.mkdir(parents=True, exist_ok=True)
        
        # Temp prefix
        prefix = sub_out / "extracted"
        print(f"Extracting images from {pdf_file.name} to {sub_out}...")
        
        # Extract images as PNG using pdfimages
        subprocess.run(["pdfimages", "-png", str(pdf_file), str(prefix)], check=True)
        
        # Convert PNG to WebP and remove PNG
        png_files = list(sub_out.glob("*.png"))
        for png in png_files:
            webp_path = png.with_suffix(".webp")
            try:
                with Image.open(png) as img:
                    img.save(webp_path, "WEBP", quality=90)
                png.unlink()
            except Exception as e:
                print(f"Failed to convert {png.name}: {e}")

if __name__ == "__main__":
    extract_and_convert()
