import json
import re
import shutil
from pathlib import Path


SOURCE_ROOT = Path("/home/toymsi/documents/examination/大學入學考試/md/112")
PUBLIC_ROOT = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/public")
OUTPUT_ROOT = PUBLIC_ROOT / "json/ceec/112"

GSAT_META = {
    "國寫": {"title": "112 學年度學科能力測驗 - 國語文寫作能力測驗", "duration": 90},
    "國綜": {"title": "112 學年度學科能力測驗 - 國語文綜合能力測驗", "duration": 90},
    "英文": {"title": "112 學年度學科能力測驗 - 英文考科", "duration": 100},
    "數A": {"title": "112 學年度學科能力測驗 - 數學 A 考科", "duration": 100},
    "數B": {"title": "112 學年度學科能力測驗 - 數學 B 考科", "duration": 100},
    "社會": {"title": "112 學年度學科能力測驗 - 社會考科", "duration": 110},
    "自然": {"title": "112 學年度學科能力測驗 - 自然考科", "duration": 110},
}

AST_META = {
    "數甲": {"md": "數甲.md", "json": "數甲", "title": "112 學年度分科測驗 - 數學甲考科", "duration": 80},
    "物理": {"md": "物理.md", "json": "物理", "title": "112 學年度分科測驗 - 物理考科", "duration": 80},
    "化學": {"md": "化學.md", "json": "化學", "title": "112 學年度分科測驗 - 化學考科", "duration": 80},
    "生物": {"md": "生物.md", "json": "生物", "title": "112 學年度分科測驗 - 生物考科", "duration": 80},
    "歷史": {"md": "歷史.md", "json": "歷史", "title": "112 學年度分科測驗 - 歷史考科", "duration": 80},
    "地理": {"md": "地理.md", "json": "地理", "title": "112 學年度分科測驗 - 地理考科", "duration": 80},
    "公民": {"md": "社會.md", "json": "公民", "title": "112 學年度分科測驗 - 公民與社會考科", "duration": 80},
}

TAG_RE = re.compile(r"\[q:(\d+),\s*type:\s*([^,\]]+)(?:,\s*ans:\s*([^\]]+))?(?:,\s*audio:([^,\]]+))?.*?\]")
PASSAGE_RE = re.compile(r"(?m)^(?:#{1,6}\s*)?\*\*題組[:：].*?\*\*.*$|^#{1,6}\s*.*?題組.*$")
RANGE_RE = re.compile(r"(\d+)\s*[-~－—]\s*(\d+)")


def passage_end(passage):
    match = RANGE_RE.search(passage or "")
    return int(match.group(2)) if match else None


def normalize_answer(q_type, ans):
    ans = (ans or "").strip()
    if q_type == "multi":
        if "," in ans:
            return [part.strip() for part in ans.split(",") if part.strip()]
        if ans.isalpha() and ans.upper() == ans and len(ans) > 1:
            return list(ans)
        if ans.isdigit() and len(ans) > 1:
            return list(ans)
        return [ans] if ans else []
    return ans


def image_replacer(exam_type, subject):
    def repl(match):
        src = Path(match.group(1))
        dest_rel = Path("images/ceec/112") / exam_type / subject / src.name
        dest_abs = PUBLIC_ROOT / dest_rel
        if src.exists():
            dest_abs.parent.mkdir(parents=True, exist_ok=True)
            if src.resolve() != dest_abs.resolve():
                shutil.copy2(src, dest_abs)
        else:
            print(f"Warning: missing image {src}")
        return f'<br><img src="/{dest_rel.as_posix()}" style="max-width:100%; display:block; margin:10px 0;">'
    return repl


def render_table(lines):
    if len(lines) < 2:
        return "\n".join(lines)
    sep = lines[1].strip()
    if not (sep.startswith("|") and sep.endswith("|") and all(c in " |:-" for c in sep)):
        return "\n".join(lines)
    headers = [h.strip() for h in lines[0].split("|")[1:-1]]
    rows = []
    for line in lines[2:]:
        cols = [c.strip() for c in line.split("|")[1:-1]]
        cols += [""] * max(0, len(headers) - len(cols))
        rows.append(cols[:len(headers)])
    html = ['<div class="custom-table-container" style="overflow-x:auto; margin: 1.5rem 0; white-space: normal;">']
    html.append('<table class="custom-exam-table" style="width:100%; border-collapse: collapse; border: 1px solid #dee2e6; font-size: 1rem; background: #fff; border-radius: 6px; white-space: normal;">')
    html.append('<thead style="background: #f8f9fa; white-space: normal;"><tr>')
    for h in headers:
        html.append(f'<th style="border: 1px solid #dee2e6; padding: 12px 16px; text-align: left; font-weight: 700; color: #2c3e50; white-space: normal;">{h}</th>')
    html.append('</tr></thead><tbody style="white-space: normal;">')
    for row in rows:
        html.append('<tr style="white-space: normal;">')
        for cell in row:
            html.append(f'<td style="border: 1px solid #dee2e6; padding: 12px 16px; color: #34495e; line-height: 1.6; white-space: normal;">{cell}</td>')
        html.append('</tr>')
    html.append('</tbody></table></div>')
    return "".join(html)


