import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    """
    Generates a section markdown file.
    choice_templates: list of 20 lambda functions (or templates) creating (text, correct_ans, opts, solution)
    fill_templates: list of 10 lambda functions (or templates) creating (text, ans, solution)
    """
    lines = [
        f"# 微積分題庫 - 1.{sec_id} 節：{title}",
        "",
        f"本節收錄 1.{sec_id} 節相關題目。",
        ""
    ]
    
    # Generate 20 Single Choice
    for i in range(1, 21):
        text, ans, opts, sol = choice_templates[i-1](i)
        
        # Format options
        options_formatted = []
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        
        # Swap correct option to its place
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


# Section 1.3: New Functions from Old Functions
# Choice Questions
sec3_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 3 == 0:
        text = f"設 $f(x) = x^2$，若將此函數向右平移 {a} 個單位、向上平移 3 個單位，新函數 $g(x)$ 為何？"
        ans = "A" if i % 4 == 0 else ("B" if i % 4 == 1 else ("C" if i % 4 == 2 else "D"))
        opts = [f"$(x-{a})^2 + 3$", f"$(x+{a})^2 + 3$", f"$(x-{a})^2 - 3$", f"$(x+{a})^2 - 3$"]
        sol = f"向右平移 {a} 個單位代表將 $x$ 替換為 $x-{a}$，向上平移 3 個單位代表加上 3。故為 $(x-{a})^2 + 3$。"
    elif i % 3 == 1:
        text = f"已知 $f(x) = {a}x + 1$，$g(x) = x^2$，試求複合函數 $(f \\circ g)(x)$ 的解析式為何？"
        ans = "B" if i % 4 == 0 else ("C" if i % 4 == 1 else ("D" if i % 4 == 2 else "A"))
        opts = [f"${a}x^2 + 1$", f"$({a}x+1)^2$", f"${a}x^2 + {a}$", f"$x^2 + {a}$"]
        sol = f"複合函數 $(f \\circ g)(x) = f(g(x)) = f(x^2) = {a}x^2 + 1$。"
    else:
        text = f"已知 $f(x) = \\sqrt{{x}}$，若要將圖形沿垂直方向拉伸 {a} 倍，應如何表示新函數？"
        ans = "C" if i % 4 == 0 else ("D" if i % 4 == 1 else ("A" if i % 4 == 2 else "B"))
        opts = [f"${a}\\sqrt{{x}}$", f"$\\sqrt{{{a}x}}$", f"$\\sqrt{{x}} + {a}$", f"$\\sqrt{{x - {a}}}$"]
        sol = f"沿垂直方向拉伸 {a} 倍，代表將函數值乘以 {a}，故表示為 ${a}\\sqrt{{x}}$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    ans_val = c * c + 1
    text = f"已知 $f(x) = x^2 + 1$，$g(x) = x - {c}$，試求 $(f \\circ g)({c})$ 的精確值為何？"
    sol = f"首先計算 $g({c}) = {c} - {c} = 0$，再將其代入 $f(x)$ 中：$f(0) = 0^2 + 1 = 1$。所以 $(f \\circ g)({c}) = 1$。"
    # Note: making sure ans matches ans_val for mathematical correctness
    ans_val = 1
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# Section 1.4: The Tangent and Velocity Problems
sec4_choices = []
for i in range(1, 21):
    v = i + 1
    if i % 2 == 0:
        text = f"一物體的運動方程式為 $s(t) = {v}t^2$，試問在 $t = 1$ 秒時的瞬時速度為多少？"
        ans = "A" if i % 4 == 0 else ("B" if i % 4 == 1 else ("C" if i % 4 == 2 else "D"))
        opts = [f"${v*2}$", f"${v}$", f"${v*3}$", f"${v+1}$"]
        sol = f"利用極限或微分：$v(t) = s'(t) = {v*2}t$。在 $t=1$ 時，$v(1) = {v*2}$。"
    else:
        text = f"已知曲線 $y = x^2 + {v}x$，試求其在 $x = 0$ 處的切線斜率為何？"
        ans = "B" if i % 4 == 0 else ("C" if i % 4 == 1 else ("D" if i % 4 == 2 else "A"))
        opts = [f"${v}$", f"${v+2}$", f"$0$", f"$1$"]
        sol = f"對 $y$ 微分得 $y' = 2x + {v}$。代入 $x=0$ 得斜率為 ${v}$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 15
    ans_val = c * 2
    text = f"若某物體之位移 $s(t) = {c}t^2 + 2t$，試求當 $t=1$ 秒時之瞬時速度為何？"
    sol = f"瞬時速度為 $s'(t) = {c*2}t + 2$。在 $t=1$ 時，速度為 ${c*2} \\times 1 + 2 = {c*2+2}$。"
    ans_val = c * 2 + 2
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# Section 1.5: The Limit of a Function
sec5_choices = []
for i in range(1, 21):
    v = i + 3
    if i % 2 == 0:
        text = f"求極限值 $\\lim_{{x \\to {v}}} (x^2 - {v})$ 的結果為何？"
        ans = "C" if i % 4 == 0 else ("D" if i % 4 == 1 else ("A" if i % 4 == 2 else "B"))
        opts = [f"${v*v - v}$", f"${v*v + v}$", f"${v*v}$", f"$0$"]
        sol = f"直接代入得：${v}^2 - {v} = {v*v - v}$。"
    else:
        text = f"已知 $\\lim_{{x \\to 2^+}} f(x) = {v}$，$\\lim_{{x \\to 2^-}} f(x) = {v}$，則 $\\lim_{{x \\to 2}} f(x)$ 為何？"
        ans = "B" if i % 4 == 0 else ("A" if i % 4 == 1 else ("D" if i % 4 == 2 else "C"))
        opts = [f"${v}$", f"$2$", f"不存在", f"$\\infty$"]
        sol = f"由於左右極限相等，故極限存在且等於左右極限值 ${v}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    ans_val = c * 3
    text = f"求極限值 $\\lim_{{x \\to 3}} ({c}x + 4)$。"
    sol = f"直接代入 $x=3$：${c}(3) + 4 = {c*3+4}$。"
    ans_val = c * 3 + 4
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# Section 1.6: Calculating Limits Using the Limit Laws
sec6_choices = []
for i in range(1, 21):
    v = i + 1
    if i % 2 == 0:
        text = f"求極限值 $\\lim_{{x \\to {v}}} \\frac{{x^2 - {v*v}}}{{x - {v}}}$。"
        ans = "A" if i % 4 == 0 else ("B" if i % 4 == 1 else ("C" if i % 4 == 2 else "D"))
        opts = [f"${v*2}$", f"${v}$", f"$0$", f"不存在"]
        sol = f"因式分解分子得 $x+{v}$，代入得 ${v*2}$。"
    else:
        text = f"利用夾擠定理，若對於所有 $x \\neq 0$，$-x^2 \\leq f(x) \\leq x^2$，求 $\\lim_{{x \\to 0}} f(x)$ 的值。"
        ans = "B" if i % 4 == 0 else ("C" if i % 4 == 1 else ("D" if i % 4 == 2 else "A"))
        opts = [f"$0$", f"$1$", f"不存在", f"$\\infty$"]
        sol = f"由於 $\\lim_{{x \\to 0}} (-x^2) = 0$ 且 $\\lim_{{x \\to 0}} x^2 = 0$，由夾擠定理得其極限為 0。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 15
    text = f"求極限值 $\\lim_{{x \\to 1}} (x^3 + {c}x + 2)$。"
    sol = f"直接代入 $x=1$：$1^3 + {c}(1) + 2 = {c+3}$。"
    ans_val = c + 3
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# Section 1.7: The Precise Definition of a Limit
sec7_choices = []
for i in range(1, 21):
    v = i + 2
    if i % 2 == 0:
        text = f"設 $\\lim_{{x \\to 1}} ({v}x - 1) = {v-1}$，若 $\\epsilon = 0.1$，試求最大的 $\\delta$ 滿足定義。"
        ans = "D" if i % 4 == 0 else ("C" if i % 4 == 1 else ("B" if i % 4 == 2 else "A"))
        # epsilon / coefficient
        val = round(0.1 / v, 4)
        opts = [f"${val}$", f"$0.1$", f"$0.05$", f"$0.2$"]
        sol = f"由 $|({v}x-1) - ({v-1})| < 0.1 \\implies {v}|x-1| < 0.1 \\implies |x-1| < \\frac{{0.1}}{{{v}}}$。故 $\\delta = {val}$。"
    else:
        text = f"極限精確定義中，若 $|x - a| < \\delta$，則何者成立？"
        ans = "A" if i % 4 == 0 else ("B" if i % 4 == 1 else ("C" if i % 4 == 2 else "D"))
        opts = [f"$|f(x) - L| < \\epsilon$", f"$|f(x) - a| < \\epsilon$", f"$|x - L| < \\epsilon$", f"$|f(x) - L| > \\epsilon$"]
        sol = f"根據極限定義，當 $x$ 趨近於 $a$（$|x - a| < \\delta$）時，函數值趨近於 $L$（$|f(x) - L| < \\epsilon$）。"
    sec7_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec7_fills = []
