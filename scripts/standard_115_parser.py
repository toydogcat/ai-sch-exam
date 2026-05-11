import json
import re
import os
from pathlib import Path

SUBJECT_META = {
    "國寫": {"title": "115 學年度學科能力測驗 - 國語文寫作能力測驗 (參考試卷)", "duration": 90},
    "國綜": {"title": "115 學年度學科能力測驗 - 國語文綜合能力測驗 (參考試卷)", "duration": 90},
    "數A": {"title": "115 學年度學科能力測驗 - 數學 A 考科 (參考試卷)", "duration": 100},
    "數B": {"title": "115 學年度學科能力測驗 - 數學 B 考科 (參考試卷)", "duration": 100},
    "社會": {"title": "115 學年度學科能力測驗 - 社會考科 (參考試卷)", "duration": 110},
    "自然": {"title": "115 學年度學科能力測驗 - 自然考科 (參考試卷)", "duration": 110},
    "英文": {"title": "115 學年度學科能力測驗 - 英文考科 (參考試卷)", "duration": 100}
}

def process_images(text, subject):
    def repl(m):
        path = m.group(1)
        # Get the raw filename
        filename = os.path.basename(path)
        # Return canonical path format: /images/ceec/115/學測/{subject}/{filename}
        return f'<br><img src="/images/ceec/115/學測/{subject}/{filename}" style="max-width:100%; display:block; margin:10px 0;">'

    text = re.sub(r'!\[.*?\]\((.*?)\)', repl, text)
    return text

def markdown_table_to_html(text):
    if "|" not in text:
        return text

    lines = text.splitlines()
    new_lines = []
    
    in_table = False
    table_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") > 1:
            in_table = True
            table_lines.append(stripped)
        else:
            if in_table:
                html_table = render_html_table(table_lines)
                new_lines.append(html_table)
                table_lines = []
                in_table = False
            new_lines.append(line)
            
    if in_table:
        html_table = render_html_table(table_lines)
        new_lines.append(html_table)
        
    return "\n".join(new_lines)

def render_html_table(table_lines):
    if len(table_lines) < 2:
        return "\n".join(table_lines)
        
    sep = table_lines[1].strip()
    if not (sep.startswith("|") and sep.endswith("|") and all(c in " |:-" for c in sep)):
        return "\n".join(table_lines)
        
    headers = [h.strip() for h in table_lines[0].split("|")[1:-1]]
    rows = []
    for line in table_lines[2:]:
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < len(headers):
            cols += [""] * (len(headers) - len(cols))
        rows.append(cols[:len(headers)])
        
    html = '<div class="custom-table-container" style="overflow-x:auto; margin: 1.5rem 0; white-space: normal;">'
    html += '<table class="custom-exam-table" style="width:100%; border-collapse: collapse; border: 1px solid #dee2e6; font-size: 1rem; background: #fff; border-radius: 6px; white-space: normal;">'
    
    html += '<thead style="background: #f8f9fa; white-space: normal;"><tr>'
    for h in headers:
        html += f'<th style="border: 1px solid #dee2e6; padding: 12px 16px; text-align: left; font-weight: 700; color: #2c3e50; white-space: normal;">{h}</th>'
    html += '</tr></thead>'
    
    html += '<tbody style="white-space: normal;">'
    for r in rows:
        html += '<tr style="white-space: normal;">'
        for c in r:
            html += f'<td style="border: 1px solid #dee2e6; padding: 12px 16px; color: #34495e; line-height: 1.6; white-space: normal;">{c}</td>'
        html += '</tr>'
    html += '</tbody></table></div>'
    
    return html
def strip_leading_qnum(text, qnum):
    t = text.strip()
    for _ in range(2):
        t = re.sub(rf'^\s*{qnum}\s*[.、：:]\s*', '', t).strip()
    return t

def extract_options_and_clean(text):
    a_matches = list(re.finditer(r'(?:^|\n)\s*(\([A-Ga-g]\))', text))
    n_matches = list(re.finditer(r'(?:^|\n)\s*(\([1-9]\))', text))
    
    chosen_matches = []
    if len(a_matches) >= 2:
        chosen_matches = a_matches
    elif len(n_matches) >= 2:
        chosen_matches = n_matches
    else:
        fallback_a = list(re.finditer(r'\(([A-G])\)', text))
        if len(fallback_a) >= 2:
             chosen_matches = fallback_a
        else:
             fallback_n = list(re.finditer(r'\(([1-9])\)', text))
             if len(fallback_n) >= 2:
                 chosen_matches = fallback_n

    if len(chosen_matches) < 2:
        return text, []

    first_pos = chosen_matches[0].start()
    prompt = text[:first_pos].rstrip()
    
    extracted_options = []
    for i in range(len(chosen_matches)):
        start = chosen_matches[i].start()
        end = chosen_matches[i+1].start() if i+1 < len(chosen_matches) else len(text)
        seg = text[start:end].strip()
        cleaned_seg = re.sub(r'^\s*\([^)]+\)\s*', '', seg).strip()
        extracted_options.append(cleaned_seg)
        
    return prompt, extracted_options

