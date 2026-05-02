import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 6.{sec_id} 節：{title}",
        "",
        f"本節收錄 6.{sec_id} 節相關題目。",
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


# 6.1: Inverse Functions and Their Derivatives
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"已知函數 $f(x) = x^3 + x + {a}$ 為一對一函數，求其反函數在 $x={a}$ 的導數值 $(f^{{-1}})'({a})$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = ["$1$", f"${a}$", f"$\\frac{{1}}{{{a}}}$", f"$0$"]
        sol = f"解 $f(x)={a} \\implies x^3+x+{a}={a} \\implies x=0$。由反函數求導公式 $(f^{{-1}})'({a}) = \\frac{{1}}{{f'(0)}}$。而 $f'(x)=3x^2+1 \\implies f'(0)=1$。故值為 $1$。"
    else:
        text = f"若 $f(x) = {a}x + 3$，求 $f^{{-1}}(x)$ 之表示式。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{x - 3}}{{{a}}}$", f"$\\frac{{x + 3}}{{{a}}}$", f"${a}x - 3$", f"$\\frac{{{a}}}{{x-3}}$"]
        sol = f"令 $y = {a}x + 3 \\implies x = \\frac{{y - 3}}{{{a}}}$。故反函數為 $f^{{-1}}(x) = \\frac{{x - 3}}{{{a}}}$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"若一對一函數滿足 $f(1) = 2$ 且 $f'(1) = {c}$，求 $(f^{{-1}})'(2)$ 之值。"
    sol = f"由反函數求導：$(f^{{-1}})'(2) = \\frac{{1}}{{f'(1)}} = \\frac{{1}}{{{c}}}$。結果為 {round(1/c, 2)}。"
    ans_val = round(1 / c, 2)
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.2: Exponential Functions and Their Derivatives
sec2_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求函數 $f(x) = e^{{{a}x}}$ 的一階導數 $f'(x)$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a}e^{{{a}x}}$", f"$e^{{{a}x}}$", f"$\\frac{{1}}{{{a}}}e^{{{a}x}}$", f"${a*2}e^{{{a}x}}$"]
        sol = f"利用鏈鎖律，$\\frac{{d}}{{dx}} e^{{{a}x}} = {a}e^{{{a}x}}$。"
    else:
        text = f"求 $\\int e^{{{a}x}} dx$ 的最一般不定積分。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{1}}{{{a}}}e^{{{a}x}} + C$", f"${a}e^{{{a}x}} + C$", f"$e^{{{a}x}} + C$", f"$-\\frac{{1}}{{{a}}}e^{{{a}x}} + C$"]
        sol = f"對指數項積分，並考量鏈鎖律之係數，$\\int e^{{{a}x}} dx = \\frac{{1}}{{{a}}}e^{{{a}x}} + C$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 19
    text = f"求 $\\int_0^1 e^{{{c}x}} dx$ 的定積分精確值。"
    sol = f"積分為 $[\\frac{{1}}{{{c}}} e^{{{c}x}}]_0^1 = \\frac{{e^{c} - 1}}{{{c}}}$。當 $c={c} \\implies \\frac{{e^{c}-1}}{{{c}}} = {round((2.71828**c - 1)/c, 2)}$。"
    ans_val = round((2.71828**c - 1)/c, 2)
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.3: Logarithmic Functions
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求對數方程式 $\\ln(x + {a}) = 1$ 的解。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$e - {a}$", f"$e + {a}$", f"$e^{a}$", f"$1 - {a}$"]
        sol = f"將對數形式轉換為指數形式：$x + {a} = e^1 \\implies x = e - {a}$。"
    else:
        text = f"化簡 $\\ln({a}e)$ 的值。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\ln {a} + 1$", f"$\\ln {a}$", f"$1$", f"${a}$"]
        sol = f"利用對數律：$\\ln({a}e) = \\ln {a} + \\ln e = \\ln {a} + 1$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求方程式 $\\ln(x) + \\ln(2) = \\ln({c})$ 中 $x$ 的解。"
    sol = f"利用對數律 $\\ln(2x) = \\ln({c}) \\implies 2x = {c} \\implies x = \\frac{{{c}}}{{2}}$。結果為 {round(c/2, 2)}。"
    ans_val = round(c / 2, 2)
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.4: Derivatives of Logarithmic Functions
sec4_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求函數 $y = \\ln({a}x^2)$ 的一階導數 $\\frac{{dy}}{{dx}}$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{2}}{{x}}$", f"$\\frac{{{a}}}{{x}}$", f"$\\frac{{1}}{{{a}x}}$", f"$\\frac{{2}}{{{a}x}}$"]
        sol = f"利用鏈鎖律：$\\frac{{d}}{{dx}} \\ln({a}x^2) = \\frac{{1}}{{{a}x^2}} \\cdot (2{a}x) = \\frac{{2a x}}{{a x^2}} = \\frac{{2}}{{x}}$。"
    else:
        text = f"求函數 $y = x \\ln x - {a}x$ 的導數。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\ln x - {a-1}$", f"$\\ln x - {a+1}$", f"$\\ln x - {a}$", f"$\\frac{{1}}{{x}}$"]
        sol = f"利用乘積律對第一項求導：$\\frac{{d}}{{dx}} (x \\ln x) = 1 \\cdot \\ln x + x \\cdot \\frac{{1}}{{x}} = \\ln x + 1$。對第二項求導：$-{a}$。合併得 $\\ln x + 1 - {a} = \\ln x - {a-1}$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 17
    text = f"求 $\\int_1^2 \\frac{{{c}}}{{x}} dx$ 的定積分精確值。"
    sol = f"積分為 $[{c} \\ln x]_1^2 = {c}(\\ln 2 - \\ln 1) = {c} \\ln 2$。當 $c={c} \\implies {c} \\times 0.6931 = {round(c*0.6931, 2)}$。"
    ans_val = round(c * 0.6931, 2)
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.2*: The Natural Logarithmic Function
sec2_star_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"從積分角度出發，自然對數定義為 $\\ln x = \\int_1^x \\frac{{1}}{{t}} dt$。求 $\\ln(1)$ 之值。"
        ans = "B" if i % 4 == 0 else "C"
        opts = [f"$1$", f"$0$", f"$e$", f"$-1$"]
        sol = f"由定義可知，$\\int_1^1 \\frac{{1}}{{t}} dt = 0$。"
    else:
        text = f"若 $f(x) = \\ln(\\sqrt{{x^{a} + 1}})$，求 $f'(x)$。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{{a}x^{a-1}}}{{2(x^{a} + 1)}}$", f"$\\frac{{x^{a}}}{{x^{a} + 1}}$", f"$\\frac{{{a}}}{{x}}$", f"$\\frac{{1}}{{2(x^{a} + 1)}}$"]
        sol = f"將對數式化簡：$f(x) = \\frac{{1}}{{2}} \\ln(x^{a} + 1)$。求導得 $f'(x) = \\frac{{1}}{{2}} \\cdot \\frac{{1}}{{x^{a} + 1}} \\cdot {a}x^{a-1} = \\frac{{{a}x^{a-1}}}{{2(x^{a} + 1)}}$。"
    sec2_star_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_star_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求函數 $f(x) = \\ln({c}x)$ 在 $x=3$ 的切線斜率。"
    sol = f"求導：$f'(x) = \\frac{{1}}{{x}}$。代入 $x=3 \\implies \\frac{{1}}{{3}} = {round(1/3, 2)}$。"
    ans_val = round(1 / 3, 2)
    sec2_star_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.3*: The Natural Exponential Function