for i in range(21, 31):
    c = i - 16
    text = f"若 $\\lim_{{x \\to 2}} {c}x = {c*2}$，且 $\\epsilon = 0.2$，求對應的 $\\delta$ 最大值除以 0.1 後的值為多少？"
    val = (0.2 / c) / 0.1
    sol = f"$\\delta = \\frac{{\\epsilon}}{{{c}}} = \\frac{{0.2}}{{{c}}}$。除以 0.1 即為 $\\frac{{2}}{{{c}}}$。其值為 {round(2/c, 2)}。"
    ans_val = round(2 / c, 2)
    sec7_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# Section 1.8: Continuity
sec8_choices = []
for i in range(1, 21):
    v = i + 1
    if i % 2 == 0:
        text = f"已知函數 $f(x) = \\frac{{x-1}}{{x - {v}}}$，試問該函數在何處不連續？"
        ans = "C" if i % 4 == 0 else ("D" if i % 4 == 1 else ("A" if i % 4 == 2 else "B"))
        opts = [f"$x = {v}$", f"$x = 1$", f"$x = 0$", f"全區域連續"]
        sol = f"分母不可為 0，當 $x - {v} = 0 \\implies x = {v}$ 時不連續。"
    else:
        text = f"設 $f(x)$ 在 $[0, 1]$ 上連續，若 $f(0) = -1$ 且 $f(1) = 1$，由中間值定理可知 $f(c) = 0$ 在區間內至少有幾個根？"
        ans = "A" if i % 4 == 0 else ("B" if i % 4 == 1 else ("C" if i % 4 == 2 else "D"))
        opts = [f"$1$", f"$2$", f"$0$", f"無限多"]
        sol = f"因 $f(0) \\cdot f(1) < 0$，根據中間值定理，在區間 $(0, 1)$ 內至少存在一個根。"
    sec8_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec8_fills = []
for i in range(21, 31):
    c = i - 15
    text = f"若函數 $f(x) = {c}x^2 + 1$ 在 $\\mathbb{{R}}$ 上連續，試求 $f(2)$ 的精確值為何？"
    sol = f"直接代入 $x=2$：${c}(2)^2 + 1 = {c*4+1}$。"
    ans_val = c * 4 + 1
    sec8_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_1")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch1_sec3.md").write_text(generate_section(1, 3, "新舊函數的變換", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch1_sec4.md").write_text(generate_section(1, 4, "切線與速度問題", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch1_sec5.md").write_text(generate_section(1, 5, "函數的極限", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch1_sec6.md").write_text(generate_section(1, 6, "利用極限定律計算極限", sec6_choices, sec6_fills), encoding='utf-8')
    (out_dir / "ch1_sec7.md").write_text(generate_section(1, 7, "極限的精確定義", sec7_choices, sec7_fills), encoding='utf-8')
    (out_dir / "ch1_sec8.md").write_text(generate_section(1, 8, "函數的連續性", sec8_choices, sec8_fills), encoding='utf-8')
    
    print("Additional sections generated successfully.")
