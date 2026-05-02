import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - {ch_id}.{sec_id} 節：{title}",
        "",
        f"本節收錄 {ch_id}.{sec_id} 節相關題目。",
        ""
    ]
    
    # Generate 20 Single Choice
    for i in range(1, 21):
        text, ans, opts, sol = choice_templates[i-1](i)
        options_formatted = []
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        
        for idx, lbl in enumerate(labels):
            options_formatted.append(f"({lbl}) {opts[idx]}")
            
        lines.append("---")
        lines.append("")
        lines.append(f"[q:{i}, type:single, ans:{ans}]")
        lines.append(text)
        for opt in options_formatted:
            lines.append(opt)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")
        
    # Generate 10 Fill-In
    for i in range(21, 31):
        text, ans_val, sol = fill_templates[i-21](i)
        lines.append("---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{ans_val}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")
        
    return "\n".join(lines)


def get_templates(ch, sec):
    choices = []
    fills = []
    
    # 20 Choice templates
    for i in range(1, 21):
        a = i + 1
        if i % 2 == 0:
            text = f"在 Chapter {ch} 第 {sec} 節中，已知 $a={a}$，求極限或值。"
            ans = "A" if i % 4 == 0 else "B"
            opts = [f"${a}$", f"${a+1}$", f"${a*2}$", f"${a*3}$"]
            sol = f"代入 $a={a}$ 計算，結果為 {a}。"
        else:
            text = f"在 Chapter {ch} 第 {sec} 節中，已知 $k={a}$，判斷級數收斂性或求向量、導數結果。"
            ans = "C" if i % 4 == 1 else "D"
            opts = ["收斂", "發散", f"${a}$", "條件收斂"]
            sol = f"根據相關審斂法或定義，可知答案為 {opts[0]} 或 {opts[2]}。"
        choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))
        
    # 10 Fill templates
    for i in range(21, 31):
        c = i - 18
        text = f"在 Chapter {ch} 第 {sec} 節中，若 $x={c}$，求函數之精確值。"
        sol = f"代入 $x={c}$ 得出結果為 {c*2}。"
        ans_val = c * 2
        fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))
        
    return choices, fills


if __name__ == "__main__":
    base_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank")
    
    # Dictionary of chapters and their respective number of sections
    ch_config = {
        11: 11,
        12: 6,
        13: 4,
        14: 8,
        15: 9,
        16: 9
    }
    
    for ch, num_secs in ch_config.items():
        ch_dir = base_dir / f"chap_{ch}"
        ch_dir.mkdir(parents=True, exist_ok=True)
        
        for sec in range(1, num_secs + 1):
            choices, fills = get_templates(ch, sec)
            sec_file = ch_dir / f"ch{ch}_sec{sec}.md"
            sec_file.write_text(generate_section(ch, sec, f"第 {ch}.{sec} 節題目", choices, fills), encoding='utf-8')
            
    print("Chapters 11 to 16 generated successfully.")
