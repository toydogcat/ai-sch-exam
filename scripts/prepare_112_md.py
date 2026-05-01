import re
import os
from pathlib import Path

ANSWERS_112 = {
    "國文": {
        1: 'D', 2: 'D', 3: 'C', 4: 'C', 5: 'D', 6: 'C', 7: 'A', 8: 'A', 9: 'A', 10: 'D',
        11: 'C', 12: 'A', 13: 'B', 14: 'C', 15: 'B', 16: 'D', 17: 'A', 18: 'C', 19: 'A', 20: 'B',
        21: 'C', 22: 'D', 23: 'D', 24: 'B', 25: 'D', 26: 'A', 27: 'A', 28: 'B', 29: 'C', 30: 'A',
        31: 'C', 32: 'B', 33: 'C', 34: 'B', 35: 'B', 36: 'C', 37: 'B', 38: 'A', 39: 'D', 40: 'D',
        41: 'B', 42: 'D'
    },
    "英語閱讀": {
        1: 'B', 2: 'D', 3: 'D', 4: 'B', 5: 'A', 6: 'B', 7: 'A', 8: 'C', 9: 'C', 10: 'D',
        11: 'D', 12: 'C', 13: 'C', 14: 'C', 15: 'D', 16: 'C', 17: 'C', 18: 'B', 19: 'D', 20: 'C',
        21: 'A', 22: 'B', 23: 'D', 24: 'B', 25: 'B', 26: 'A', 27: 'A', 28: 'C', 29: 'D', 30: 'B',
        31: 'A', 32: 'A', 33: 'D', 34: 'C', 35: 'B', 36: 'D', 37: 'D', 38: 'B', 39: 'B', 40: 'C',
        41: 'B', 42: 'A', 43: 'A'
    },
    "英語聽力": {
        1: 'C', 2: 'A', 3: 'B', 4: 'C', 5: 'C', 6: 'B', 7: 'A', 8: 'B', 9: 'C', 10: 'B',
        11: 'C', 12: 'C', 13: 'B', 14: 'A', 15: 'A', 16: 'A', 17: 'B', 18: 'A', 19: 'C', 20: 'C',
        21: 'A'
    },
    "數學": {
        1: 'A', 2: 'C', 3: 'B', 4: 'C', 5: 'B', 6: 'A', 7: 'A', 8: 'C', 9: 'B', 10: 'D',
        11: 'D', 12: 'A', 13: 'C', 14: 'B', 15: 'D', 16: 'C', 17: 'C', 18: 'B', 19: 'B', 20: 'C',
        21: 'B', 22: 'C', 23: 'B', 24: 'D', 25: 'A'
    },
    "社會": {
        1: 'C', 2: 'D', 3: 'A', 4: 'A', 5: 'A', 6: 'C', 7: 'C', 8: 'D', 9: 'C', 10: 'C',
        11: 'B', 12: 'D', 13: 'A', 14: 'B', 15: 'A', 16: 'C', 17: 'A', 18: 'A', 19: 'D', 20: 'A',
        21: 'B', 22: 'D', 23: 'B', 24: 'B', 25: 'A', 26: 'B', 27: 'A', 28: 'B', 29: 'A', 30: 'D',
        31: 'C', 32: 'D', 33: 'B', 34: 'D', 35: 'D', 36: 'C', 37: 'B', 38: 'D', 39: 'A', 40: 'A',
        41: 'C', 42: 'D', 43: 'C', 44: 'C', 45: 'D', 46: 'B', 47: 'C', 48: 'D', 49: 'B', 50: 'A',
        51: 'A', 52: 'D', 53: 'B', 54: 'C'
    },
    "自然": {
        1: 'D', 2: 'B', 3: 'D', 4: 'C', 5: 'A', 6: 'A', 7: 'B', 8: 'C', 9: 'C', 10: 'B',
        11: 'D', 12: 'A', 13: 'A', 14: 'B', 15: 'B', 16: 'A', 17: 'B', 18: 'A', 19: 'C', 20: 'B',
        21: 'D', 22: 'B', 23: 'C', 24: 'D', 25: 'D', 26: 'A', 27: 'A', 28: 'A', 29: 'B', 30: 'C',
        31: 'C', 32: 'C', 33: 'C', 34: 'D', 35: 'C', 36: 'A', 37: 'B', 38: 'D', 39: 'D', 40: 'A',
        41: 'A', 42: 'D', 43: 'A', 44: 'D', 45: 'C', 46: 'B', 47: 'B', 48: 'B', 49: 'A', 50: 'C'
    }
}

def get_audio_path(q_num):
    base_dir = "/home/toymsi/documents/examination/國中教育會考/raw/112/英語聽力"
    if not os.path.isdir(base_dir):
        return ""
    for f in os.listdir(base_dir):
        if f.endswith(".mp3") and f"第{q_num}題" in f:
            return f
    return ""

