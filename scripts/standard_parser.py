import json
import re
import os
from pathlib import Path

def parse_markdown_to_json(md_path, year, subject, title, duration):
    if not os.path.exists(md_path):
        print(f"File not found: {md_path}")
        return None

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by the metadata tag: [q:N, type:T, ans:A]
    # We use a regex that matches the tag and captures its contents
    tag_pattern = r'\[q:(\d+),\s*type:(\w+)(?:,\s*ans:([^,\]]*))?(?:,\s*audio:([^,\]]*))?.*?\]'
    
    # First, let's identify all tag positions
    matches = list(re.finditer(tag_pattern, content))
    
    questions = []
    current_passage = ""

    for i in range(len(matches)):
        m = matches[i]
        q_num = int(m.group(1))
        q_type = m.group(2)
        q_ans = m.group(3) or ""
        q_audio = m.group(4) or ""
        
        start_pos = m.end()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        
        # Text between this tag and the next one
        q_block = content[start_pos:end_pos].strip()
        
        # Check if there was a passage header BEFORE this tag
        # Look at the text between the PREVIOUS match end and THIS match start
        prev_end = matches[i-1].end() if i > 0 else 0
        pre_gap = content[prev_end:m.start()].strip()
        
        # If pre_gap contains a passage header like "**題組：...**", capture it
        passage_match = re.search(r'(\*\*題組：.*?\*\*(?:.*?))(?=\[q:|$)', pre_gap, re.DOTALL)
        if passage_match:
            current_passage = passage_match.group(1).strip()
        elif "---" in pre_gap: # Reset passage on horizontal rules
            current_passage = ""

        # Process Images
        images = re.findall(r'!\[\]\((.*?)\)', q_block)
        image_html = ""
        for img in images:
            # Convert absolute path to relative for VitePress
            img_rel = img.replace("/home/toymsi/documents/examination/Github/ai-sch-exam/public/", "")
            image_html += f'<br><img src="/{img_rel}" style="max-width:100%; display:block; margin:10px 0;">'
        
        # Process Passage Images
        passage_image_html = ""
        if current_passage:
            p_images = re.findall(r'!\[\]\((.*?)\)', current_passage)
            for p_img in p_images:
                p_img_rel = p_img.replace("/home/toymsi/documents/examination/Github/ai-sch-exam/public/", "")
                passage_image_html += f'<br><img src="/{p_img_rel}" style="max-width:100%; display:block; margin:10px 0;">'
            current_passage = re.sub(r'!\[\]\(.*?\)', '', current_passage).strip()

        # Clean question text
        clean_q_text = re.sub(r'!\[\]\(.*?\)', '', q_block).strip()
        
        # Extract Options
        # Matches (A), (B), (C), (D) etc.
        options = []
        # First, split the block by horizontal rules or section headers to isolate question content
        main_q_block = re.split(r'\n---\n|\n##', clean_q_text)[0].strip()
        
        opt_matches = re.findall(r'\(([A-G])\)\s*(.*?)(?=\s*\([A-G]\)|$)', main_q_block, re.DOTALL)
        if opt_matches:
            for opt_label, opt_val in opt_matches:
                options.append(opt_val.strip())
            # Remove options from the main text
            clean_q_text = re.split(r'\([A-G]\)', clean_q_text)[0].strip()

        # Final score logic
        score = 2
        if subject == "自然": score = 2
        elif subject == "社會": score = 2
        elif subject == "國文": score = 2
        elif subject == "數學": score = 4 if q_num <= 25 else 5
        
        questions.append({
            "number": q_num,
            "text": clean_q_text + image_html,
            "passage": current_passage + passage_image_html if current_passage else "",
            "options": options,
            "answer": q_ans,
            "type": q_type,
            "audio": q_audio,
            "score": score
        })

    return {
        "title": title,
        "year": year,
        "subject": subject,
        "duration": duration,
        "questions": questions
    }

def run_conversion():
    base_md = Path("/home/toymsi/documents/examination/國中教育會考/md/114")
    output_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/json/cap/114")
    output_dir.mkdir(parents=True, exist_ok=True)

    subjects = {
        "國文": 70,
        "數學": 80,
        "社會": 70,
        "自然": 70,
        "英語閱讀": 60,
        "英語聽力": 25
    }

    for sub, dur in subjects.items():
        md_file = base_md / f"{sub}.md"
        if not md_file.exists(): continue
        
        print(f"Parsing {sub}...")
        data = parse_markdown_to_json(md_file, "114", sub, f"114 年國中教育會考 - {sub}", dur)
        
        if data:
            with open(output_dir / f"{sub}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Saved to {output_dir / f'{sub}.json'}")

if __name__ == "__main__":
    run_conversion()
