import os
import re
from pathlib import Path

def cleanup_unused_images():
    root_dir = Path("/home/toymsi/documents/examination")
    image_base_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/images")

    print(f"Scanning all markdown and json files in {root_dir}...")
    
    # 1. Read the entire content of all .md and .json files in /home/toymsi/documents/examination
    # We ignore cache, dist, node_modules, git
    ignored_dirs = {'.git', 'node_modules', 'cache', 'dist', '__pycache__'}
    extensions = {'.md', '.json'}
    
    all_content = []
    
    for path in root_dir.rglob('*'):
        if any(ignored in path.parts for ignored in ignored_dirs):
            continue
        if path.is_file() and path.suffix.lower() in extensions:
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    all_content.append(f.read())
            except Exception as e:
                pass
                
    giant_text = "\n".join(all_content)
    print(f"Read all file contents. Size of merged text: {len(giant_text)} characters.")

    # 2. Iterate through all files in the public/images folder
    image_extensions = {'.png', '.jpg', '.jpeg', '.webp', '.gif'}
    
    total_images = 0
    deleted_images = 0
    
    for path in image_base_dir.rglob('*'):
        if path.is_file() and path.suffix.lower() in image_extensions:
            total_images += 1
            basename = path.name
            
            # 3. Check if the basename exists anywhere in our merged text
            if basename not in giant_text:
                print(f"Unused image detected & deleted: {path}")
                try:
                    os.remove(path)
                    deleted_images += 1
                except Exception as e:
                    print(f"Error deleting {path}: {e}")
                    
    print(f"\nCleanup complete. Scanned {total_images} image file(s). Deleted {deleted_images} unused image(s).")

if __name__ == "__main__":
    cleanup_unused_images()
