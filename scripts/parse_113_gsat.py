import json
import re
import os
import shutil
from pathlib import Path

SUBJECT_META = {
    "自然": {"md": "自然.md", "title": "113 學年度學科能力測驗 - 自然考科", "duration": 110},
    "社會": {"md": "社會.md", "title": "113 學年度學科能力測驗 - 社會考科", "duration": 110},
    "數B": {"md": "數B.md", "title": "113 學年度學科能力測驗 - 數學B考科", "duration": 100},
    "數A": {"md": "數A.md", "title": "113 學年度學科能力測驗 - 數學A考科", "duration": 100},
    "英文": {"md": "英文.md", "title": "113 學年度學科能力測驗 - 英文考科", "duration": 100},
}

def process_images(text, subject_key):
    def repl(m):
        path_str = m.group(1)
        if path_str.startswith("/home/toymsi/documents/examination"):
            src_path = Path(path_str)
        else:
            src_path = Path(path_str)

        repo_pub = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public")
        dest_rel = Path(f"images/ceec/113/學測/{subject_key}/{src_path.name}")
        dest_abs = repo_pub / dest_rel

        if src_path.exists():
            if src_path.resolve() != dest_abs.resolve():
                dest_abs.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dest_abs)
            return f'<br><img src="/{dest_rel.as_posix()}" style="max-width:100%; display:block; margin:10px 0;">'
        else:
            return f'<br><img src="/images/ceec/113/學測/{subject_key}/{src_path.name}" style="max-width:100%; display:block; margin:10px 0;">'

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

def parse_markdown_to_json(md_path, year, subject_key, title, duration):
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

        clean_q_text = re.sub(r'(?m)^\s*-\s*\d+\s*-\s*$', '', q_block)
        clean_q_text = re.sub(r'\d+\s*年學測.*', '', clean_q_text)
        clean_q_text = re.sub(r'第\s*\d+\s*頁\s*共\s*\d+\s*頁', '', clean_q_text)
        clean_q_text = re.sub(r'請記得在答題卷.*', '', clean_q_text)
        clean_q_text = clean_q_text.strip()
        
        options = []
        if q_type in ["single", "multi"]:
            if "(A)" in clean_q_text:
                opt_matches = re.findall(r'\(([A-G])\)\s*(.*?)(?=\s*\([A-G]\)|$)', clean_q_text, re.DOTALL)
            elif "(1)" in clean_q_text:
                opt_matches = re.findall(r'\(([1-7])\)\s*(.*?)(?=\s*\([1-7]\)|$)', clean_q_text, re.DOTALL)
            else:
                opt_matches = []

            if opt_matches:
                for opt_label, opt_val in opt_matches:
                    options.append(opt_val.strip())
                first_label = opt_matches[0][0]
                clean_q_text = clean_q_text.split(f"({first_label})")[0].strip()
            else:
                options = ["(A)", "(B)", "(C)", "(D)", "(E)"]

        clean_q_text = clean_q_text.replace("<", "&lt;").replace(">", "&gt;")
        if current_passage:
            current_passage = current_passage.replace("<", "&lt;").replace(">", "&gt;")
        options = [opt.replace("<", "&lt;").replace(">", "&gt;") for opt in options]

        parsed_ans = q_ans
        if q_type == "multi" or "," in q_ans:
            if "," in q_ans:
                parsed_ans = [x.strip() for x in q_ans.split(",")]
            elif q_ans.isalpha() and q_ans.isupper():
                parsed_ans = list(q_ans)
            else:
                parsed_ans = [q_ans]
        elif q_type in ["single", "multi"] and not parsed_ans:
            parsed_ans = []

        clean_q_text = process_images(clean_q_text, subject_key)
        clean_passage = process_images(current_passage, subject_key) if current_passage else ""

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
    base_md = Path("/home/toymsi/documents/examination/大學入學考試/md/113/學測")
    output_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public/json/ceec/113/學測")
    output_dir.mkdir(parents=True, exist_ok=True)

    for sub_key, meta in SUBJECT_META.items():
        md_file = base_md / meta["md"]
        if not md_file.exists():
            print(f"Markdown file does not exist: {md_file}")
            continue
        
        print(f"Parsing {sub_key}...")
        data = parse_markdown_to_json(md_file, "113", sub_key, meta["title"], meta["duration"])
        
        if data:
            with open(output_dir / f"{sub_key}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Saved to {output_dir / f'{sub_key}.json'}")

if __name__ == "__main__":
    run_conversion()
