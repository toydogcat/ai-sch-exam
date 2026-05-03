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


# 4.1: The Area and Distance Problems
sec1_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"已知一物體在時間區間 $[0, 2]$ 的速度函數為 $v(t) = {a}t^2$，試問其移動的總距離為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{{a*8}}}{{3}}$", f"$\\frac{{{a*4}}}{{3}}$", f"${a}$", f"$0$"]
        sol = f"距離即為速度函數之定積分。$\\int_0^2 {a}t^2 dt = [\\frac{{{a}}}{{3}}t^3]_0^2 = \\frac{{{a*8}}}{{3}}$。"
    else:
        text = f"若用黎曼和之右端點法來逼近 $f(x) = {a}x$ 在 $[0, 2]$ 區間之面積，將區間等分為 $n$ 份，則 $\\Delta x$ 為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{2}}{{n}}$", f"$\\frac{{1}}{{n}}$", f"$\\frac{{{a}}}{{n}}$", f"$n$"]
        sol = f"區間為 $[0, 2]$，長度為 $2-0 = 2$。等分為 $n$ 份則 $\\Delta x = \\frac{{2}}{{n}}$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"若函數 $f(x) = {c}x$ 在 $[0, 4]$ 之下的面積利用積分計算，則此面積值為何？"
    sol = f"積分式為 $\\int_0^4 {c}x dx = [\\frac{{{c}}}{{2}}x^2]_0^4 = \\frac{{{c}}}{{2}} \\times 16 = {c*8}$。"
    ans_val = c * 8
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 4.2: The Definite Integral
sec2_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 2 == 0:
        text = f"計算定積分 $\\int_1^2 {a} dx$ 的結果。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a}$", f"$0$", f"${a*2}$", f"$1$"]
        sol = f"定積分為 $[{a}x]_1^2 = {a}(2) - {a}(1) = {a}$。"
    else:
        text = f"若 $\\int_a^b f(x)dx = {a}$ 且 $\\int_a^b g(x)dx = 3$，則 $\\int_a^b (f(x) + g(x))dx$ 為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a+3}$", f"${a-3}$", f"$3$", f"$0$"]
        sol = f"定積分之線性性質：$\\int_a^b (f(x) + g(x))dx = \\int_a^b f(x)dx + \\int_a^b g(x)dx = {a} + 3 = {a+3}$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(31, 51):
    c = i - 19
    text = f"已知 $\\int_2^5 {c} dx$ 的精確值為多少？"
    sol = f"定積分為 $[{c}x]_2^5 = {c}(5 - 2) = {c*3}$。"
    ans_val = c * 3
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 4.3: The Fundamental Theorem of Calculus
sec3_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"利用微積分基本定理計算 $\\frac{{d}}{{dx}} \\int_0^x (t^2 + {a}) dt$。"
        ans = "D" if i % 4 == 0 else "C"
        opts = [f"$x^2 + {a}$", f"$2x$", f"$x^2$", f"$2x + {a}$"]
        sol = f"根據 FTC Part 1，$\\frac{{d}}{{dx}} \\int_a^x f(t) dt = f(x)$。故結果為 $x^2 + {a}$。"
    else:
        text = f"求 $\\int_1^3 {a}x^2 dx$ 的值。"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"$\\frac{{{a*26}}}{{3}}$", f"$\\frac{{{a*27}}}{{3}}$", f"$\\frac{{{a}}}{{3}}$", f"$26$"]
        sol = f"積分為 $[\\frac{{{a}}}{{3}}x^3]_1^3 = \\frac{{{a}}}{{3}}(3^3 - 1^3) = \\frac{{{a*26}}}{{3}}$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"若 $F(x) = \\int_0^x {c}t dt$，求 $F'(5)$ 的值。"
    sol = f"由微積分基本定理，$F'(x) = {c}x$。代入 $x=5 \\implies {c} \\times 5 = {c*5}$。"
    ans_val = c * 5
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 4.4: Indefinite Integrals and the Net Change Theorem
sec4_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 2 == 0:
        text = f"求不定積分 $\\int ({a}x^2 + \\sin x) dx$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{{a}}}{{3}}x^3 - \\cos x + C$", f"$\\frac{{{a}}}{{3}}x^3 + \\cos x + C$", f"${a*2}x - \\cos x + C$", f"$\\frac{{{a}}}{{3}}x^3 - \\sin x + C$"]
        sol = f"對各項積分：$\\int {a}x^2 dx = \\frac{{{a}}}{{3}}x^3$，$\\int \\sin x dx = -\\cos x$。故最一般不定積分為 $\\frac{{{a}}}{{3}}x^3 - \\cos x + C$。"
    else:
        text = f"某物體的速度為 $v(t) = {a}t + 1$，求物體在 $t=1$ 到 $t=3$ 之間的淨變化量。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*4+2}$", f"${a*4}$", f"${a}$", f"$4$"]
        sol = f"位移即速度之定積分：$\\int_1^3 ({a}t + 1) dt = [\\frac{{{a}}}{{2}}t^2 + t]_1^3 = (\\frac{{{a}}}{{2}} \\cdot 9 + 3) - (\\frac{{{a}}}{{2}} \\cdot 1 + 1) = {a*4+2}$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(31, 51):
    c = i - 15
    text = f"求 $\\int_0^1 ({c}x^2 + 1) dx$ 之定積分精確值。"
    sol = f"積分為 $[\\frac{{{c}}}{{3}}x^3 + x]_0^1 = \\frac{{{c}}}{{3}} + 1$。當 $c={c} \\implies \\frac{{{c}}}{{3}} + 1 = {round(c/3 + 1, 2)}$。"
    ans_val = round(c / 3 + 1, 2)
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 4.5: The Substitution Rule
sec5_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 2 == 0:
        text = f"利用代換法計算 $\\int 2x(x^2 + 1)^{a} dx$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{1}}{{{a+1}}}(x^2 + 1)^{a+1} + C$", f"$(x^2 + 1)^{a+1} + C$", f"$\\frac{{1}}{{{a}}}(x^2 + 1)^{a} + C$", f"$2(x^2 + 1)^{a+1} + C$"]
        sol = f"令 $u = x^2+1 \\implies du = 2x dx$。積分式變為 $\\int u^{a} du = \\frac{{1}}{{{a+1}}}u^{a+1} + C = \\frac{{1}}{{{a+1}}}(x^2+1)^{a+1} + C$。"
    else:
        text = f"求 $\\int \\sin({a}x) dx$ 之最一般不定積分。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$-\\frac{{1}}{{{a}}}\\cos({a}x) + C$", f"$\\frac{{1}}{{{a}}}\\cos({a}x) + C$", f"$-\\cos({a}x) + C$", f"$\\cos({a}x) + C$"]
        sol = f"令 $u = {a}x \\implies du = {a} dx$。則 $\\int \\sin u \\frac{{1}}{{{a}}} du = -\\frac{{1}}{{{a}}}\\cos u + C = -\\frac{{1}}{{{a}}}\\cos({a}x) + C$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(31, 51):
    c = i - 18
    text = f"利用代換法求定積分 $\\int_0^1 2x(x^2+1)^{c} dx$ 的精確值。"
    sol = f"令 $u = x^2+1 \\implies du=2x dx$。積分上限變為 2，下限變為 1。故為 $\\int_1^2 u^{c} du = [\\frac{{1}}{{{c+1}}} u^{c+1}]_1^2 = \\frac{{2^{c+1} - 1}}{{{c+1}}}$。當 $c={c} \\implies \\frac{{2^{c+1}-1}}{{{c+1}}} = {round((2**(c+1) - 1)/(c+1), 2)}$。"
    ans_val = round((2**(c+1) - 1)/(c+1), 2)
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# ch4_final: Review
sec_final_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"【綜合】求 $\\int ({a}x^2 + 1) dx$ 之最一般反導函數。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{{a}}}{{3}}x^3 + x + C$", f"${a}x + C$", f"$x + C$", f"不存在"]
        sol = f"對各項積分：$\\frac{{{a}}}{{3}}x^3 + x + C$。"
    elif i % 3 == 1:
        text = f"【綜合】求 $\\int_1^2 {a} dx$ 的精確值。"
        ans = "B" if i % 4 == 1 else "C"
        opts = [f"${a}$", f"$0$", f"${a*2}$", f"$1$"]
        sol = f"定積分值為 $[{a}x]_1^2 = {a}$。"
    else:
        text = f"【綜合】求 $\\int \\sin({a}x) dx$ 之最一般不定積分。"
        ans = "C" if i % 4 == 2 else "D"
        opts = [f"$-\\frac{{1}}{{{a}}}\\cos({a}x) + C$", f"$\\frac{{1}}{{{a}}}\\cos({a}x) + C$", f"$-\\cos({a}x) + C$", f"$\\cos({a}x) + C$"]
        sol = f"令 $u = {a}x \\implies -\\frac{{1}}{{{a}}}\\cos({a}x) + C$。"
    sec_final_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec_final_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"【綜合】若 $F(x) = \\int_0^x {c}t dt$，求 $F'(2)$ 之值。"
        sol = f"由微積分基本定理，$F'(x) = {c}x$。代入 $x=2 \\implies {c} \\times 2 = {c*2}$。"
        ans_val = c * 2
    else:
        text = f"【綜合】已知 $\\int_1^3 {c} dx$ 的精確值為多少？"
        sol = f"定積分值為 $[{c}x]_1^3 = {c}(3 - 1) = {c*2}$。"
        ans_val = c * 2
    sec_final_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_4")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch4_sec1.md").write_text(generate_section(4, 1, "面積與距離問題", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch4_sec2.md").write_text(generate_section(4, 2, "定積分", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch4_sec3.md").write_text(generate_section(4, 3, "微積分基本定理", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch4_sec4.md").write_text(generate_section(4, 4, "不定積分與淨變化定理", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch4_sec5.md").write_text(generate_section(4, 5, "代換法", sec5_choices, sec5_fills), encoding='utf-8')
    
    (out_dir / "ch4_final.md").write_text(generate_review(4, "綜合題目", sec_final_choices, sec_final_fills), encoding='utf-8')
    
    print("All Chapter 4 files and review generated successfully.")