def truncate_tail_at_next_passage(text):
    patterns = [
        r'(?:\r?\n){1,}\s*-{3,}',
        r'(?:\r?\n){1,}\s*##\s+',
        r'(?:\r?\n){1,}\s*##\s*.*?題組',
        r'(?:\r?\n){1,}\s*\*\*題組：.*?\*\*',
        r'(?:\r?\n){1,}\s*\*\*題組.*?\*\*'
    ]
    earliest_pos = len(text)
    found = False
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match and match.start() < earliest_pos:
            earliest_pos = match.start()
            found = True
    if found:
        return text[:earliest_pos].strip()
    return text

def parse_markdown_to_json(md_path, year, subject, title, duration):
    if not os.path.exists(md_path):
        print(f"File not found: {md_path}")
        return None

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tag_pattern = r'\[q:(\d+),\s*type:\s*([^,\]]+)(?:,\s*ans:\s*([^\]]+))?\]'
    matches = list(re.finditer(tag_pattern, content))
    
    questions = []
    current_passage = ""

    for i in range(len(matches)):
        m = matches[i]
        q_num = int(m.group(1))
        q_type = m.group(2).strip()
        q_ans = (m.group(3) or "").strip()
        
        start_pos = m.end()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        
        q_block = content[start_pos:end_pos].strip()
        
        prev_end = matches[i-1].end() if i > 0 else 0
        pre_gap = content[prev_end:m.start()].strip()
        
        passage_match = re.search(r'(?:##\s*.*題組.*|\*\*題組：.*?\*\*|\*\*題組.*?\*\*)(?:.*?)(?=\[q:|$)', pre_gap, re.DOTALL | re.IGNORECASE)
        if passage_match:
            current_passage = passage_match.group(0).strip()
        elif "---" in pre_gap:
            current_passage = ""

        clean_q_text = truncate_tail_at_next_passage(q_block)
        # clean_q_text = re.sub(r'-\s*\d+\s*-', '', q_block)  # Commented out: corrupts filenames like '數A.pdf-0002-10.webp'
        clean_q_text = re.sub(r'\d+\s*年學測.*', '', clean_q_text)
        clean_q_text = re.sub(r'第\s*\d+\s*頁\s*共\s*\d+\s*頁', '', clean_q_text)
        clean_q_text = re.sub(r'請記得在答題卷.*', '', clean_q_text)
        clean_q_text = clean_q_text.strip()
        
        # 1. Remove leading question number redundancy
        clean_q_text = strip_leading_qnum(clean_q_text, q_num)
        
        options = []
        # 2. Extract correct option texts and remove them from question body
        if q_type in ["single", "multi"]:
            prompt, extracted_opts = extract_options_and_clean(clean_q_text)
            clean_q_text = prompt
            if extracted_opts:
                options = extracted_opts
            else:
                # Absolute fallback to dummy array if parser found nothing
                options = ["(A)", "(B)", "(C)", "(D)", "(E)"]

        parsed_ans = q_ans
        if q_type == "multi" or "," in q_ans:
            if "," in q_ans:
                parsed_ans = [x.strip() for x in q_ans.split(",")]
            elif q_ans.isalpha() and q_ans.isupper():
                parsed_ans = list(q_ans)
            else:
                parsed_ans = [q_ans]

        clean_q_text = process_images(clean_q_text, subject)
        clean_passage = process_images(current_passage, subject) if current_passage else ""

        clean_q_text = markdown_table_to_html(clean_q_text)
        if clean_passage:
            clean_passage = markdown_table_to_html(clean_passage)

        questions.append({
            "number": q_num,
            "text": clean_q_text,
            "passage": clean_passage,
            "options": options,
            "answer": parsed_ans,
            "type": q_type,
            "score": 2
        })

    return {
        "title": title,
        "duration": duration,
        "questions": questions
    }

def run_conversion():
    base_md = Path("/home/toymsi/documents/examination/大學入學考試/md/115/學測")
    output_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/json/ceec/115/學測")
    output_dir.mkdir(parents=True, exist_ok=True)

    for sub, meta in SUBJECT_META.items():
        md_file = base_md / f"{sub}.md"
        if not md_file.exists(): continue
        
        print(f"Parsing {sub}...")
        data = parse_markdown_to_json(md_file, "115", sub, meta["title"], meta["duration"])
        
        if data:
            with open(output_dir / f"{sub}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Saved to {output_dir / f'{sub}.json'}")

if __name__ == "__main__":
    run_conversion()
