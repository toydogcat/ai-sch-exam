import os
from pathlib import Path

def generate_section(sec_id, title, choices, fills):
    lines = [
        f"# 微積分題庫 - 2.{sec_id} 節：{title}",
        "",
        f"本節收錄 2.{sec_id} 節相關題目。",
        ""
    ]
    for i, (text, ans, opts, sol) in enumerate(choices, start=1):
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        options_formatted = [f"({lbl}) {opts[idx]}" for idx, lbl in enumerate(labels)]
        
        lines.extend([
            "---", "",
            f"[q:{i}, type:single, ans:{ans}]",
            text
        ])
        lines.extend(options_formatted)
        lines.extend(["<!-- solution -->", sol, ""])
        
    for i, (text, ans_val, sol) in enumerate(fills, start=31):
        lines.extend([
            "---", "",
            f"[q:{i}, type:fill, ans:{ans_val}]",
            text,
            "<!-- solution -->",
            sol,
            ""
        ])
    return "\n".join(lines)

def generate_review(choices, fills):
    lines = [
        "# 微積分題庫 - 第二章綜合測驗 (Chapter 2 Review)",
        "",
        "本節收錄第二章所有主題的綜合題目。",
        ""
    ]
    for i, (text, ans, opts, sol) in enumerate(choices, start=1):
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        options_formatted = [f"({lbl}) {opts[idx]}" for idx, lbl in enumerate(labels)]
        
        lines.extend([
            "---", "",
            f"[q:{i}, type:single, ans:{ans}]",
            text
        ])
        lines.extend(options_formatted)
        lines.extend(["<!-- solution -->", sol, ""])
        
    for i, (text, ans_val, sol) in enumerate(fills, start=31):
        lines.extend([
            "---", "",
            f"[q:{i}, type:fill, ans:{ans_val}]",
            text,
            "<!-- solution -->",
            sol,
            ""
        ])
    return "\n".join(lines)

# Generate distinct sections
all_choices = []
all_fills = []

# Sec 2.1: 導數與變化率
sec1_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 2
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"若函數 $f(t) = t^2 + {a}t$，試問其在 $t=2$ 時之瞬時變化率為何？"
        opts = [f"${a+4}$", f"${a+2}$", f"${a}$", f"$4$"]
        sol = f"$f'(t) = 2t + {a}$。代入 $t=2$ 得 $2(2) + {a} = {a+4}$。"
    elif i <= 20:
        a = i - 5
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"已知一曲線方程式為 $y = {a}x^2$，試問其在 $x=1$ 處的切線斜率為何？"
        opts = [f"${a*2}$", f"${a}$", f"$2$", f"${a*3}$"]
        sol = f"利用導數定義：$y' = 2 \\cdot {a}x = {a*2}x$。代入 $x=1$ 得 ${a*2}$。"
    else:
        c = i - 15
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"設某物體的位置函數為 $s(t) = t^2 + {c}t$，求在時間區間 $[1, 3]$ 的平均變化率。"
        opts = [f"${4+c}$", f"${c}$", f"$4$", f"${2*c}$"]
        sol = f"平均變化率為 $\\frac{{s(3)-s(1)}}{{3-1}} = \\frac{{(9+3c) - (1+c)}}{{2}} = \\frac{{8+2c}}{{2}} = 4 + c$。"
    sec1_choices.append((text, ans, opts, sol))

sec1_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 11
        text = f"求 $f(x) = {c}x^2$ 在 $x=3$ 處之切線斜率。"
        ans_val = c * 6
        sol = f"對 $x$ 微分得 $f'(x) = {c*2}x$。代入 $x=3 \\implies {c*2} \\times 3 = {c*6}$。"
    else:
        d = i + 1
        text = f"已知一物體之位置函數為 $s(t) = {d}t^2 + 5t$，試問其在 $t=2$ 時之瞬時速度為何？"
        ans_val = d * 4 + 5
        sol = f"$v(t) = s'(t) = {d*2}t + 5$。代入 $t=2$ 得 ${d*2}(2)+5 = {d*4+5}$。"
    sec1_fills.append((text, ans_val, sol))

