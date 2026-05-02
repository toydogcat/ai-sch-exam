import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 10.{sec_id} 節：{title}",
        "",
        f"本節收錄 10.{sec_id} 節相關題目。",
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


# 10.1: Curves Defined by Parametric Equations
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"對於一條參數曲線 $x = t^2$, $y = t^3 - {a}t$，求此曲線在 $t=1$ 處的點坐標 $(x, y)$。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$(1, {1 - a})$", "$(1, 1)$", f"$(1, {a})$", "$(0, 0)$"]
        sol = "代入 $t=1$ 進入參數方程得 $x = 1^2 = 1$，$y = 1^3 - a(1) = 1 - a$。"
    else:
        text = f"已知參數方程 $x = {a}\\cos t$, $y = {a}\\sin t$（$0 \\le t \\le 2\\pi$），此參數曲線所代表的幾何圖形為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["圓", "橢圓", "雙曲線", "拋物線"]
        sol = f"因為 $x^2 + y^2 = ({a}\\cos t)^2 + ({a}\\sin t)^2 = {a*a}(\\cos^2 t + \\sin^2 t) = {a*a}$，其為一圓方程。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"設參數曲線 $x = t + {c}$, $y = 2t + 1$，將其消去參數 $t$ 得到直角坐標方程 $y = mx + b$，求斜率 $m$ 的值。"
    sol = f"由 $x = t + {c} \\implies t = x - {c}$。代入 $y = 2(x - {c}) + 1 = 2x - {2*c - 1}$。斜率 $m=2$。"
    ans_val = 2
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 10.2: Calculus with Parametric Curves
sec2_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"一條參數曲線由 $x = {a}t^2$, $y = t^3$ 所定義，求其切線斜率 $\\frac{{dy}}{{dx}}$ 的一般表達式。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{3t}}{{{2*a}}}$", f"$\\frac{{2t}}{{{a}}}$", f"$\\frac{{t}}{{{a}}}$", f"${a}t$"]
        sol = "切線斜率公式 $\\frac{dy}{dx} = \\frac{dy/dt}{dx/dt} = \\frac{3t^2}{2at} = \\frac{3t}{2a}$。"
    else:
        text = f"參數曲線的第二階導數 $\\frac{{d^2y}}{{dx^2}}$ 的正確計算公式為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["$\\frac{\\frac{d}{dt}(\\frac{dy}{dx})}{dx/dt}$", "$\\frac{d^2y/dt^2}{d^2x/dt^2}$", "$\\frac{dy/dt}{dx/dt}$", "$\\frac{dy}{dx}$"]
        sol = "參數方程二階導數公式為 $\\frac{d}{dt}(\\frac{dy}{dx}) / \\frac{dx}{dt}$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"一條參數曲線為 $x = t^2 + 1$, $y = {c}t^3$，求當 $t=1$ 時切線斜率 $\\frac{{dy}}{{dx}}$ 的值。"
    sol = f"$\\frac{{dy}}{{dx}} = \\frac{{dy/dt}}{{dx/dt}} = \\frac{{3{c}t^2}}{{2t}} = \\frac{{3{c}t}}{{2}}$。代入 $t=1 \\implies \\frac{{3{c}}}{{2}}$。結果為 {round(1.5*c, 2)}。"
    ans_val = round(1.5 * c, 2)
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 10.3: Polar Coordinates
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"若某點的極坐標為 $(r, \\theta) = ({a}, \\frac{{\\pi}}{{2}})$，將其轉換為直角坐標 $(x, y)$。"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"$(0, {a})$", f"$({a}, 0)$", f"$(0, -{a})$", f"$(1, {a})$"]
        sol = f"直角坐標：$x = {a}\\cos(\\frac{{\\pi}}{{2}}) = 0$，$y = {a}\\sin(\\frac{{\\pi}}{{2}}) = {a}$。"
    else:
        text = f"極坐標方程 $r = {a}\\cos\\theta$ 在直角坐標下所代表的圖形為何？"
        ans = "B" if i % 4 == 1 else "D"
        opts = ["圓", "直線", "橢圓", "雙曲線"]
        sol = f"乘以 $r$ 得 $r^2 = {a}r\\cos\\theta \\implies x^2 + y^2 = {a}x$，移項後代表一個圓心在 $({a/2}, 0)$ 的圓。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"已知一點在直角坐標為 $({c}, 0)$，求其對應的極半徑 $r$ 的值。"
    sol = f"極半徑 $r = \\sqrt{{x^2 + y^2}} = \\sqrt{{{c}^2 + 0}} = {c}$。"
    ans_val = c
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 10.4: Areas and Lengths in Polar Coordinates
sec4_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求極坐標曲線 $r = {a}\\theta$ 在 $0 \\le \\theta \\le 2$ 範圍內圍成的面積。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\frac{{{a*a}}}{{3}}$", f"${a*a}$", f"$\\frac{{{a}}}{{2}}$", f"${2*a}$"]
        sol = "極坐標面積公式：$A = \\int_a^b \\frac{1}{2} r^2 d\\theta$。故 $A = \\int_0^2 \\frac{1}{2} (a\\theta)^2 d\\theta = \\frac{a^2}{2} [\\frac{\\theta^3}{3}]_0^2 = \\frac{a^2}{2} \\cdot \\frac{8}{3} = \\frac{4a^2}{3}$。"
    else:
        text = f"極坐標曲線 $r = f(\\theta)$ 在 $a \\le \\theta \\le b$ 的弧長公式為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["$\\int_a^b \\sqrt{r^2 + (\\frac{dr}{d\\theta})^2} d\\theta$", "$\\int_a^b \\sqrt{1 + (\\frac{dr}{d\\theta})^2} d\\theta$", "$\\int_a^b r d\\theta$", "$\\int_a^b \\frac{1}{2}r^2 d\\theta$"]
        sol = "極坐標下的弧長公式為 $\\int_a^b \\sqrt{r^2 + (dr/d\\theta)^2} d\\theta$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求圓 $r = {c}$ 在 $0 \\le \\theta \\le 2\\pi$ 的定積分求出的總面積（以 $\\pi$ 的倍數表示）。"
    sol = f"公式 $A = \\int_0^{{2\\pi}} \\frac{{1}}{{2}} r^2 d\\theta = \\frac{{1}}{{2}} {c*c} (2\\pi) = {c*c}\\pi$。結果為 {c*c}。"
    ans_val = c * c
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 10.5: Conic Sections
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"拋物線 $y^2 = {4*a}x$ 的焦點坐標為何？"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"$({a}, 0)$", f"$(0, {a})$", f"$(-{a}, 0)$", f"$(1, {a})$"]
        sol = f"標準拋物線形式為 $y^2 = 4px$，此處 $4p = {4*a} \\implies p = {a}$。故焦點為 $({a}, 0)$。"
    else:
        text = f"橢圓 $\\frac{{x^2}}{{{a*a}}} + \\frac{{y^2}}{{1}} = 1$ 當 ${a} > 1$ 時的離心率 $e$ 為何？"
        ans = "B" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{\\sqrt{{{a*a} - 1}}}}{{{a}}}$", f"$\\frac{{1}}{{{a}}}$", f"$\\frac{{\\sqrt{{{a*a} + 1}}}}{{{a}}}$", f"$1$"]
        sol = f"橢圓中 $c = \\sqrt{{a^2 - b^2}} = \\sqrt{{a^2 - 1}}$，離心率 $e = \\frac{{c}}{{a}} = \\frac{{\\sqrt{{{a*a} - 1}}}}{{{a}}}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"設拋物線方程為 $y^2 = {4*c}x$，求準線（Directrix）方程 $x = k$ 的 $k$ 值。"
    sol = f"準線為 $x = -p$。因 $4p = {4*c} \\implies p = {c}$。故準線為 $x = -{c}$。"
    ans_val = -c
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 10.6: Conic Sections in Polar Coordinates
sec6_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"若圓錐曲線極坐標方程為 $r = \\frac{{{a}}}{{1 + e\\cos\\theta}}$，當 $e=1$ 時，此圓錐曲線屬於何種幾何圖形？"
        ans = "B" if i % 4 == 0 else "A"
        opts = ["拋物線", "橢圓", "雙曲線", "圓"]
        sol = "圓錐曲線分類依據離心率 $e$ 的大小。當 $e=1$ 時為拋物線，當 $e < 1$ 時為橢圓，當 $e > 1$ 時為雙曲線。"
    else:
        text = f"若圓錐曲線極坐標方程中，離心率 $e = \\frac{{1}}{{{a}}}$ 且 ${a} > 1$，則此曲線為何種圖形？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["橢圓", "拋物線", "雙曲線", "圓"]
        sol = f"因為 $e = \\frac{1}{a} < 1$，故此圓錐曲線為橢圓。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"若圓錐曲線之極坐標方程為 $r = \\frac{{{c}}}{{1 + e\\cos\\theta}}$，離心率 $e=0$，求此極坐標方程所化簡出之圓半徑。"
    sol = f"當 $e=0$ 時，方程式簡化為 $r = {c}$，這正是一個圓心在極點、半徑為 {c} 的圓。"
    ans_val = c
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_10")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch10_sec1.md").write_text(generate_section(10, 1, "參數方程定義的曲線", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch10_sec2.md").write_text(generate_section(10, 2, "參數曲線的微積分", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch10_sec3.md").write_text(generate_section(10, 3, "極坐標", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch10_sec4.md").write_text(generate_section(10, 4, "極坐標下的面積與長度", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch10_sec5.md").write_text(generate_section(10, 5, "圓錐曲線", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch10_sec6.md").write_text(generate_section(10, 6, "極坐標下的圓錐曲線", sec6_choices, sec6_fills), encoding='utf-8')
    
    print("Chapter 10 sections generated successfully.")
