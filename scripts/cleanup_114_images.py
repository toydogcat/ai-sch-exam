import os
import re
from pathlib import Path

def cleanup_unused_images():
    base_dir = Path("/home/toymsi/documents/examination/國中教育會考")
    md_dir = base_dir / "md" / "114"
    image_base = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/images/cap/114")
    
    # 1. Collect all images in the 114 directory
    all_images = []
    for root, dirs, files in os.walk(image_base):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                all_images.append(Path(root) / file)
    
    print(f"Total images found in {image_base}: {len(all_images)}")
    
    # 2. Collect all image references in MD files
    used_images = set()
    md_files = list(md_dir.glob("*.md"))
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match ![](/path/to/image.webp)
            matches = re.findall(r'!\[\]\((.*?)\)', content)
            for m in matches:
                # Normalize path
                used_images.add(str(Path(m).resolve()))
    
    print(f"Unique images referenced in {md_dir}: {len(used_images)}")
    
    # 3. Find unused
    removed_count = 0
    for img_path in all_images:
        abs_img_path = str(img_path.resolve())
        if abs_img_path not in used_images:
            print(f"Removing unused image: {img_path.relative_to(image_base)}")
            os.remove(img_path)
            removed_count += 1
            
    print(f"Done. Removed {removed_count} unused images.")

if __name__ == "__main__":
    cleanup_unused_images()