# Sec 2.2: 導數作為一個函數
sec2_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 2
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"求函數 $f(x) = x^{a}$ 的導函數 $f'(x)$。"
        opts = [f"${a}x^{a-1}$", f"$x^{a}$", f"${a-1}x^{a}$", f"${a+1}x^{a}$"]
        sol = f"由冪函數微分法可知 $\\frac{{d}}{{dx}} (x^n) = nx^{{n-1}}$。故為 ${a}x^{a-1}$。"
    elif i <= 20:
        c = i + 5
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"設導函數 $f'(x) = {c}x$，試問其導函數的定義域為何？"
        opts = [f"$\\mathbb{{R}}$", f"$(0, \\infty)$", f"$[0, \\infty)$", f"$(-\\infty, 0)$"]
        sol = f"因為 $f'(x) = {c}x$ 是多項式函數，在所有實數上均有定義，故定義域為 $\\mathbb{{R}}$。"
    else:
        k = i - 10
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"已知 $f(x) = x^2 - {k}x$，試問在何處此函數有水平切線？"
        opts = [f"$x = {k/2:.1f}$", f"$x = {k}$", f"$x = {k*2}$", f"$x = 0$"]
        sol = f"水平切線代表 $f'(x) = 0$。$2x - {k} = 0 \\implies x = \\frac{{{k}}}{{2}} = {k/2:.1f}$。"
    sec2_choices.append((text, ans, opts, sol))

sec2_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 11
        text = f"若函數 $f(x) = {c}x^2$，求導函數 $f'(x)$ 在 $x=5$ 的值。"
        ans_val = c * 10
        sol = f"導函數為 $f'(x) = {c*2}x$。代入 $x=5 \\implies {c*2} \\times 5 = {c*10}$。"
    else:
        d = i - 5
        text = f"已知函數 $f(x) = x^3$，其切線斜率為 {d*d*3} 的切點 $x$ 座標為正數，求該 $x$ 座標。"
        ans_val = d
        sol = f"$f'(x) = 3x^2 = {d*d*3} \\implies x^2 = {d*d} \\implies x = {d}$（取正數）。"
    sec2_fills.append((text, ans_val, sol))

# Sec 2.3: 微分公式
sec3_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 2
        ans = "D" if i % 4 == 1 else ("C" if i % 4 == 2 else ("B" if i % 4 == 3 else "A"))
        text = f"利用微分公式計算 $\\frac{{d}}{{dx}} ({a}x^3 + 5x)$ 的結果。"
        opts = [f"${a*3}x^2 + 5$", f"${a}x^2 + 5$", f"${a*3}x^2$", f"${a*3}x + 5$"]
        sol = f"各項分別微分得：${a*3}x^2 + 5$。"
    elif i <= 20:
        b = i - 5
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"求函數 $f(x) = ({b}x+1)(x+2)$ 的導函數 $f'(x)$。"
        opts = [f"${b*2}x + {b*2+1}$", f"${b}x + {b+1}$", f"${b}x^2 + 1$", f"$x + {b}$"]
        sol = f"展開得 $f(x) = {b}x^2 + {b*2+1}x + 2$，故微分為 ${b*2}x + {b*2+1}$。"
    else:
        c = i - 15
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"若 $f(x) = \\frac{{x}}{{{c}x+1}}$，試求 $f'(x)$ 的解析式為何？"
        opts = [f"$\\frac{{1}}{{({c}x+1)^2}}$", f"$\\frac{{x}}{{({c}x+1)^2}}$", f"$\\frac{{1}}{{{c}x+1}}$", f"$\\frac{{{c}}}{{({c}x+1)^2}}$"]
        sol = f"商式微分法：$\\frac{{1 \\cdot ({c}x+1) - x \\cdot {c}}}{{({c}x+1)^2}} = \\frac{{1}}{{({c}x+1)^2}}$。"
    sec3_choices.append((text, ans, opts, sol))

sec3_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 1
        text = f"求 $f(x) = {c}x^3 + x^2$ 的導函數在 $x=1$ 的值。"
        ans_val = c * 3 + 2
        sol = f"$f'(x) = {c*3}x^2 + 2x$。代入 $x=1 \\implies {c*3}(1) + 2(1) = {c*3+2}$。"
    else:
        d = i + 11
        text = f"若 $f(x) = \\frac{{{d}x+1}}{{x+2}}$，求 $f'(0)$ 的精確值。"
        ans_val = round((d * 2 - 1) / 4, 2)
        sol = f"$f'(x) = \\frac{{{d}(x+2) - ({d}x+1) \\cdot 1}}{{(x+2)^2}} = \\frac{{{d*2-1}}}{{(x+2)^2}}$。代入 $x=0 \\implies \\frac{{{d*2-1}}}{{4}} = {round((d*2-1)/4, 2)}$。"
    sec3_fills.append((text, ans_val, sol))

