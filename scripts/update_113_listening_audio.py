import re
from pathlib import Path

md_path = Path("/home/toymsi/documents/examination/國中教育會考/md/113/英語聽力.md")

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

mp3_map = {
    1: '04 第1題.mp3',
    2: '05 第2題.mp3',
    3: '06 第3題.mp3',
    4: '08 第4題.mp3',
    5: '09 第5題.mp3',
    6: '10 第6題.mp3',
    7: '11 第7題.mp3',
    8: '12 第8題.mp3',
    9: '13 第9題.mp3',
    10: '14 第10題.mp3',
    11: '15 第11題.mp3',
    12: '17 第12題.mp3',
    13: '18 第13題.mp3',
    14: '19 第14題.mp3',
    15: '20 第15題.mp3',
    16: '21 第16題.mp3',
    17: '22 第17題.mp3',
    18: '23 第18題.mp3',
    19: '24 第19題.mp3',
    20: '25 第20題.mp3',
    21: '26 第21題.mp3'
}

def replacer(match):
    q_num = int(match.group(1))
    q_type = match.group(2)
    q_ans = match.group(3)
    if q_num in mp3_map:
        audio_filename = mp3_map[q_num]
        audio_path = f"/home/toymsi/documents/examination/Github/ai-sch-exam/public/audio/cap/113/英語聽力/{audio_filename}"
        return f"[q:{q_num}, type:{q_type}, ans:{q_ans}, audio:{audio_path}]"
    return match.group(0)

# Replace the metadata tag
new_content = re.sub(r'\[q:(\d+),\s*type:([\w/]+),\s*ans:([^\]]+)\]', replacer, content)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated 英語聽力.md successfully!")
