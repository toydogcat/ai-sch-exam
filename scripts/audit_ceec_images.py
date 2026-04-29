import os
import json
import re

def audit_images():
    base_dir = "/home/toymsi/documents/examination/Github/ai-sch-exam"
    images_dir = os.path.join(base_dir, "public/images/ceec")
    json_dir = os.path.join(base_dir, "public/json/ceec")

    # 1. Collect all images
    all_images = set()
    for root, dirs, files in os.walk(images_dir):
        for file in files:
            if file.endswith(('.webp', '.png', '.jpg', '.jpeg')):
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                # Normalize path for comparison (the JSON usually uses public-relative paths)
                # e.g. "images/ceec/..." instead of "public/images/ceec/..."
                if rel_path.startswith("public/"):
                    rel_path = rel_path[len("public/"):]
                all_images.add(rel_path)

    print(f"Total images found: {len(all_images)}")

    # 2. Scan all JSON files for image references
    referenced_images = set()
    broken_links = []
    absolute_paths = []
    missing_image_hints = [] # Questions mentioning "圖" but no img tag

    for root, dirs, files in os.walk(json_dir):
        for file in files:
            if file.endswith('.json') and file != 'catalog.json':
                json_path = os.path.join(root, file)
                with open(json_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        questions = data.get('questions', [])
                        for q in questions:
                            text = q.get('text', '')
                            # Search for image tags or markdown images
                            # Matches src="images/..." or src="/images/..." or ![](/images/...)
                            found = re.findall(r'src=["\']?/?(images/ceec/[^"\'>\s]+)["\']?', text)
                            found_md = re.findall(r'!\[.*?\]\((/?[^)]*images/ceec/[^)]+)\)', text)
                            
                            for img in found + found_md:
                                # Clean leading slash
                                clean_img = img.lstrip('/')
                                # Check for absolute paths
                                if "/home/toymsi/" in img:
                                    absolute_paths.append((json_path, q.get('number'), img))
                                    # Try to extract the relative part for usage check
                                    match = re.search(r'images/ceec/.*', img)
                                    if match:
                                        clean_img = match.group(0)

                                referenced_images.add(clean_img)
                                if clean_img not in all_images:
                                    broken_links.append((json_path, q.get('number'), clean_img))
                            
                            # Check for missing image hints
                            if re.search(r'圖\s?\d+', text) and not (found or found_md):
                                missing_image_hints.append((json_path, q.get('number'), text[:50] + "..."))

                    except Exception as e:
                        print(f"Error parsing {json_path}: {e}")

    # 3. Report
    orphans = all_images - referenced_images

    print("\n--- Summary ---")
    print(f"Referenced images: {len(referenced_images)}")
    print(f"Orphaned images: {len(orphans)}")
    print(f"Broken links: {len(broken_links)}")
    print(f"Absolute paths: {len(absolute_paths)}")
    print(f"Potential missing images (hints): {len(missing_image_hints)}")

    if broken_links:
        print("\n--- Broken Links (Top 10) ---")
        for loc, num, img in broken_links[:10]:
            print(f"{os.path.basename(loc)} Q{num}: {img}")

    if absolute_paths:
        print("\n--- Absolute Paths ---")
        for loc, num, path in absolute_paths:
            print(f"{os.path.basename(loc)} Q{num}: {path}")

    if orphans:
        print("\n--- Orphaned Images (Top 10) ---")
        for img in sorted(list(orphans))[:10]:
            print(img)
            
    if missing_image_hints:
        print("\n--- Missing Image Hints (Top 10) ---")
        for loc, num, snippet in missing_image_hints[:10]:
            print(f"{os.path.basename(loc)} Q{num}: {snippet}")

if __name__ == "__main__":
    audit_images()