# Sec 2.4: 三角函數的導數
sec4_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 2
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"求 $\\frac{{d}}{{dx}} ({a}\\sin x + \\cos x)$ 的導函數。"
        opts = [f"${a}\\cos x - \\sin x$", f"${a}\\cos x + \\sin x$", f"$-{a}\\cos x - \\sin x$", f"${a}\\sin x$"]
        sol = f"由 $(\\sin x)' = \\cos x$ 且 $(\\cos x)' = -\\sin x$，結果為 ${a}\\cos x - \\sin x$。"
    elif i <= 20:
        b = i - 5
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"求函數 $y = {b}\\tan x$ 的導函數為何？"
        opts = [f"${b}\\sec^2 x$", f"${b}\\csc^2 x$", f"${b}\\sec x \\tan x$", f"${b}\\cos^2 x$"]
        sol = f"根據公式：$(\\tan x)' = \\sec^2 x$。故為 ${b}\\sec^2 x$。"
    else:
        k = i - 15
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"計算 $\\frac{{d}}{{dx}} ({k}x \\sin x)$ 的結果。"
        opts = [f"${k}\\sin x + {k}x \\cos x$", f"${k}\\sin x - {k}x \\cos x$", f"${k}\\cos x$", f"${k}x \\cos x$"]
        sol = f"乘積微分法：$({k}x)' \\sin x + {k}x(\\sin x)' = {k}\\sin x + {k}x \\cos x$。"
    sec4_choices.append((text, ans, opts, sol))

sec4_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 1
        text = f"已知 $f(x) = {c}\\sin x + 2\\cos x$，求 $f'(0)$ 的精確值。"
        ans_val = c
        sol = f"導函數為 $f'(x) = {c}\\cos x - 2\\sin x$。代入 $x=0 \\implies {c}\\cos 0 - 2\\sin 0 = {c}$。"
    else:
        d = i + 11
        text = f"若 $f(x) = {d}\\cos x + 3\\sin x$，求 $f'(\\pi/2)$ 的精確值。"
        ans_val = -d
        sol = f"$f'(x) = -{d}\\sin x + 3\\cos x$。代入 $x=\\pi/2 \\implies -{d}\\sin(\\pi/2) + 3\\cos(\\pi/2) = -{d}(1) + 0 = -{d}$。"
    sec4_fills.append((text, ans_val, sol))

# Sec 2.5: 連鎖律
sec5_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 1
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"利用連鎖律計算 $\\frac{{d}}{{dx}} (x^2 + 1)^{a}$。"
        opts = [f"${a*2}x(x^2 + 1)^{a-1}$", f"${a}x(x^2 + 1)^{a-1}$", f"${a*2}(x^2 + 1)^{a}$", f"$2x(x^2 + 1)^{a-1}$"]
        sol = f"外層：${a}(x^2+1)^{a-1}$，內層 $2x$。結果為 ${a*2}x(x^2+1)^{a-1}$。"
    elif i <= 20:
        c = i - 5
        ans = "D" if i % 4 == 1 else ("C" if i % 4 == 2 else ("B" if i % 4 == 3 else "A"))
        text = f"求 $\\frac{{d}}{{dx}} (\\sin({c}x))$ 的結果。"
        opts = [f"${c}\\cos({c}x)$", f"$\\cos({c}x)$", f"$-{c}\\cos({c}x)$", f"${c}\\sin({c}x)$"]
        sol = f"外層微分為 $\\cos({c}x)$，內層微分為 ${c}$。故為 ${c}\\cos({c}x)$。"
    else:
        k = i - 15
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"求函數 $y = \\sqrt{{{k}x+1}}$ 的導函數。"
        opts = [f"$\\frac{{{k}}}{{2\\sqrt{{{k}x+1}}}}$", f"$\\frac{{1}}{{2\\sqrt{{{k}x+1}}}}$", f"$\\frac{{{k}}}{{\\sqrt{{{k}x+1}}}}$", f"$\\frac{{2k}}{{\\sqrt{{{k}x+1}}}}$"]
        sol = f"由連鎖律：$\\frac{{1}}{{2\\sqrt{{{k}x+1}}}} \\cdot ({k}x+1)' = \\frac{{{k}}}{{2\\sqrt{{{k}x+1}}}}$。"
    sec5_choices.append((text, ans, opts, sol))

