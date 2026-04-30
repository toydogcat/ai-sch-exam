import os
import subprocess
from pathlib import Path

def convert_png_to_webp_globally():
    # Root paths
    image_root = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/images/cap")
    md_root = Path("/home/toymsi/documents/examination/國中教育會考/md")
    
    # 1. Convert ALL PNG to WEBP recursively in the images root
    png_files = list(image_root.rglob("*.png"))
    print(f"Found {len(png_files)} PNG files to convert in total.")
    
    for png_path in png_files:
        webp_path = png_path.with_suffix(".webp")
        print(f"Converting {png_path.relative_to(image_root)} -> {webp_path.name}")
        try:
            subprocess.run([
                "ffmpeg", "-i", str(png_path), 
                "-c:v", "libwebp", "-lossless", "1", 
                str(webp_path), "-y"
            ], check=True, capture_output=True)
            os.remove(png_path)
        except Exception as e:
            print(f"Error converting {png_path}: {e}")

    # 2. Update ALL MD files across all years
    md_files = list(md_root.rglob("*.md"))
    print(f"Checking {len(md_files)} markdown files for references...")
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(".png)", ".webp)")
        
        if content != new_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Updated references in {md_file.relative_to(md_root)}")

if __name__ == "__main__":
    convert_png_to_webp_globally()