def markdown_tables_to_html(text):
    lines = text.splitlines()
    out = []
    table = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") > 1:
            table.append(stripped)
            continue
        if table:
            out.append(render_table(table))
            table = []
        out.append(line)
    if table:
        out.append(render_table(table))
    return "\n".join(out)


def clean_common_noise(text):
    text = re.sub(r"(?m)^-{1,3}\s*\d+\s*-{1,3}\s*$", "", text)
    text = re.sub(r"(?m)^第\s*\d+\s*頁\s*共\s*\d+\s*頁.*$", "", text)
    text = re.sub(r"(?m)^.*請記得在答題卷.*$", "", text)
    return text.strip()


def split_options(text, q_type):
    if q_type not in {"single", "multi"}:
        return text.strip(), []
    table_result = split_table_options(text)
    if table_result:
        return table_result
    labels = "ABCDEFGHIJ"
    pattern = re.compile(r"\(([A-J])\)\s*(.*?)(?=\s*\([A-J]\)|\Z)", re.S)
    matches = list(pattern.finditer(text))
    label_kind = "letter"
    if len(matches) < 2:
        pattern = re.compile(r"\(([1-9])\)\s*(.*?)(?=\s*\([1-9]\)|\Z)", re.S)
        matches = list(pattern.finditer(text))
        label_kind = "number"
    if len(matches) < 2:
        return text.strip(), []
    first = matches[0]
    q_text = text[:first.start()].strip()
    options = []
    for match in matches:
        label, body = match.group(1), match.group(2).strip()
        body = body.rstrip()
        if label_kind == "number":
            options.append(f"({label}) {body}")
        else:
            options.append(body)
    return q_text, options


def split_table_options(text):
    lines = text.splitlines()
    start = None
    end = None
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [cell.strip() for cell in stripped.split("|")[1:-1]]
        if cells and re.fullmatch(r"\([A-J]\)", cells[0]):
            start = idx
            break
    if start is None:
        return None

    table_start = start
    while table_start > 0:
        prev = lines[table_start - 1].strip()
        if not (prev.startswith("|") and prev.endswith("|")):
            break
        table_start -= 1

    end = start
    while end < len(lines):
        stripped = lines[end].strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            break
        end += 1

    options = []
    for line in lines[start:end]:
        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        if cells and re.fullmatch(r"\([A-J]\)", cells[0]):
            options.append(" | ".join(cell for cell in cells[1:] if cell))

    if len(options) < 2:
        return None

    q_text_lines = lines[:table_start] + lines[end:]
    return "\n".join(q_text_lines).strip(), options


def finalize_text(text, exam_type, subject):
    text = clean_common_noise(text)
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"!\[.*?\]\((.*?)\)", image_replacer(exam_type, subject), text)
    return markdown_tables_to_html(text).strip()


def parse_markdown(md_path, exam_type, subject, title, duration):
    content = md_path.read_text(encoding="utf-8")
    matches = list(TAG_RE.finditer(content))
    questions = []
    current_passage = ""
    current_passage_end = None

    for i, match in enumerate(matches):
        q_num = int(match.group(1))
        q_type = match.group(2).strip()
        q_ans = normalize_answer(q_type, match.group(3))
        audio = (match.group(4) or "").strip()

        if current_passage_end is not None and q_num > current_passage_end:
            current_passage = ""
            current_passage_end = None

        block_end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[match.end():block_end].strip()
        next_passage = ""
        passage_match = PASSAGE_RE.search(block)
        if passage_match:
            next_passage = block[passage_match.start():].strip()
            block = block[:passage_match.start()].strip()

        q_text, options = split_options(block, q_type)
        q_text = finalize_text(q_text, exam_type, subject)
        options = [finalize_text(opt, exam_type, subject) for opt in options]
        passage_text = finalize_text(current_passage, exam_type, subject) if current_passage else ""

        question = {
            "number": q_num,
            "text": q_text,
            "passage": passage_text,
            "options": options,
            "answer": q_ans,
            "type": q_type,
            "score": 2,
        }
        if audio:
            question["audio"] = audio
        questions.append(question)

        if next_passage:
            current_passage = next_passage
            current_passage_end = passage_end(current_passage)

    return {"title": title, "duration": duration, "questions": questions}


def write_json(data, out_path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {out_path} ({len(data['questions'])} questions)")


def main():
    for subject, meta in GSAT_META.items():
        md_path = SOURCE_ROOT / "學測" / f"{subject}.md"
        if not md_path.exists():
            print(f"Skip missing {md_path}")
            continue
        data = parse_markdown(md_path, "學測", subject, meta["title"], meta["duration"])
        write_json(data, OUTPUT_ROOT / "學測" / f"{subject}.json")

    for subject, meta in AST_META.items():
        md_path = SOURCE_ROOT / "分科" / meta["md"]
        if not md_path.exists():
            print(f"Skip missing {md_path}")
            continue
        data = parse_markdown(md_path, "分科", subject, meta["title"], meta["duration"])
        write_json(data, OUTPUT_ROOT / "分科" / f"{meta['json']}.json")


if __name__ == "__main__":
    main()
