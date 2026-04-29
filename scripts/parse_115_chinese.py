import json
import re
import os

ANSWERS = {
    1: "C", 2: "A", 3: "D", 4: "B", 5: "C",
    6: "D", 7: "C", 8: "D", 9: "A", 10: "C",
    11: "D", 12: "B", 13: "B", 14: "B", 15: "A",
    16: "D", 17: "B", 18: "D", 19: "D", 20: "A",
    21: "A", 22: "C", 23: "B", 24: "C",
    25: "BE", 26: "ABD", 27: "ABD", 28: "ACDE", 29: "CD", 30: "CD", 31: "ABE"
}

GROUP_ENDS = {8, 10, 13, 15, 18, 21, 24, 31, 36}

def clean_text(text):
    text = re.sub(r'-\s*\d+\s*-', '', text)
    text = re.sub(r'\d+年學測\s*國語文綜合能力測驗', '', text)
    text = re.sub(r'第\s*\d+\s*頁\s*共\s*\d+\s*頁', '', text)
    text = re.sub(r'請記得在答題卷簽名欄位以正楷簽全名', '', text)
    text = re.sub(r'\f', '', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def parse_md_to_json(md_content, title, duration=90):
    lines = md_content.split('\n')
    stripped_lines = []
    for line in lines:
        m = re.match(r'^\d+:\s?(.*)', line)
        stripped_lines.append(m.group(1) if m else line)
    
    clean_md = '\n'.join(stripped_lines)
    clean_md = clean_md.split('---', 2)[-1].strip()
    
    questions = []
    current_passage = ""
    
    # Split by Question number OR Group header
    blocks = re.split(r'\n(?=\d+\.\s|\d+-\d+為題組)', '\n' + clean_md)
    
    for block in blocks:
        block = block.strip()
        if not block: continue
        
        # If block starts with a group header
        if re.match(r'^\d+-\d+為題組', block):
            # Split this block into passage and questions
            sub_blocks = re.split(r'\n(?=\d+\.\s)', block)
            passage_text = sub_blocks[0]
            current_passage = clean_text(passage_text)
            # Process remaining sub_blocks as questions
            for q_block in sub_blocks[1:]:
                q_num, current_passage = process_q_block(q_block, questions, current_passage)
        elif re.match(r'^\d+\.\s', block):
            q_num, current_passage = process_q_block(block, questions, current_passage)
            
    return {
        "title": title,
        "duration": duration,
        "questions": questions
    }

IMAGE_MAP = {
    19: "images/ceec/115/國綜/懷素自敘帖.webp"
}

def process_q_block(q_block, questions, current_passage):
    q_match = re.match(r'^(\d+)\.\s*(.*)', q_block, re.DOTALL)
    if q_match:
        q_num = int(q_match.group(1))
        remaining = q_match.group(2)
        
        # Identify where options start
        opt_start = re.search(r'\([A-E]\)', remaining)
        if opt_start:
            q_text = clean_text(remaining[:opt_start.start()])
            opts_part = remaining[opt_start.start():]
            
            parts = re.split(r'(\([A-E]\))', opts_part)
            options = []
            for j in range(1, len(parts), 2):
                label = parts[j]
                content = clean_text(parts[j+1])
                options.append(f"{label} {content}")
        else:
            q_text = clean_text(remaining)
            options = []
            
        if current_passage:
            # Inject image into passage if q_num is in IMAGE_MAP
            if q_num in IMAGE_MAP:
                img_tag = f'<br><img src="{IMAGE_MAP[q_num]}" style="max-width:100%; display:block; margin:10px 0;">'
                if "▲" in current_passage:
                    # Insert before the marker
                    current_passage = current_passage.replace("▲", img_tag + "\n▲")
                else:
                    current_passage += "\n" + img_tag
            full_text = current_passage + "\n\n" + q_text
        else:
            full_text = q_text
            if q_num in IMAGE_MAP:
                img_tag = f'<br><img src="{IMAGE_MAP[q_num]}" style="max-width:100%; display:block; margin:10px 0;">'
                full_text += "\n" + img_tag
            
        q_type = "single" if q_num <= 24 else "multi"
        questions.append({
            "number": q_num,
            "text": full_text,
            "options": options,
            "answer": ANSWERS.get(q_num, ""),
            "type": q_type,
            "score": 2 if q_type == "single" else 4
        })
        
        # Clear passage if this was the last question in the group
        if q_num in GROUP_ENDS:
            return q_num, ""
        return q_num, current_passage
    return None, current_passage

# Read MD
with open('/home/toymsi/.gemini/antigravity/brain/d6fef143-a45d-4a9f-bf1d-841eb16730f9/.system_generated/steps/66/output.txt', 'r') as f:
    content = f.read()

data = parse_md_to_json(content, "115 學年度學科能力測驗 - 國語文綜合能力測驗")

seen_nums = set()
unique_questions = []
for q in data['questions']:
    if q['number'] not in seen_nums:
        unique_questions.append(q)
        seen_nums.add(q['number'])
data['questions'] = unique_questions

# Save to target location
output_dir = "/home/toymsi/documents/examination/Github/ai-sch-exam/public/json/ceec/115"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "國綜.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(data['questions'])} unique questions with answers.")
