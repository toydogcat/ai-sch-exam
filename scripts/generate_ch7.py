import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 7.{sec_id} 節：{title}",
        "",
        f"本節收錄 7.{sec_id} 節相關題目。",
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


# 7.1: Integration by Parts
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用分部積分法（Integration by Parts），求 $\\int x e^{{{a}x}} dx$ 的最一般不定積分。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{x}}{{{a}}}e^{{{a}x}} - \\frac{{1}}{{{a*a}}}e^{{{a}x}} + C$", f"$x e^{{{a}x}} - e^{{{a}x}} + C$", f"$\\frac{{x}}{{{a}}}e^{{{a}x}} + C$", f"$\\frac{{1}}{{{a*a}}}e^{{{a}x}} + C$"]
        sol = f"令 $u=x, dv=e^{{{a}x}}dx \\implies du=dx, v=\\frac{{1}}{{{a}}}e^{{{a}x}}$。故分部積分得 $\\frac{{x}}{{{a}}}e^{{{a}x}} - \\int \\frac{{1}}{{{a}}}e^{{{a}x}} dx = \\frac{{x}}{{{a}}}e^{{{a}x}} - \\frac{{1}}{{{a*a}}}e^{{{a}x}} + C$。"
    else:
        text = f"求 $\\int x \\cos({a}x) dx$ 的最一般不定積分。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{x}}{{{a}}}\\sin({a}x) + \\frac{{1}}{{{a*a}}}\\cos({a}x) + C$", f"$\\frac{{x}}{{{a}}}\\sin({a}x) - \\frac{{1}}{{{a*a}}}\\cos({a}x) + C$", f"$x\\sin({a}x) + C$", f"$\\frac{{1}}{{{a}}}\\sin({a}x) + C$"]
        sol = f"令 $u=x, dv=\\cos({a}x)dx \\implies du=dx, v=\\frac{{1}}{{{a}}}\\sin({a}x)$。故分部積分得 $\\frac{{x}}{{{a}}}\\sin({a}x) - \\int \\frac{{1}}{{{a}}}\\sin({a}x) dx = \\frac{{x}}{{{a}}}\\sin({a}x) + \\frac{{1}}{{{a*a}}}\\cos({a}x) + C$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求 $\\int_1^2 {c}x \\ln x dx$ 的定積分之精確值。"
    sol = f"分部積分：令 $u=\\ln x, dv={c}x dx \\implies du=\\frac{{1}}{{x}}dx, v=\\frac{{{c}}}{{2}}x^2$。積分為 $[\\frac{{{c}}}{{2}}x^2 \\ln x]_1^2 - \\int_1^2 \\frac{{{c}}}{{2}}x dx = 2{c}\\ln 2 - [\\frac{{{c}}}{{4}}x^2]_1^2 = 2{c}\\ln 2 - \\frac{{3{c}}}{{4}}$。結果為 {round(2*c*0.6931 - 0.75*c, 2)}。"
    ans_val = round(2 * c * 0.6931 - 0.75 * c, 2)
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.2: Trigonometric Integrals
sec2_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用三角函數積分法，求 $\\int \\sin^2({a}x) dx$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{x}}{{2}} - \\frac{{\\sin({a*2}x)}}{{{a*4}}} + C$", f"$\\frac{{x}}{{2}} + \\frac{{\\sin({a*2}x)}}{{{a*4}}} + C$", f"$\\frac{{\\sin^3({a}x)}}{{3}} + C$", f"$\\frac{{\\cos^2({a}x)}}{{2}} + C$"]
        sol = f"利用半角公式 $\\sin^2({a}x) = \\frac{{1 - \\cos({a*2}x)}}{{2}}$。故積分為 $\\frac{{x}}{{2}} - \\frac{{\\sin({a*2}x)}}{{{a*4}}} + C$。"
    else:
        text = f"求 $\\int \\sin^3(x) \\cos^{{{a}}}(x) dx$ 的結果。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{\\cos^{{{a+3}}}(x)}}{{{a+3}}} - \\frac{{\\cos^{{{a+1}}}(x)}}{{{a+1}}} + C$", f"$\\frac{{\\cos^{{{a+1}}}(x)}}{{{a+1}}} - \\frac{{\\cos^{{{a+3}}}(x)}}{{{a+3}}} + C$", f"$\\frac{{\\sin^4(x)}}{{4}} + C$", f"$\\frac{{\\cos^2(x)}}{{2}} + C$"]
        sol = f"令 $u=\\cos x, du=-\\sin x dx$。積分為 $\\int (1 - u^2) u^{{{a}}} (-du) = \\int (u^{{{a+2}}} - u^{{{a}}}) du = \\frac{{u^{{{a+3}}}}}{{{a+3}}} - \\frac{{u^{{{a+1}}}}}{{{a+1}}} + C$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求 $\\int_0^\\pi {c} \\sin^2 x dx$ 的定積分之精確值（以 $\\pi$ 的倍數表示）。"
    sol = f"積分為 $\\int_0^\\pi \\frac{{{c}}}{{2}}(1 - \\cos 2x) dx = [\\frac{{{c}}}{{2}}x - \\frac{{{c}}}{{4}}\\sin 2x]_0^\\pi = \\frac{{{c}\\pi}}{{2}}$。結果為 {round(c/2, 2)}。"
    ans_val = round(c / 2, 2)
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.3: Trigonometric Substitution
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用三角代換法，計算 $\\int \\frac{{1}}{{\\sqrt{{{a*a} - x^2}}}} dx$ 的最一般不定積分。"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"$\\sin^{{-1}}\\left(\\frac{{x}}{{{a}}}\\right) + C$", f"$\\tan^{{-1}}\\left(\\frac{{x}}{{{a}}}\\right) + C$", f"$\\frac{{1}}{{{a}}}\\sin^{{-1}}\\left(\\frac{{x}}{{{a}}}\\right) + C$", f"$\\sin^{{-1}}(x) + C$"]
        sol = f"令 $x = {a}\\sin\\theta \\implies dx = {a}\\cos\\theta d\\theta$。積分為 $\\int \\frac{{{a}\\cos\\theta}}{{{a}\\cos\\theta}} d\\theta = \\int d\\theta = \\theta + C = \\sin^{{-1}}\\left(\\frac{{x}}{{{a}}}\\right) + C$。"
    else:
        text = f"利用三角代換法，對於 $\\int \\frac{{1}}{{x^2 \\sqrt{{x^2 + {a*a}}}}} dx$，應該進行何種代換？"
        ans = "B" if i % 4 == 1 else "D"
        opts = [f"$x = {a}\\tan\\theta$", f"$x = {a}\\sin\\theta$", f"$x = {a}\\sec\\theta$", f"$x = {a}\\cos\\theta$"]
        sol = f"根據恆等式 $1 + \\tan^2\\theta = \\sec^2\\theta$，遇到 $x^2 + a^2$ 的根號形式應令 $x = a\\tan\\theta$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"利用三角代換法，求 $\\int_0^{c} \\frac{{1}}{{\\sqrt{{{c*c} - x^2}}}} dx$ 的定積分之精確值（以 $\\pi$ 的倍數表示）。"
    sol = f"利用代換 $x = {c}\\sin\\theta$，定積分為 $[\\sin^{{-1}}(\\frac{{x}}{{{c}}})]_0^{c} = \\sin^{{-1}}(1) - \\sin^{{-1}}(0) = \\frac{{\\pi}}{{2}} = 0.5\\pi$。"
    ans_val = 0.5
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.4: Integration of Rational Functions by Partial Fractions
sec4_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用部分分式法（Partial Fractions），求 $\\int \\frac{{1}}{{x(x + {a})}} dx$ 的最一般不定積分。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{1}}{{{a}}}(\\ln|x| - \\ln|x + {a}|) + C$", f"$\\ln|x| - \\ln|x + {a}| + C$", f"$\\frac{{1}}{{{a}}}(\\ln|x| + \\ln|x + {a}|) + C$", f"$\\ln|\\frac{{x + {a}}}{{x}}| + C$"]
        sol = "展開為：$\\frac{1}{x(x + " + str(a) + ")} = \\frac{1}{" + str(a) + "x} - \\frac{1}{" + str(a) + "(x + " + str(a) + ")}$。故積分為 $\\frac{1}{" + str(a) + "}\\ln|x| - \\frac{1}{" + str(a) + "}\\ln|x + " + str(a) + "| + C$。"
    else:
        text = f"求 $\\int \\frac{{2x + {a}}}{{x^2 + {a}x}} dx$ 的最一般不定積分。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\ln|x^2 + {a}x| + C$", f"$\\frac{{1}}{{{a}}}\\ln|x^2 + {a}x| + C$", f"$2\\ln|x| + C$", f"$\\ln|x + {a}| + C$"]
        sol = f"令 $u = x^2 + {a}x \\implies du = (2x + {a})dx$。故積分為 $\\int \\frac{{1}}{{u}} du = \\ln|u| + C = \\ln|x^2 + {a}x| + C$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"利用部分分式法將 $\\frac{{1}}{{x^2 - {c*c}}}$ 拆解為 $\\frac{{A}}{{x - {c}}} + \\frac{{B}}{{x + {c}}}$，求 $A$ 之值。"
    sol = f"設 $\\frac{{1}}{{x^2 - {c*c}}} = \\frac{{A}}{{x - {c}}} + \\frac{{B}}{{x + {c}}} \\implies A(x + {c}) + B(x - {c}) = 1$。令 $x={c} \\implies 2{c}A = 1 \\implies A = \\frac{{1}}{{2{c}}}$。結果為 {round(1/(2*c), 3)}。"
    ans_val = round(1 / (2 * c), 3)
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.5: Strategy for Integration
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"在求不定積分時，最先應考慮的策略為何？"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"簡化被積函數與基本公式代換", f"分部積分法", f"三角代換法", f"部分分式法"]
        sol = f"在進階技巧之前，應先檢查是否能直接化簡或套用基本公式。"
    else:
        text = f"對於 $\\int \\frac{{\\ln x}}{{x}} dx$，最適合的積分策略為何？"
        ans = "B" if i % 4 == 1 else "D"
        opts = [f"變數變換（令 $u = \\ln x$）", f"分部積分法", f"三角代換法", f"查表法"]
        sol = f"令 $u = \\ln x \\implies du = \\frac{{1}}{{x}} dx$，積分直接轉換成 $\\int u du$，因此最合適的是變數代換法。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求 $\\int_1^e \\frac{{\\ln x}}{{x}} dx$ 的精確值。"
    sol = f"變數變換：令 $u=\\ln x$。定積分為 $[\\frac{{u^2}}{{2}}]_0^1 = \\frac{{1}}{{2}} = 0.5$。"
    ans_val = 0.5
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.6: Integration Using Tables and Technology
sec6_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"使用積分表（Integration Tables）查出 $\\int \\frac{{1}}{{x^2 - {a*a}}} dx$ 的一般形式。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{1}}{{{a*2}}}\\ln|\\frac{{x - {a}}}{{x + {a}}}| + C$", f"$\\frac{{1}}{{{a}}}\\ln|\\frac{{x - {a}}}{{x + {a}}}| + C$", f"$\\sin^{{-1}}\\left(\\frac{{x}}{{{a}}}\\right) + C$", f"$\\tan^{{-1}}(x) + C$"]
        sol = f"對應積分表公式：$\\int \\frac{{1}}{{x^2 - a^2}} dx = \\frac{{1}}{{2a}}\\ln|\\frac{{x - a}}{{x + a}}| + C$。"
    else:
        text = f"使用科技工具處理複雜積分時，電腦代數系統（CAS）通常使用哪種基本算法？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"里斯算法（Risch Algorithm）", f"牛頓法", f"辛普森法", f"歐拉法"]
        sol = f"里斯算法是一套用於決定不定積分是否可用初等函數表示的決定性演算法。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"當使用里斯算法判斷 $\\int e^{{x^2}} dx$ 是否可用初等函數表示時，其答案為初等函數（填1）或非初等函數（填0）？"
    sol = f"$\\int e^{{x^2}} dx$ 屬於非初等積分，無法用初等函數表示。故答案為 0。"
    ans_val = 0
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.7: Approximate Integration
sec7_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"在近似積分法中，使用梯形法（Trapezoidal Rule）估計 $\\int_a^b f(x) dx$，每一項的權重係數除了端點外為何？"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"$2$", f"$4$", f"$1$", f"$3$"]
        sol = f"梯形法公式為 $T_n = \\frac{{\\Delta x}}{{2}} [f(x_0) + 2f(x_1) + 2f(x_2) + \\dots + f(x_n)]$，中間權重皆為 2。"
    else:
        text = f"辛普森法（Simpson's Rule）要求區間個數 $n$ 必須滿足什麼條件？"
        ans = "B" if i % 4 == 1 else "D"
        opts = [f"必須為偶數", f"必須為奇數", f"可以為任意整數", f"必須是 3 的倍數"]
        sol = f"辛普森法（1/3法）推導基於二次拋物線，要求子區間個數 $n$ 必須為偶數。"
    sec7_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec7_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"利用梯形法，將區間 $[0, 2]$ 分為 $n=2$ 等分，求 $\\int_0^2 {c}x dx$ 的近似值（精確值）。"
    sol = f"梯形寬 $\\Delta x = 1$。$x_0=0, x_1=1, x_2=2$。$T_2 = \\frac{{1}}{{2}} [{c}(0) + 2({c}\\cdot 1) + {c}\\cdot 2] = \\frac{{1}}{{2}} [2{c} + 2{c}] = 2{c}$。"
    ans_val = c * 2
    sec7_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 7.8: Improper Integrals
