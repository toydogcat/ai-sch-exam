import os
import json
import re

def audit_images():
    base_dir = "/home/toymsi/documents/examination/Github/ai-sch-exam"
    public_dir = os.path.join(base_dir, "public")
    images_ceec_dir = os.path.join(public_dir, "images/ceec")
    json_ceec_dir = os.path.join(public_dir, "json/ceec")

    # 1. Collect all images
    all_images = set()
    for root, dirs, files in os.walk(images_ceec_dir):
        for file in files:
            if file.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, public_dir)
                all_images.add(rel_path)

    # 2. Collect all JSON files
    json_files = []
    for root, dirs, files in os.walk(json_ceec_dir):
        for file in files:
            if file.endswith('.json') and file != 'catalog.json':
                json_files.append(os.path.join(root, file))

    used_images = set()
    missing_images = []
    questions_without_images = []

    # Patterns for finding image references in JSON
    img_tag_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
    # Patterns for finding mentions of figures/tables in text
    # "圖 1", "表 2", "圖一", "如下圖", "示意圖", "圖示"
    figure_mention_pattern = re.compile(r'(圖\s*[0-9A-Z一二三四五六七八九十]+|表\s*[0-9一二三四五六七八九十]+|示意圖|圖示|如下圖|如圖)')

    for json_path in json_files:
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error loading {json_path}: {e}")
                continue

            rel_json_path = os.path.relpath(json_path, base_dir)
            
            if 'questions' in data:
                for q in data['questions']:
                    q_text = q.get('text', '')
                    q_num = q.get('number', 'unknown')
                    
                    # Find image tags in question text or options
                    tags = img_tag_pattern.findall(q_text)
                    for opt in q.get('options', []):
                        tags.extend(img_tag_pattern.findall(opt))
                    
                    has_img = len(tags) > 0
                    for src in tags:
                        # Normalize path
                        # src might be "images/ceec/..." or "/images/ceec/..."
                        clean_src = src.lstrip('/')
                        used_images.add(clean_src)
                        if clean_src not in all_images:
                            missing_images.append({
                                'json': rel_json_path,
                                'q_num': q_num,
                                'src': src
                            })

                    # Check for mentions without images
                    if not has_img:
                        mentions = figure_mention_pattern.findall(q_text)
                        if mentions:
                            questions_without_images.append({
                                'json': rel_json_path,
                                'q_num': q_num,
                                'mentions': list(set(mentions)),
                                'text_preview': q_text[:100] + "..."
                            })

    unused_images = all_images - used_images

    # Output results
    print(f"Total images found: {len(all_images)}")
    print(f"Total unique images used in JSON: {len(used_images)}")
    print(f"Total unused images: {len(unused_images)}")
    print(f"Total missing images (referenced but not found): {len(missing_images)}")
    print(f"Questions mentioning figures but lacking <img> tags: {len(questions_without_images)}")

    print("\n--- Unused Images (Top 20) ---")
    for img in sorted(list(unused_images))[:20]:
        print(img)
    if len(unused_images) > 20:
        print("...")

    print("\n--- Missing Images ---")
    for item in missing_images:
        print(f"JSON: {item['json']}, Q: {item['q_num']}, Src: {item['src']}")

    print("\n--- Questions potentially missing images ---")
    for item in questions_without_images[:20]:
        print(f"JSON: {item['json']}, Q: {item['q_num']}, Mentions: {item['mentions']}")
    if len(questions_without_images) > 20:
        print("...")

if __name__ == "__main__":
    audit_images()
