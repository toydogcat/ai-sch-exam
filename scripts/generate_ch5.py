import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - {ch_id}.{sec_id} 節：{title}",
        "",
        f"本節收錄 {ch_id}.{sec_id} 節相關題目。",
        ""
    ]
    
    # Generate 30 Single Choice
    for i in range(1, 31):
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
        
    # Generate 20 Fill-In
    for i in range(31, 51):
        text, ans_val, sol = fill_templates[i-31](i)
        lines.append("---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{ans_val}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")
        
    return "\n".join(lines)


def generate_review(ch_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 第 {ch_id} 章：{title}",
        "",
        f"本節為第 {ch_id} 章綜合題目。",
        ""
    ]
    
    # Generate 30 Single Choice
    for i in range(1, 31):
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
        
    # Generate 20 Fill-In
    for i in range(31, 51):
        text, ans_val, sol = fill_templates[i-31](i)
        lines.append("---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{ans_val}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")
        
    return "\n".join(lines)


# 5.1: Areas Between Curves
sec1_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"求由曲線 $y = x^2 + {a}$ 與 $y = x + {a}$ 在 $x=0$ 到 $x=1$ 所圍成的區域面積。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{1}}{{6}}$", f"$\\frac{{1}}{{3}}$", f"$\\frac{{1}}{{2}}$", f"$\\frac{{5}}{{6}}$"]
        sol = f"面積為 $\\int_0^1 ((x + {a}) - (x^2 + {a})) dx = \\int_0^1 (x - x^2) dx = [\\frac{{1}}{{2}}x^2 - \\frac{{1}}{{3}}x^3]_0^1 = \\frac{{1}}{{6}}$。"
    else:
        text = f"求曲線 $y = {a}x$ 與 $y = x^2$ 在第一象限所圍成區域的面積。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{{a*a*a}}}{{6}}$", f"$\\frac{{{a}}}{{3}}$", f"$\\frac{{{a*a}}}{{2}}$", f"$1$"]
        sol = f"交點為 $x=0, {a}$。面積為 $\\int_0^{a} ({a}x - x^2) dx = [\\frac{{{a}}}{{2}}x^2 - \\frac{{1}}{{3}}x^3]_0^{a} = \\frac{{{a*a*a}}}{{6}}$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"求兩曲線 $y = {c}x$ 與 $y = x^2$ 圍成區域之面積精確值。"
    sol = f"交點為 $x=0$ 到 $x={c}$。面積為 $\\int_0^{c} ({c}x - x^2) dx = \\frac{{{c}^3}}{{6}}$。當 $c={c} \implies \\frac{{{c*c*c}}}{{6}} = {round((c**3)/6, 2)}$。"
    ans_val = round((c**3)/6, 2)
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 5.2: Volumes
sec2_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"求曲線 $y = {a}\\sqrt{{x}}$ 在 $x=0$ 到 $x=1$ 之間繞 $x$ 軸旋轉所得之旋轉體體積。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{{a*a}\\pi}}{{2}}$", f"${a*a}\\pi$", f"${a}\\pi$", f"$\\pi$"]
        sol = f"圓盤法：$V = \\int_0^1 \\pi ({a}\\sqrt{{x}})^2 dx = \\pi {a*a} [\\frac{{1}}{{2}}x^2]_0^1 = \\frac{{{a*a}\\pi}}{{2}}$。"
    else:
        text = f"求區域由 $y = {a}x$、 $x=1$、與 $y=0$ 所圍成，繞 $x$ 軸旋轉所得之體積。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{{a*a}\\pi}}{{3}}$", f"$\\frac{{{a*a}\\pi}}{{2}}$", f"${a*a}\\pi$", f"$3\\pi$"]
        sol = f"體積 $V = \\pi \\int_0^1 ({a}x)^2 dx = \\frac{{{a*a}\\pi}}{{3}}$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"將曲線 $y = {c}x$ 在 $[0, 2]$ 與 $x$ 軸圍成的區域繞 $x$ 軸旋轉，求其體積之精確值為何（除以 $\\pi$ 的倍數）？"
    sol = f"體積除以 $\\pi$ 為：$\\int_0^2 ({c}x)^2 dx = \\frac{{{c*c*8}}}{{3}}$。計算結果為 {round((c*c*8)/3, 2)}。"
    ans_val = round((c*c*8)/3, 2)
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 5.3: Volumes by Cylindrical Shells
sec3_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"利用圓柱殼層法求曲線 $y = {a}x^2$、 $y=0$、 $x=1$ 繞 $y$ 軸旋轉所得之體積。"
        ans = "D" if i % 4 == 0 else "C"
        opts = [f"$\\frac{{{a}\\pi}}{{2}}$", f"$\\frac{{{a}\\pi}}{{3}}$", f"$\\frac{{{a*2}\\pi}}{{3}}$", f"${a}\\pi$"]
        sol = f"圓柱殼層法：$V = \\int_0^1 2\\pi x ({a}x^2) dx = 2\\pi {a} [\\frac{{1}}{{4}}x^4]_0^1 = \\frac{{{a}\\pi}}{{2}}$。"
    else:
        text = f"求 $y = {a}x$、 $y=0$、 $x=2$ 繞 $y$ 軸旋轉之旋轉體體積。"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"$\\frac{{{a*16}\\pi}}{{3}}$", f"$\\frac{{{a*8}\\pi}}{{3}}$", f"$\\frac{{{a}\\pi}}{{3}}$", f"$16\\pi$"]
        sol = f"圓柱殼層法：$V = \\int_0^2 2\\pi x ({a}x) dx = \\frac{{{a*16}\\pi}}{{3}}$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"利用圓柱殼層法將 $y = {c}x^2$ 在 $x=0$ 到 $x=2$ 繞 $y$ 軸旋轉之旋轉體體積為何（除以 $\\pi$ 的倍數）？"
    sol = f"體積為 $\\int_0^2 2\\pi x ({c}x^2) dx = 8{c}\\pi$。除以 $\\pi$ 為 {c*8}。"
    ans_val = c * 8
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 5.4: Work
sec4_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 2 == 0:
        text = f"一彈簧在拉長 $x$ 公尺時所需的力為 $F(x) = {a}x$ 牛頓，試問將其從 $x=0$ 拉長至 $x=2$ 公尺所需的功為多少焦耳？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a*2}$", f"${a*4}$", f"${a}$", f"$0$"]
        sol = f"功即力的定積分：$W = \\int_0^2 {a}x dx = [\\frac{{{a}}}{{2}}x^2]_0^2 = {a*2}$。"
    else:
        text = f"若將一條拉力函數為 $F(x) = {a}x^2$ 的非線性彈簧從 $x=0$ 拉長至 $x=3$，則所作之功為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*9}$", f"${a*3}$", f"${a*27}$", f"$9$"]
        sol = f"功 $W = \\int_0^3 {a}x^2 dx = [\\frac{{{a}}}{{3}}x^3]_0^3 = {a*9}$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"已知一拉力 $F(x) = {c}x$ 牛頓，求在拉長 $x=0$ 到 $x=4$ 區間內所作之功為何？"
    sol = f"功為 $\\int_0^4 {c}x dx = [\\frac{{{c}}}{{2}}x^2]_0^4 = {c*8}$。"
    ans_val = c * 8
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 5.5: Average Value of a Function
sec5_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"求函數 $f(x) = {a}x^2$ 在區間 $[0, 3]$ 的平均值。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a*3}$", f"${a*9}$", f"${a}$", f"$\\frac{{{a}}}{{3}}$"]
        sol = f"平均值 $f_{{avg}} = \\frac{{1}}{{3}} \\int_0^3 {a}x^2 dx = {a*3}$。"
    else:
        text = f"求函數 $f(x) = {a}x$ 在區間 $[1, 5]$ 的平均值為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*3}$", f"${a*2}$", f"${a*4}$", f"${a}$"]
        sol = f"平均值 $f_{{avg}} = \\frac{{1}}{{4}} \\int_1^5 {a}x dx = {a*3}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"求函數 $f(x) = {c}x$ 在區間 $[0, 6]$ 的平均值之精確值。"
    sol = f"平均值為 $\\frac{{1}}{{6}} \\int_0^6 {c}x dx = {c*3}$。"
    ans_val = c * 3
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# ch5_final: Review
sec_final_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"【綜合】求曲線 $y = x^2 + {a}$ 與 $y = x + {a}$ 在 $x=0$ 到 $x=1$ 所圍成的區域面積。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{1}}{{6}}$", f"$\\frac{{1}}{{3}}$", f"$\\frac{{1}}{{2}}$", f"$1$"]
        sol = f"面積為 $\\int_0^1 (x - x^2) dx = \\frac{{1}}{{6}}$。"
    elif i % 3 == 1:
        text = f"【綜合】求區域由 $y = {a}x$、 $x=1$、與 $y=0$ 所圍成，繞 $x$ 軸旋轉所得之體積。"
        ans = "B" if i % 4 == 1 else "C"
        opts = [f"$\\frac{{{a*a}\\pi}}{{3}}$", f"$\\frac{{{a}\\pi}}{{3}}$", f"${a}\\pi$", f"$1$"]
        sol = f"體積 $V = \\pi \\int_0^1 ({a}x)^2 dx = \\frac{{{a*a}\\pi}}{{3}}$。"
    else:
        text = f"【綜合】求函數 $f(x) = {a}x$ 在區間 $[1, 5]$ 的平均值為何？"
        ans = "C" if i % 4 == 2 else "D"
        opts = [f"${a*3}$", f"${a*2}$", f"${a*4}$", f"${a}$"]
        sol = f"平均值為 $a \\times 3 = {a*3}$。"
    sec_final_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec_final_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"【綜合】求兩曲線 $y = {c}x$ 與 $y = x^2$ 圍成區域之面積精確值。"
        sol = f"面積為 $\\frac{{{c}^3}}{{6}}$。當 $c={c} \implies \\frac{{{c*c*c}}}{{6}} = {round((c**3)/6, 2)}$。"
        ans_val = round((c**3)/6, 2)
    else:
        text = f"【綜合】求函數 $f(x) = {c}x$ 在區間 $[0, 6]$ 的平均值之精確值。"
        sol = f"平均值為 $\\frac{{1}}{{6}} \\int_0^6 {c}x dx = {c*3}$。"
        ans_val = c * 3
    sec_final_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_5")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch5_sec1.md").write_text(generate_section(5, 1, "兩曲線間的面積", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch5_sec2.md").write_text(generate_section(5, 2, "體積", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch5_sec3.md").write_text(generate_section(5, 3, "圓柱殼層法求體積", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch5_sec4.md").write_text(generate_section(5, 4, "功", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch5_sec5.md").write_text(generate_section(5, 5, "函數的平均值", sec5_choices, sec5_fills), encoding='utf-8')
    
    (out_dir / "ch5_final.md").write_text(generate_review(5, "綜合題目", sec_final_choices, sec_final_fills), encoding='utf-8')
    
    print("All Chapter 5 files and review generated successfully.")