sec8_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求瑕積分（Improper Integral） $\\int_1^\\infty \\frac{{1}}{{x^{a}}} dx$ 的斂散性。"
        ans = "B" if i % 4 == 0 else "C"
        opts = [f"收斂", f"發散", f"不確定", f"無解"]
        sol = f"根據 $p$-級數積分判別法：在 $[1, \\infty)$，$\\int_1^\\infty \\frac{{1}}{{x^p}} dx$ 在 $p = {a} > 1$ 時收斂。"
    else:
        text = f"求瑕積分 $\\int_1^\\infty \\frac{{1}}{{x}} dx$ 的斂散性。"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"發散", f"收斂", f"振盪散開", f"極限為 1"]
        sol = f"$\\lim_{{t \\to \\infty}} [\\ln x]_1^t = \\lim_{{t \\to \\infty}} \\ln t = \\infty$，故發散。"
    sec8_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec8_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求瑕積分 $\\int_1^\\infty \\frac{{{c}}}{{x^2}} dx$ 之精確收斂值。"
    sol = f"積分為 $\\lim_{{t \\to \\infty}} [- \\frac{{{c}}}{{x}}]_1^t = \\lim_{{t \\to \\infty}} (- \\frac{{{c}}}{{t}} + {c}) = {c}$。"
    ans_val = c
    sec8_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_7")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch7_sec1.md").write_text(generate_section(7, 1, "分部積分法", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch7_sec2.md").write_text(generate_section(7, 2, "三角積分", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch7_sec3.md").write_text(generate_section(7, 3, "三角代換法", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch7_sec4.md").write_text(generate_section(7, 4, "部分分式法求有理函數積分", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch7_sec5.md").write_text(generate_section(7, 5, "積分策略", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch7_sec6.md").write_text(generate_section(7, 6, "查表與科技工具積分", sec6_choices, sec6_fills), encoding='utf-8')
    (out_dir / "ch7_sec7.md").write_text(generate_section(7, 7, "近似積分", sec7_choices, sec7_fills), encoding='utf-8')
    (out_dir / "ch7_sec8.md").write_text(generate_section(7, 8, "瑕積分", sec8_choices, sec8_fills), encoding='utf-8')
    
    print("Chapter 7 sections generated successfully.")
