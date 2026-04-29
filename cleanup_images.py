import os
import json
import re

def cleanup():
    base_dir = "/home/toymsi/documents/examination/Github/ai-sch-exam"
    json_dir = os.path.join(base_dir, "public/json/ceec")
    image_dir = os.path.join(base_dir, "public/images/ceec")
    
    used_images = set()
    
    # Scan all JSON files for image references
    for root, dirs, files in os.walk(json_dir):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        # Traverse the JSON to find all "text" fields
                        def find_images(obj):
                            if isinstance(obj, dict):
                                for k, v in obj.items():
                                    if k == "text" and isinstance(v, str):
                                        # Find all src="images/ceec/..."
                                        matches = re.findall(r'src=["\']images/ceec/(.*?)["\']', v)
                                        for m in matches:
                                            used_images.add(m)
                                    else:
                                        find_images(v)
                            elif isinstance(obj, list):
                                for item in obj:
                                    find_images(item)
                        
                        find_images(data)
                    except Exception as e:
                        print(f"Error parsing {file}: {e}")
    
    print(f"Total unique images referenced in JSON: {len(used_images)}")
    
    files_to_delete = []
    total_images = 0
    
    # Scan image directory
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            total_images += 1
            rel_path = os.path.relpath(os.path.join(root, file), image_dir)
            if rel_path not in used_images:
                files_to_delete.append(os.path.join(root, file))
                
    print(f"Total images in directory: {total_images}")
    print(f"Found {len(files_to_delete)} unused images.")
    
    # Actually delete
    for f in files_to_delete:
        os.remove(f)
        
    print("Cleanup complete.")

if __name__ == "__main__":
    cleanup()