sec5_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 1
        text = f"求導函數 $f(x) = (2x+1)^{c}$ 在 $x=0$ 處的值。"
        ans_val = c * 2
        sol = f"$f'(x) = {c}(2x+1)^{c-1} \\cdot 2 = {c*2}(2x+1)^{c-1}$。代入 $x=0 \\implies {c*2}(1) = {c*2}$。"
    else:
        d = i + 1
        text = f"若 $f(x) = \\cos({d}x)$，求 $f'(0)$ 的值。"
        ans_val = 0
        sol = f"導函數 $f'(x) = -{d}\\sin({d}x)$。代入 $x=0 \\implies -{d}\\sin 0 = 0$。"
    sec5_fills.append((text, ans_val, sol))

# Sec 2.6: 隱函數微分
sec6_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 1
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"若 $x^2 + y^2 = {a*a}$，試求其隱函數導函數 $\\frac{{dy}}{{dx}}$。"
        opts = [f"$-\\frac{{x}}{{y}}$", f"$\\frac{{x}}{{y}}$", f"$-\\frac{{y}}{{x}}$", f"$\\frac{{y}}{{x}}$"]
        sol = f"對 $x$ 微分得 $2x + 2y \\frac{{dy}}{{dx}} = 0 \\implies \\frac{{dy}}{{dx}} = -\\frac{{x}}{{y}}$。"
    elif i <= 20:
        c = i - 5
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"若 $x^2 + {c}y^3 = 10$，試求 $\\frac{{dy}}{{dx}}$ 的結果。"
        opts = [f"$-\\frac{{2x}}{{{c*3}y^2}}$", f"$\\frac{{2x}}{{{c*3}y^2}}$", f"$-\\frac{{2x}}{{y}}$", f"$-\\frac{{x}}{{y}}$"]
        sol = f"微分得 $2x + {c*3}y^2 \\frac{{dy}}{{dx}} = 0 \\implies \\frac{{dy}}{{dx}} = -\\frac{{2x}}{{{c*3}y^2}}$。"
    else:
        k = i - 15
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"已知 $x^3 + y^3 = {k}$，求在 $x=1$ 且 $y=1$（假設該點成立）時的切線斜率。"
        opts = [f"$-1$", f"$1$", f"$0$", f"$-2$"]
        sol = f"$3x^2 + 3y^2 \\frac{{dy}}{{dx}} = 0 \\implies \\frac{{dy}}{{dx}} = -\\frac{{x^2}}{{y^2}}$。代入 $(1, 1) \\implies -1$。"
    sec6_choices.append((text, ans, opts, sol))

sec6_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 11
        text = f"已知曲線為 $x^2 + y^2 = {c*c}$，求在 $(0, {c})$ 處切線的斜率。"
        ans_val = 0
        sol = f"隱函數微分為 $\\frac{{dy}}{{dx}} = -\\frac{{x}}{{y}}$。代入 $x=0, y={c} \\implies -0/{c} = 0$。"
    else:
        d = i + 1
        text = f"已知曲線為 $x y = {d}$，求在 $(1, {d})$ 處切線斜率的絕對值。"
        ans_val = d
        sol = f"$1 \\cdot y + x \\frac{{dy}}{{dx}} = 0 \\implies \\frac{{dy}}{{dx}} = -\\frac{{y}}{{x}}$。代入 $(1, {d}) \\implies -{d}$，絕對值為 {d}。"
    sec6_fills.append((text, ans_val, sol))

# Sec 2.7: 自然與社會科學中的變化率
sec7_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 2
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"某物體受重力作用向下運動，高度 $h(t) = -{a}t^2 + 100$，求在 $t=2$ 秒時的瞬時速率。"
        opts = [f"${a*4}$", f"${a*2}$", f"$4$", f"$100$"]
        sol = f"速度 $v(t) = -{a*2}t$，速率為絕對值。在 $t=2$ 時，$|-{a*4}| = {a*4}$。"
    elif i <= 20:
        b = i - 5
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"某化學反應物質量 $M(t) = {b}t^2 + t$，求當 $t=1$ 時之反應速率。"
        opts = [f"${b*2+1}$", f"${b}$", f"${b+1}$", f"$2$"]
        sol = f"反應速率為 $M'(t) = {b*2}t + 1$。代入 $t=1$ 得 ${b*2+1}$。"
    else:
        c = i - 15
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"設總成本函數為 $C(x) = {c}x^2 + 20x$，求 $x=10$ 時之邊際成本。"
        opts = [f"${c*20+20}$", f"${c*10+20}$", f"$20$", f"${c*20}$"]
        sol = f"邊際成本為 $C'(x) = {c*2}x + 20$。代入 $x=10 \\implies {c*2}(10) + 20 = {c*20+20}$。"
    sec7_choices.append((text, ans, opts, sol))

