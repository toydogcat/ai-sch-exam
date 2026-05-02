import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 2.{sec_id} 節：{title}",
        "",
        f"本節收錄 2.{sec_id} 節相關題目。",
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


# 2.1: Derivatives and Rates of Change
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"已知一曲線方程式為 $y = {a}x^2$，試問其在 $x=1$ 處的切線斜率為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a*2}$", f"${a}$", f"$2$", f"${a*3}$"]
        sol = f"利用導數定義或微分：$y' = 2 \\cdot {a}x = {a*2}x$。代入 $x=1$ 得 ${a*2}$。"
    else:
        text = f"若函數 $f(t) = t^2 + {a}t$，試問其在 $t=2$ 時之瞬時變化率為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a+4}$", f"${a+2}$", f"${a}$", f"$4$"]
        sol = f"$f'(t) = 2t + {a}$。代入 $t=2$ 得 $2(2) + {a} = {a+4}$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求 $f(x) = {c}x^2$ 在 $x=3$ 處之切線斜率。"
    sol = f"對 $x$ 微分得 $f'(x) = {c*2}x$。代入 $x=3 \\implies {c*2} \\times 3 = {c*6}$。"
    ans_val = c * 6
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.2: The Derivative as a Function
sec2_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求函數 $f(x) = x^{a}$ 的導函數 $f'(x)$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a}x^{a-1}$", f"$x^{a}$", f"${a-1}x^{a}$", f"$\\{a}x^{a-1}$"]
        sol = f"由冪函數微分法可知 $\\frac{{d}}{{dx}} (x^n) = nx^{{n-1}}$。故為 ${a}x^{a-1}$。"
    else:
        text = f"設導函數 $f'(x) = {a}x$，試問其導函數的定義域為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\mathbb{{R}}$", f"$(0, \\infty)$", f"$[0, \\infty)$", f"$(-\\infty, 0)$"]
        sol = f"因為 $f'(x) = {a}x$ 是多項式函數，在所有實數上均有定義。故其定義域為 $\\mathbb{{R}}$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 19
    text = f"若函數 $f(x) = {c}x^2$，求導函數 $f'(x)$ 在 $x=5$ 的值。"
    sol = f"導函數為 $f'(x) = {c*2}x$。代入 $x=5 \\implies {c*2} \\times 5 = {c*10}$。"
    ans_val = c * 10
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.3: Differentiation Formulas
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用微分公式計算 $\\frac{{d}}{{dx}} ({a}x^3 + 5x)$ 的結果。"
        ans = "D" if i % 4 == 0 else "C"
        opts = [f"${a*3}x^2 + 5$", f"${a}x^2 + 5$", f"${a*3}x^2$", f"${a*3}x + 5$"]
        sol = f"對各項微分得 ${a*3}x^2 + 5$。"
    else:
        text = f"求函數 $f(x) = ({a}x+1)(x+2)$ 的導函數 $f'(x)$。"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"${a*2}x + {a*2+1}$", f"${a}x + {a+1}$", f"${a}x^2 + 1$", f"$x + {a}$"]
        sol = f"展開得 $f(x) = {a}x^2 + {a*2+1}x + 2$，故微分為 ${a*2}x + {a*2+1}$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求 $f(x) = {c}x^3 + x^2$ 的導函數在 $x=1$ 的值。"
    sol = f"導函數為 $f'(x) = {c*3}x^2 + 2x$。代入 $x=1$ 得 ${c*3}(1) + 2(1) = {c*3+2}$。"
    ans_val = c * 3 + 2
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.4: Derivatives of Trigonometric Functions
sec4_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求 $\\frac{{d}}{{dx}} ({a}\\sin x + \\cos x)$ 的導函數。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a}\\cos x - \\sin x$", f"${a}\\cos x + \\sin x$", f"$-{a}\\cos x - \\sin x$", f"${a}\\sin x$"]
        sol = f"由於 $(\\sin x)' = \\cos x$ 且 $(\\cos x)' = -\\sin x$，故結果為 ${a}\\cos x - \\sin x$。"
    else:
        text = f"求函數 $y = \\tan x$ 的導函數為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\sec^2 x$", f"$\\csc^2 x$", f"$\\sec x \\tan x$", f"$\\cos^2 x$"]
        sol = f"由三角微分公式，$(\\tan x)' = \\sec^2 x$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 15
    text = f"已知 $f(x) = {c}\\sin x + 2\\cos x$，求 $f'(0)$ 的精確值。"
    sol = f"導函數為 $f'(x) = {c}\\cos x - 2\\sin x$。代入 $x=0 \\implies {c}\\cos 0 - 2\\sin 0 = {c}$。"
    ans_val = c
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.5: The Chain Rule
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用連鎖律計算 $\\frac{{d}}{{dx}} (x^2 + 1)^{a}$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a*2}x(x^2 + 1)^{a-1}$", f"${a}x(x^2 + 1)^{a-1}$", f"${a*2}(x^2 + 1)^{a}$", f"$2x(x^2 + 1)^{a-1}$"]
        sol = f"外層函數微分為 ${a}(x^2+1)^{a-1}$，內層函數 $x^2+1$ 微分為 $2x$。故為 ${a*2}x(x^2+1)^{a-1}$。"
    else:
        text = f"求 $\\frac{{d}}{{dx}} (\\sin({a}x))$ 的結果。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a}\\cos({a}x)$", f"$\\cos({a}x)$", f"$-{a}\\cos({a}x)$", f"${a}\\sin({a}x)$"]
        sol = f"外層 $(\\sin u)' = \\cos u$，內層 $({a}x)' = {a}$。故為 ${a}\\cos({a}x)$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求導函數 $f(x) = (2x+1)^{c}$ 在 $x=0$ 處的值。"
    sol = f"導函數為 $f'(x) = {c} \\cdot (2x+1)^{c-1} \\cdot 2 = {c*2}(2x+1)^{c-1}$。代入 $x=0 \\implies {c*2}(1)^{c-1} = {c*2}$。"
    ans_val = c * 2
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.6: Implicit Differentiation
sec6_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"若 $x^2 + y^2 = {a*a}$，試求其隱函數導函數 $\\frac{{dy}}{{dx}}$。"
        ans = "B" if i % 4 == 0 else "C"
        opts = [f"$-\\frac{{x}}{{y}}$", f"$\\frac{{x}}{{y}}$", f"$-\\frac{{y}}{{x}}$", f"$\\frac{{y}}{{x}}$"]
        sol = f"兩邊對 $x$ 微分：$2x + 2y \\frac{{dy}}{{dx}} = 0 \\implies \\frac{{dy}}{{dx}} = -\\frac{{x}}{{y}}$。"
    else:
        text = f"若 $x^2 + {a}y^3 = 10$，試求 $\\frac{{dy}}{{dx}}$ 的結果為何？"
        ans = "D" if i % 4 == 1 else "A"
        opts = [f"$-\\frac{{2x}}{{{a*3}y^2}}$", f"$\\frac{{2x}}{{{a*3}y^2}}$", f"$-\\frac{{2x}}{{y}}$", f"$-\\frac{{x}}{{y}}$"]
        sol = f"兩邊對 $x$ 微分得 $2x + {a*3}y^2 \\frac{{dy}}{{dx}} = 0 \\implies \\frac{{dy}}{{dx}} = -\\frac{{2x}}{{{a*3}y^2}}$。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 16
    text = f"已知曲線方程式為 $x^2 + y^2 = {c*c}$，求在 $(0, {c})$ 處切線的斜率為多少？"
    sol = f"隱函數微分得 $\\frac{{dy}}{{dx}} = -\\frac{{x}}{{y}}$。代入 $x=0, y={c} \\implies -\\frac{{0}}{{{c}}} = 0$。"
    ans_val = 0
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.7: Rates of Change in the Natural and Social Sciences
sec7_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"某物體受重力作用向下運動，其高度 $h(t) = -{a}t^2 + 100$，試問在 $t=2$ 秒時的瞬時速率為多少？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a*4}$", f"${a*2}$", f"$4$", f"$100$"]
        sol = f"速率為速度的絕對值。$v(t) = h'(t) = -{a*2}t$。在 $t=2$ 時，$|v(2)| = |-{a*4}| = {a*4}$。"
    else:
        text = f"某化學反應產生的物質量 $M(t) = {a}t^2 + t$，求當 $t=1$ 時之反應速率。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*2+1}$", f"${a}$", f"${a+1}$", f"$2$"]
        sol = f"反應速率為 $M'(t) = {a*2}t + 1$。代入 $t=1$ 得 ${a*2+1}$。"
    sec7_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec7_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"若某成本函數為 $C(x) = {c}x^2 + 30x + 100$，試求 $x=2$ 時之邊際成本。"
    sol = f"邊際成本即為 $C'(x) = {c*2}x + 30$。代入 $x=2 \\implies {c*2}(2) + 30 = {c*4+30}$。"
    ans_val = c * 4 + 30
    sec7_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.8: Related Rates
