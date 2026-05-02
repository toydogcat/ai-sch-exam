import json
import re
import os
from pathlib import Path

def parse_calculus_bank(bank_dir, output_path):
    if not os.path.exists(bank_dir):
        print(f"Directory not found: {bank_dir}")
        return

    questions = []
    
    # Iterate through all md files in the bank directory
    for md_file in sorted(Path(bank_dir).rglob("*.md")):
        print(f"Parsing {md_file.name}...")
        
        # Determine the chapter name from the filename
        stem = md_file.stem.lower()
        if stem == 'ch0_sec1':
            chapter_name = 'Ch0 0.1節：代數與算術基礎'
        elif stem == 'ch0_sec2':
            chapter_name = 'Ch0 0.2節：幾何與三角函數'
        elif stem == 'ch1_sec1':
            chapter_name = 'Ch1 1.1節：函數的表示法'
        elif stem == 'ch1_sec2':
            chapter_name = 'Ch1 1.2節：數學模型與基本函數'
        elif stem == 'ch1_sec3':
            chapter_name = 'Ch1 1.3節：新舊函數的變換'
        elif stem == 'ch1_sec4':
            chapter_name = 'Ch1 1.4節：切線與速度問題'
        elif stem == 'ch1_sec5':
            chapter_name = 'Ch1 1.5節：函數的極限'
        elif stem == 'ch1_sec6':
            chapter_name = 'Ch1 1.6節：利用極限定律計算極限'
        elif stem == 'ch1_sec7':
            chapter_name = 'Ch1 1.7節：極限的精確定義'
        elif stem == 'ch1_sec8':
            chapter_name = 'Ch1 1.8節：函數的連續性'
        elif stem == 'ch2_sec1':
            chapter_name = 'Ch2 2.1節：導數與變化率'
        elif stem == 'ch2_sec2':
            chapter_name = 'Ch2 2.2節：導數作為一個函數'
        elif stem == 'ch2_sec3':
            chapter_name = 'Ch2 2.3節：微分公式'
        elif stem == 'ch2_sec4':
            chapter_name = 'Ch2 2.4節：三角函數的導數'
        elif stem == 'ch2_sec5':
            chapter_name = 'Ch2 2.5節：連鎖律'
        elif stem == 'ch2_sec6':
            chapter_name = 'Ch2 2.6節：隱函數微分'
        elif stem == 'ch2_sec7':
            chapter_name = 'Ch2 2.7節：自然與社會科學中的變化率'
        elif stem == 'ch2_sec8':
            chapter_name = 'Ch2 2.8節：相關變率'
        elif stem == 'ch2_sec9':
            chapter_name = 'Ch2 2.9節：線性逼近與微分'
        elif stem == 'ch3_sec1':
            chapter_name = 'Ch3 3.1節：最大值與最小值'
        elif stem == 'ch3_sec2':
            chapter_name = 'Ch3 3.2節：均值定理'
        elif stem == 'ch3_sec3':
            chapter_name = 'Ch3 3.3節：導函數如何告訴我們圖形的形狀'
        elif stem == 'ch3_sec4':
            chapter_name = 'Ch3 3.4節：無窮遠處的極限與水平漸近線'
        elif stem == 'ch3_sec5':
            chapter_name = 'Ch3 3.5節：曲線描繪摘要'
        elif stem == 'ch3_sec6':
            chapter_name = 'Ch3 3.6節：微積分與科技作圖'
        elif stem == 'ch3_sec7':
            chapter_name = 'Ch3 3.7節：最佳化問題'
        elif stem == 'ch3_sec8':
            chapter_name = 'Ch3 3.8節：牛頓法'
        elif stem == 'ch3_sec9':
            chapter_name = 'Ch3 3.9節：反導函數'
        elif stem == 'ch4_sec1':
            chapter_name = 'Ch4 4.1節：面積與距離問題'
        elif stem == 'ch4_sec2':
            chapter_name = 'Ch4 4.2節：定積分'
        elif stem == 'ch4_sec3':
            chapter_name = 'Ch4 4.3節：微積分基本定理'
        elif stem == 'ch4_sec4':
            chapter_name = 'Ch4 4.4節：不定積分與淨變化定理'
        elif stem == 'ch4_sec5':
            chapter_name = 'Ch4 4.5節：代換法'
        else:
            chapter_name = md_file.stem.replace("_", " ").title()

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by metadata tags
        tag_pattern = r'\[q:(\d+),\s*type:(\w+),\s*ans:([^\]]+)\]'
        matches = list(re.finditer(tag_pattern, content))

        for i in range(len(matches)):
            m = matches[i]
            q_num = int(m.group(1))
            q_type = m.group(2)
            q_ans = m.group(3).strip()

            start_pos = m.end()
            end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)

            block = content[start_pos:end_pos].strip()

            # Split into question text and solution
            solution = ""
            if "<!-- solution -->" in block:
                parts = block.split("<!-- solution -->")
                clean_block = parts[0].strip()
                solution = parts[1].strip()
            else:
                clean_block = block

            # Process options if single choice
            options = []
            if q_type == 'single':
                # Extract options from clean_block
                opt_matches = re.findall(r'\(([A-D])\)\s*(.*?)(?=\s*\([A-D]\)|$)', clean_block, re.DOTALL)
                if opt_matches:
                    for opt_label, opt_val in opt_matches:
                        options.append(opt_val.strip())
                    # Isolate question text before options
                    clean_block = re.split(r'\([A-D]\)', clean_block)[0].strip()

            questions.append({
                "number": q_num,
                "text": clean_block,
                "options": options,
                "answer": q_ans,
                "type": q_type,
                "solution": solution,
                "chapter": chapter_name,
                "score": 10
            })

    print(f"Parsed a total of {len(questions)} questions from all chapters.")

    # Write JSON output per chapter
    grouped_questions = {}
    for q in questions:
        match = re.search(r'[Cc]h(\d+)', q["chapter"])
        if match:
            ch_key = f"ch{match.group(1)}"
        else:
            ch_key = "ch0"
        if ch_key not in grouped_questions:
            grouped_questions[ch_key] = []
        grouped_questions[ch_key].append(q)

    out_dir = Path(output_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    for ch_key, ch_questions in grouped_questions.items():
        ch_output_path = out_dir / f"calculus_bank_{ch_key}.json"
        with open(ch_output_path, 'w', encoding='utf-8') as f:
            json.dump({ "questions": ch_questions }, f, ensure_ascii=False, indent=2)
        print(f"Successfully saved {ch_key} bank to {ch_output_path}")

if __name__ == "__main__":
    parse_calculus_bank(
        "/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank",
        "/home/toymsi/documents/examination/Github/ai-sch-exam/public/json/calculus_bank.json"
    )