sec7_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 1
        text = f"若某成本函數為 $C(x) = {c}x^2 + 30x + 100$，試求 $x=2$ 時之邊際成本。"
        ans_val = c * 4 + 30
        sol = f"$C'(x) = {c*2}x + 30$。代入 $x=2 \\implies {c*2}(2) + 30 = {c*4+30}$。"
    else:
        d = i + 1
        text = f"若一粒子之速度函數為 $v(t) = {d}t^2 + 4t$，求 $t=3$ 時之加速度。"
        ans_val = d * 6 + 4
        sol = f"$a(t) = v'(t) = {d*2}t + 4$。代入 $t=3 \\implies {d*2}(3)+4 = {d*6+4}$。"
    sec7_fills.append((text, ans_val, sol))

# Sec 2.8: 相關變率
sec8_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 1
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"正方形的邊長以 {a} cm/s 的速率增加，當邊長為 10 cm 時，其面積增加速率為多少 $\\text{{cm}}^2\\text{{/s}}$？"
        opts = [f"${a*20}$", f"${a*10}$", f"${a*2}$", f"$20$"]
        sol = f"$A = x^2 \\implies \\frac{{dA}}{{dt}} = 2x \\frac{{dx}}{{dt}}$。代入 $x=10, \\frac{{dx}}{{dt}} = {a} \\implies 2 \\times 10 \\times {a} = {a*20}$。"
    elif i <= 20:
        b = i - 5
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"圓的半徑以 {b} cm/s 增加，當半徑為 2 cm 時，面積的增加速率為何？"
        opts = [f"${b*4}\\pi$", f"${b*2}\\pi$", f"${b}\\pi$", f"$4\\pi$"]
        sol = f"$A = \\pi r^2 \\implies \\frac{{dA}}{{dt}} = 2\\pi r \\frac{{dr}}{{dt}} = 2\\pi(2)({b}) = {b*4}\\pi$。"
    else:
        c = i - 15
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"球體半徑以 {c} cm/s 增加，當半徑為 3 cm 時，表面積 $S = 4\\pi r^2$ 的增加速率為何？"
        opts = [f"${c*24}\\pi$", f"${c*12}\\pi$", f"$24\\pi$", f"$12\\pi$"]
        sol = f"$\\frac{{dS}}{{dt}} = 8\\pi r \\frac{{dr}}{{dt}} = 8\\pi(3)({c}) = {c*24}\\pi$。"
    sec8_choices.append((text, ans, opts, sol))

sec8_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 1
        text = f"正方形的邊長以 {c} cm/s 的速率增加，求當邊長為 5 cm 時，面積的增加速率為何？"
        ans_val = c * 10
        sol = f"$\\frac{{dA}}{{dt}} = 2x \\frac{{dx}}{{dt}} = 2(5)({c}) = {c*10}$。"
    else:
        d = i + 1
        text = f"圓面積以 {d*40}\\pi \\text{{ cm}}^2\\text{{/s}} 的速率增加，當半徑為 10 cm 時，半徑的增加速率為何？"
        ans_val = d * 2
        sol = f"$\\frac{{dA}}{{dt}} = 2\\pi r \\frac{{dr}}{{dt}} \\implies {d*40}\\pi = 2\\pi(10)\\frac{{dr}}{{dt}} \\implies \\frac{{dr}}{{dt}} = {d*2}$。"
    sec8_fills.append((text, ans_val, sol))