def prepare_subject(subject):
    print(f"Processing {subject}...")
    w_md_path = Path(f"/home/toymsi/documents/examination/國中教育會考/md/112/{subject}-w.md")
    
    if subject == "寫作測驗":
        if not w_md_path.exists():
            print(f"  No working file {w_md_path} found.")
            return
        with open(w_md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        out_lines = ["[q:1, type:essay]\n"]
        out_lines.extend(lines)
        out_md_path = Path(f"/home/toymsi/documents/examination/國中教育會考/md/112/{subject}.md")
        with open(out_md_path, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)
        print(f"  Wrote clean markdown to {out_md_path}")
        return

    if subject == "英語閱讀":
        gen_path = Path("/home/toymsi/documents/examination/國中教育會考/raw/112/英語閱讀/gen.md")
        if gen_path.exists():
            with open(gen_path, 'r', encoding='utf-8') as f:
                gen_lines = f.readlines()[:166]
        else:
            gen_lines = []

        with open(w_md_path, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace("<br>", "\n").replace("<BR>", "\n")
        w_lines = text.split("\n")[111:] # line 112 onwards

        out_lines = []
        out_lines.extend(gen_lines)

        generated_tags = set()
        for line in w_lines:
            m = re.match(r'^\s*(?:##\s*|-\s*|>\s*|\|\s*)?(\d+)\.\s*', line)
            if m:
                q_num = int(m.group(1))
                if q_num >= 24 and q_num <= 43 and q_num not in generated_tags:
                    generated_tags.add(q_num)
                    ans = ANSWERS_112["英語閱讀"].get(q_num, "")
                    out_lines.append(f"[q:{q_num}, type:single, ans:{ans}]\n")
            out_lines.append(line + "\n")

        out_md_path = Path(f"/home/toymsi/documents/examination/國中教育會考/md/112/{subject}.md")
        with open(out_md_path, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)
        print(f"  Wrote clean markdown to {out_md_path}")
        return

    if subject == "英語聽力":
        if not w_md_path.exists():
            print(f"  No working file {w_md_path} found.")
            return
        with open(w_md_path, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace("<br>", "\n").replace("<BR>", "\n")
        lines = text.split("\n")
        
        out_lines = []
        for line in lines:
            m = re.search(r'(?:##\s*|^\s*)第\s*(\d+)\s*題', line)
            if m:
                q_num = int(m.group(1))
                ans = ANSWERS_112["英語聽力"].get(q_num, "")
                audio_path = get_audio_path(q_num)
                tag_str = f"[q:{q_num}, type:single"
                if ans:
                    tag_str += f", ans:{ans}"
                if audio_path:
                    tag_str += f", audio:/home/toymsi/documents/examination/國中教育會考/raw/112/英語聽力/{audio_path}"
                tag_str += "]\n"
                out_lines.append(tag_str)
            out_lines.append(line + "\n")
        
        out_md_path = Path(f"/home/toymsi/documents/examination/國中教育會考/md/112/{subject}.md")
        with open(out_md_path, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)
        print(f"  Wrote clean markdown to {out_md_path}")
        return

    if subject == "數學":
        if not w_md_path.exists():
            print(f"  No working file {w_md_path} found.")
            return
        with open(w_md_path, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace("<br>", "\n").replace("<BR>", "\n")
        lines = text.split("\n")
        
        out_lines = []
        found_divider = False
        in_second_part = False
        generated_tags = set()
        
        for idx, line in enumerate(lines):
            if line.strip() == "---" or "第一部分" in line or idx > 44:
                found_divider = True
            if "第二部分：非選擇題" in line:
                in_second_part = True
            
            m = re.match(r'^\s*(?:##\s*|-\s*|>\s*|\|\s*)?(\d+)\.\s*', line)
            if m and found_divider:
                q_num = int(m.group(1))
                if not in_second_part:
                    if q_num >= 1 and q_num <= 25 and q_num not in generated_tags:
                        generated_tags.add(q_num)
                        ans = ANSWERS_112["數學"].get(q_num, "")
                        out_lines.append(f"[q:{q_num}, type:single, ans:{ans}]\n")
                else:
                    if q_num in [1, 2] and f"非選{q_num}" not in generated_tags:
                        generated_tags.add(f"非選{q_num}")
                        out_lines.append(f"[q:非選{q_num}, type:essay]\n")
            out_lines.append(line + "\n")
            
        out_md_path = Path(f"/home/toymsi/documents/examination/國中教育會考/md/112/{subject}.md")
        with open(out_md_path, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)
        print(f"  Wrote clean markdown to {out_md_path}")
        return

    # For 國文, 社會, 自然
    if not w_md_path.exists():
        print(f"  No working file {w_md_path} found.")
        return
    with open(w_md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("<br>", "\n").replace("<BR>", "\n")
    lines = text.split("\n")
        
    out_lines = []
    found_divider = False
    generated_tags = set()
    
    for idx, line in enumerate(lines):
        if line.strip() == "---" or "第一部分" in line or "一、單題" in line or idx > 45:
            found_divider = True
        
        m = re.match(r'^\s*(?:##\s*|-\s*|>\s*|\|\s*)?(\d+)\.\s*', line)
        if m and found_divider:
            q_num = int(m.group(1))
            if q_num in ANSWERS_112[subject] and q_num not in generated_tags:
                generated_tags.add(q_num)
                ans = ANSWERS_112[subject].get(q_num, "")
                out_lines.append(f"[q:{q_num}, type:single, ans:{ans}]\n")
        out_lines.append(line + "\n")
        
    out_md_path = Path(f"/home/toymsi/documents/examination/國中教育會考/md/112/{subject}.md")
    with open(out_md_path, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"  Wrote clean markdown to {out_md_path}")

def run():
    subjects = ["國文", "寫作測驗", "數學", "社會", "自然", "英語閱讀", "英語聽力"]
    for sub in subjects:
        prepare_subject(sub)

if __name__ == "__main__":
    run()