sec8_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"一個正方形的邊長以 {a} cm/s 的速率增加，試問當邊長為 10 cm 時，面積的增加速率為多少 $\\text{{cm}}^2\\text{{/s}}$？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a*20}$", f"${a*10}$", f"${a*2}$", f"$20$"]
        sol = f"正方形面積為 $A = x^2$。兩邊對 $t$ 微分：$\\frac{{dA}}{{dt}} = 2x \\frac{{dx}}{{dt}}$。代入 $x=10, \\frac{{dx}}{{dt}} = {a} \\implies 2 \\times 10 \\times {a} = {a*20}$。"
    else:
        text = f"一個圓的半徑以 {a} cm/s 的速率增加，當半徑為 2 cm 時，面積的增加速率為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*4}\\pi$", f"${a*2}\\pi$", f"${a}\\pi$", f"$4\\pi$"]
        sol = f"圓面積為 $A = \\pi r^2$。微分：$\\frac{{dA}}{{dt}} = 2\\pi r \\frac{{dr}}{{dt}}$。代入 $r=2, \\frac{{dr}}{{dt}} = {a} \\implies 2\\pi(2)({a}) = {a*4}\\pi$。"
    sec8_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec8_fills = []
for i in range(21, 31):
    c = i - 15
    text = f"一個正方形的邊長以 {c} cm/s 的速率增加，求當邊長為 5 cm 時，面積的增加速率為何？"
    sol = f"面積為 $A=x^2$，因此 $\\frac{{dA}}{{dt}} = 2x \\frac{{dx}}{{dt}}$。代入 $x=5, \\frac{{dx}}{{dt}}={c} \\implies 2(5)({c}) = {c*10}$。"
    ans_val = c * 10
    sec8_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 2.9: Linear Approximations and Differentials