# Sec 2.9: 線性逼近與微分
sec9_choices = []
for i in range(1, 31):
    if i <= 10:
        a = i + 2
        ans = "C" if i % 4 == 1 else ("D" if i % 4 == 2 else ("A" if i % 4 == 3 else "B"))
        text = f"求函數 $f(x) = x^2$ 在 $a=2$ 處的線性化 $L(x)$。"
        opts = [f"$4x - 4$", f"$4x$", f"$2x + 4$", f"$4x + 4$"]
        sol = f"$L(x) = f(2) + f'(2)(x-2) = 4 + 4(x-2) = 4x - 4$。"
    elif i <= 20:
        b = i - 5
        ans = "A" if i % 4 == 1 else ("B" if i % 4 == 2 else ("C" if i % 4 == 3 else "D"))
        text = f"已知 $y = x^3$，當 $x=2$ 且 $\\Delta x = 0.1$ 時，試問其微分 $dy$ 為何？"
        opts = [f"$1.2$", f"$12$", f"$0.1$", f"$0.4$"]
        sol = f"$dy = 3x^2 dx = 3(2)^2(0.1) = 12(0.1) = 1.2$。"
    else:
        k = i - 15
        ans = "B" if i % 4 == 1 else ("C" if i % 4 == 2 else ("D" if i % 4 == 3 else "A"))
        text = f"利用線性逼近公式估算 $(1+x)^{{{k}}}$ 在 $x \\approx 0$ 時的近似函數。"
        opts = [f"$1 + {k}x$", f"$1 + x$", f"${k}x$", f"$1 - {k}x$"]
        sol = f"$f(x) = (1+x)^{{{k}}} \\implies f(0)=1, f'(0)={k} \\implies L(x) = 1 + {k}x$。"
    sec9_choices.append((text, ans, opts, sol))

sec9_fills = []
for i in range(1, 21):
    if i <= 10:
        c = i + 1
        text = f"若函數 $f(x) = {c}x^2$ 在 $x=1$ 且 $dx=0.1$，試求 $dy$ 的精確值。"
        ans_val = round(c * 2 * 0.1, 2)
        sol = f"$dy = 2 \\cdot {c}x dx = {c*2}(1)(0.1) = {round(c*2*0.1, 2)}$。"
    else:
        d = i + 1
        text = f"若 $y = \\sqrt{{x}}$，當 $x=1$ 且 $dx = 0.2$ 時，求 $dy$ 的精確值。"
        ans_val = round(0.5 * 0.2, 2)
        sol = f"$dy = \\frac{{1}}{{2\\sqrt{{x}}}} dx = \\frac{{1}}{{2}}(0.2) = 0.1$。"
    sec9_fills.append((text, ans_val, sol))

if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_2")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch2_sec1.md").write_text(generate_section(1, "導數與變化率", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch2_sec2.md").write_text(generate_section(2, "導數作為一個函數", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch2_sec3.md").write_text(generate_section(3, "微分公式", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch2_sec4.md").write_text(generate_section(4, "三角函數的導數", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch2_sec5.md").write_text(generate_section(5, "連鎖律", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch2_sec6.md").write_text(generate_section(6, "隱函數微分", sec6_choices, sec6_fills), encoding='utf-8')
    (out_dir / "ch2_sec7.md").write_text(generate_section(7, "自然與社會科學中的變化率", sec7_choices, sec7_fills), encoding='utf-8')
    (out_dir / "ch2_sec8.md").write_text(generate_section(8, "相關變率", sec8_choices, sec8_fills), encoding='utf-8')
    (out_dir / "ch2_sec9.md").write_text(generate_section(9, "線性逼近與微分", sec9_choices, sec9_fills), encoding='utf-8')
    
    # Generate Review: pick 30 choice questions and 20 fill questions across sections
    review_choices = (sec1_choices[:4] + sec2_choices[:3] + sec3_choices[:3] + 
                      sec4_choices[:3] + sec5_choices[:4] + sec6_choices[:3] + 
                      sec7_choices[:3] + sec8_choices[:3] + sec9_choices[:4])
    review_fills = (sec1_fills[:3] + sec2_fills[:2] + sec3_fills[:2] + 
                    sec4_fills[:2] + sec5_fills[:3] + sec6_fills[:2] + 
                    sec7_fills[:2] + sec8_fills[:2] + sec9_fills[:2])
    
    # Exactly 30 choices and 20 fills
    review_choices = review_choices[:30]
    review_fills = review_fills[:20]
    
    (out_dir / "ch2_final.md").write_text(generate_review(review_choices, review_fills), encoding='utf-8')
    
    print("All Chapter 2 files and review generated successfully.")
