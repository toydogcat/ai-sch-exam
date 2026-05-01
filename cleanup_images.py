import os
import json
import re

def cleanup():
    base_dir = "/home/toymsi/documents/examination/Github/ai-sch-exam"
    
    # directories to check
    mapping = {
        "ceec": os.path.join(base_dir, "public/images/ceec"),
        "cap": os.path.join(base_dir, "public/images/cap")
    }
    
    used_images = {
        "ceec": set(),
        "cap": set()
    }
    
    # regex to find all images
    pattern = r'images/(ceec|cap)/([^"\']+\.(?:webp|png|jpg|jpeg))'
    
    # Scan all JSON files in public/json
    json_base = os.path.join(base_dir, "public/json")
    for root, dirs, files in os.walk(json_base):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                    def find_images(obj):
                        if isinstance(obj, dict):
                            for k, v in obj.items():
                                if isinstance(v, str):
                                    matches = re.findall(pattern, v)
                                    for m in matches:
                                        cat, img_rel = m
                                        used_images[cat].add(img_rel)
                                else:
                                    find_images(v)
                        elif isinstance(obj, list):
                            for item in obj:
                                find_images(item)
                                
                    find_images(data)
                except Exception as e:
                    print(f"Error parsing {file}: {e}")
                    
    print(f"Total unique images referenced in CEEC: {len(used_images['ceec'])}")
    print(f"Total unique images referenced in CAP: {len(used_images['cap'])}")
    
    # Actually clean up unreferenced images
    for cat, image_dir in mapping.items():
        if not os.path.exists(image_dir):
            print(f"Image directory {image_dir} does not exist. Skipping.")
            continue
            
        files_to_delete = []
        total_images = 0
        
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                    total_images += 1
                    rel_path = os.path.relpath(os.path.join(root, file), image_dir)
                    if rel_path not in used_images[cat]:
                        files_to_delete.append(os.path.join(root, file))
                        
        print(f"[{cat}] Total images: {total_images}")
        print(f"[{cat}] Found {len(files_to_delete)} unused images.")
        
        for f in files_to_delete:
            os.remove(f)
            
    print("Cleanup complete.")

if __name__ == "__main__":
    cleanup()