sec3_star_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"設自然對數之反函數為自然指數函數 $\\exp(x) = e^x$。求 $\\lim_{{x \\to 0}} \\frac{{e^{{{a}x}} - 1}}{{x}}$。"
        ans = "D" if i % 4 == 0 else "C"
        opts = [f"${a}$", f"$1$", f"$0$", f"$e$"]
        sol = f"利用洛必達法則或導數定義，$\\lim_{{x \\to 0}} \\frac{{e^{{{a}x}} - 1}}{{x}} = \\frac{{d}}{{dx}}[e^{{{a}x}}]|_{{x=0}} = {a} e^{{0}} = {a}$。"
    else:
        text = f"求 $\\int e^{{x + {a}}} dx$ 的結果。"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"$e^{{x + {a}}} + C$", f"$e^x + C$", f"$\\frac{{1}}{{{a}}}e^{{x + {a}}} + C$", f"$x e^{{x + {a}}} + C$"]
        sol = f"利用代換法或直接對常數項積分：$\\int e^{{x + {a}}} dx = e^{{x + {a}}} + C$。"
    sec3_star_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_star_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求方程式 $e^{{{c}x}} = 1$ 的實數解。"
    sol = f"兩邊取 $\\ln \\implies {c}x = \\ln 1 = 0 \\implies x = 0$。"
    ans_val = 0
    sec3_star_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.4*: General Logarithmic and Exponential Functions