sec9_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求函數 $f(x) = x^2$ 在 $a=2$ 處的線性化（Linearization）$L(x)$。"
        ans = "C" if i % 4 == 0 else "D"
        opts = [f"$4x - 4$", f"$4x$", f"$2x + 4$", f"$4x + 4$"]
        sol = f"$L(x) = f(a) + f'(a)(x-a)$。$f(2)=4, f'(2)=4 \\implies 4 + 4(x-2) = 4x - 4$。"
    else:
        text = f"已知 $y = x^3$，當 $x=2$ 且 $\\Delta x = 0.1$ 時，試問其微分 $dy$ 的值為多少？"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"$1.2$", f"$12$", f"$0.1$", f"$0.4$"]
        sol = f"$dy = f'(x)dx = 3x^2 dx$。代入 $x=2, dx=0.1 \\implies 3(2)^2(0.1) = 3(4)(0.1) = 1.2$。"
    sec9_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec9_fills = []
for i in range(21, 31):
    c = i - 16
    text = f"若函數 $f(x) = {c}x^2$ 在 $x=1$ 且 $dx=0.1$，試求 $dy$ 的精確值。"
    sol = f"微分 $dy = 2 \\cdot {c}x dx = {c*2}x dx$。代入 $x=1, dx=0.1 \\implies {c*2}(1)(0.1) = {round(c*2*0.1, 2)}$。"
    ans_val = round(c * 2 * 0.1, 2)
    sec9_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_2")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch2_sec1.md").write_text(generate_section(2, 1, "導數與變化率", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch2_sec2.md").write_text(generate_section(2, 2, "導數作為一個函數", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch2_sec3.md").write_text(generate_section(2, 3, "微分公式", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch2_sec4.md").write_text(generate_section(2, 4, "三角函數的導數", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch2_sec5.md").write_text(generate_section(2, 5, "連鎖律", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch2_sec6.md").write_text(generate_section(2, 6, "隱函數微分", sec6_choices, sec6_fills), encoding='utf-8')
    (out_dir / "ch2_sec7.md").write_text(generate_section(2, 7, "自然與社會科學中的變化率", sec7_choices, sec7_fills), encoding='utf-8')
    (out_dir / "ch2_sec8.md").write_text(generate_section(2, 8, "相關變率", sec8_choices, sec8_fills), encoding='utf-8')
    (out_dir / "ch2_sec9.md").write_text(generate_section(2, 9, "線性逼近與微分", sec9_choices, sec9_fills), encoding='utf-8')
    
    print("Chapter 2 sections generated successfully.")