sec4_star_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求指數函數 $f(x) = {a}^x$ 的導數 $f'(x)$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a}^x \\ln {a}$", f"${a}^x$", f"$\\frac{{{a}^x}}{{\\ln {a}}}$", f"$x {a}^{{x-1}}$"]
        sol = f"一般指數函數求導公式為 $\\frac{{d}}{{dx}} a^x = a^x \\ln a$。"
    else:
        text = f"求對數函數 $f(x) = \\log_{{{a}}} x$ 的一階導數 $f'(x)$。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{1}}{{x \\ln {a}}}$", f"$\\frac{{\\ln {a}}}{{x}}$", f"$\\frac{{1}}{{x}}$", f"$\\frac{{x}}{{\\ln {a}}}$"]
        sol = f"由換底公式 $\\log_a x = \\frac{{\\ln x}}{{\\ln a}}$，求導得 $\\frac{{1}}{{x \\ln a}}$。"
    sec4_star_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_star_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求 $\\int 2^x \\ln(2) dx$ 的最一般不定積分之係數（$C$ 以外部分在 $x=0$ 的值）。"
    sol = f"積分為 $\\int 2^x \\ln 2 dx = 2^x + C$。當 $x=0$ 時其值為 $2^0 = 1$。"
    ans_val = 1
    sec4_star_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.5: Exponential Growth and Decay
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"某群體數量 $P(t)$ 滿足微分方程 $\\frac{{dP}}{{dt}} = {a}P$。若 $P(0) = 100$，求 $P(t)$ 之表示式。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$100e^{{{a}t}}$", f"$100e^t$", f"${a}e^{{100t}}$", f"$100t$"]
        sol = f"該方程為標準的指數成長模型，解為 $P(t) = P(0)e^{{kt}} = 100e^{{{a}t}}$。"
    else:
        text = f"某放射性物質半衰期為 $T$，若滿足 $\\frac{{dy}}{{dt}} = -ky$，則衰變常數 $k$ 為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{\\ln 2}}{{T}}$", f"$\\frac{{1}}{{T}}$", f"$\\frac{{T}}{{\\ln 2}}$", f"$\\ln 2$" ]
        sol = f"半衰期公式：$y(T) = y_0 e^{{-kT}} = \\frac{{1}}{{2}} y_0 \\implies -kT = \\ln(\\frac{{1}}{{2}}) = -\\ln 2 \\implies k = \\frac{{\\ln 2}}{{T}}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"某物質以指數衰變，初量為 100，在 $t=1$ 時量為 $100e^{{-{c}}}$。求 $t=2$ 時該物質的量（除以 100 的倍數，取至小數點後兩位）。"
    sol = f"方程式為 $y(t) = 100e^{{-{c}t}}$。當 $t=2 \\implies 100e^{{-{c*2}}}$。除以 100 為 $e^{{-{c*2}}} = {round(2.71828**(-2*c), 4)}$。"
    ans_val = round(2.71828 ** (-2 * c), 4)
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.6: Inverse Trigonometric Functions
sec6_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求反三角函數 $y = \\tan^{{-1}}(x)$ 的一階導數 $\\frac{{dy}}{{dx}}$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{1}}{{1 + x^2}}$", f"$\\frac{{1}}{{\\sqrt{{1 - x^2}}}}$", f"$\\frac{{1}}{{x^2 - 1}}$", f"$\\frac{{1}}{{1 - x^2}}$"]
        sol = f"反正切函數的導數公式為 $\\frac{{d}}{{dx}} \\tan^{{-1}} x = \\frac{{1}}{{1 + x^2}}$。"
    else:
        text = f"求 $\\int \\frac{{1}}{{1 + x^2}} dx$ 的最一般不定積分。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\tan^{{-1}} x + C$", f"$\\sin^{{-1}} x + C$", f"$\\cos^{{-1}} x + C$", f"$\\sec^{{-1}} x + C$"]
        sol = f"對反三角函數求導公式反向積分：$\\int \\frac{{1}}{{1 + x^2}} dx = \\tan^{{-1}} x + C$。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 19
    text = f"求 $\\tan^{{-1}}(1)$ 之精確值（以 $\\pi$ 表示，如 $\\pi/4$ 為 0.25）。"
    sol = f"已知 $\\tan(\\pi/4) = 1 \\implies \\tan^{{-1}}(1) = \\pi/4 = 0.25$。"
    ans_val = 0.25
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.7: Hyperbolic Functions
sec7_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求雙曲正弦函數 $\\sinh(x)$ 的一階導數 $\\frac{{d}}{{dx}} \\sinh(x)$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\cosh(x)$", f"$-\\cosh(x)$", f"$\\sinh(x)$", f"$0$"]
        sol = f"由雙曲函數定義：$\\frac{{d}}{{dx}} \\sinh x = \\cosh x$。"
    else:
        text = f"求雙曲函數恆等式：$\\cosh^2(x) - \\sinh^2(x)$ 的值。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$1$", f"$-1$", f"$0$", f"$\\cosh(2x)$"]
        sol = f"由定義可知，$\\cosh^2 x - \\sinh^2 x = 1$ 恆成立。"
    sec7_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec7_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"計算 $\\cosh(0)$ 的值。"
    sol = f"雙曲餘弦定義：$\\cosh(0) = \\frac{{e^0 + e^{{-0}}}}{{2}} = \\frac{{1 + 1}}{{2}} = 1$。"
    ans_val = 1
    sec7_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 6.8: Indeterminate Forms and l'Hospital's Rule
sec8_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用洛必達法則（l'Hospital's Rule）求極限 $\\lim_{{x \\to 0}} \\frac{{\\sin({a}x)}}{{x}}$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a}$", f"$1$", f"$0$", f"$\\infty$"]
        sol = f"此極限為 $\\frac{{0}}{{0}}$ 型。求導：$\\lim_{{x \\to 0}} \\frac{{{a}\\cos({a}x)}}{{1}} = {a}\\cos(0) = {a}$。"
    else:
        text = f"利用洛必達法則求極限 $\\lim_{{x \\to 0}} \\frac{{e^{{{a}x}} - 1}}{{x}}$。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a}$", f"$1$", f"$0$", f"$e$"]
        sol = f"此為 $\\frac{{0}}{{0}}$ 型。分子分母求導：$\\lim_{{x \\to 0}} \\frac{{{a}e^{{{a}x}}}}{{1}} = {a}e^0 = {a}$。"
    sec8_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec8_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"利用洛必達法則求 $\\lim_{{x \\to 0}} \\frac{{{c}x}}{{e^x - 1}}$ 的精確值。"
    sol = f"此為 $\\frac{{0}}{{0}}$ 型。求導：$\\lim_{{x \\to 0}} \\frac{{{c}}}{{e^x}} = \\frac{{{c}}}{{1}} = {c}$。"
    ans_val = c
    sec8_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_6")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch6_sec1.md").write_text(generate_section(6, 1, "反函數與其導數", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch6_sec2.md").write_text(generate_section(6, 2, "指數函數與其導數", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch6_sec3.md").write_text(generate_section(6, 3, "對數函數", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch6_sec4.md").write_text(generate_section(6, 4, "對數函數的導數", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch6_sec2_star.md").write_text(generate_section(6, "2_star", "自然對數函數", sec2_star_choices, sec2_star_fills), encoding='utf-8')
    (out_dir / "ch6_sec3_star.md").write_text(generate_section(6, "3_star", "自然指數函數", sec3_star_choices, sec3_star_fills), encoding='utf-8')
    (out_dir / "ch6_sec4_star.md").write_text(generate_section(6, "4_star", "一般對數與指數函數", sec4_star_choices, sec4_star_fills), encoding='utf-8')
    (out_dir / "ch6_sec5.md").write_text(generate_section(6, 5, "指數增長與衰退", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch6_sec6.md").write_text(generate_section(6, 6, "反三角函數", sec6_choices, sec6_fills), encoding='utf-8')
    (out_dir / "ch6_sec7.md").write_text(generate_section(6, 7, "雙曲函數", sec7_choices, sec7_fills), encoding='utf-8')
    (out_dir / "ch6_sec8.md").write_text(generate_section(6, 8, "不定型與洛必達法則", sec8_choices, sec8_fills), encoding='utf-8')
    
    print("Chapter 6 sections generated successfully.")
