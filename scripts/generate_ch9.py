import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 9.{sec_id} 節：{title}",
        "",
        f"本節收錄 9.{sec_id} 節相關題目。",
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


# 9.1: Modeling with Differential Equations
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"對於一階常微分方程 $\\frac{{dy}}{{dt}} = {a}y$，其最一般的通解形式為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$y(t) = C e^{{{a}t}}$", f"$y(t) = C e^{{-{a}t}}$", f"$y(t) = {a}t + C$", f"$y(t) = C e^{{t/{a}}}$"]
        sol = "分離變數積分：$\\int \\frac{1}{y} dy = \\int a dt \\implies \\ln|y| = at + C_1 \\implies y(t) = C e^{at}$。"
    else:
        text = f"判斷下列哪一個函數是 $\\frac{{d^2y}}{{dx^2}} + {a*a}y = 0$ 的解？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\cos({a}x)$", f"$\\sin({a}x)$", f"$e^{{{a}x}}$", f"$x^{{{a}}}$"]
        sol = f"對 $y = \\cos({a}x)$ 求二次導數得 $y'' = -{a*a}\\cos({a}x)$。代入原微分方程滿足 $y'' + {a*a}y = 0$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"已知一函數滿足 $\\frac{{dy}}{{dx}} = {c}x$，且 $y(0) = 5$，求 $y(2)$ 之精確值。"
    sol = f"積分為 $y(x) = \\frac{{{c}}}{{2}}x^2 + C$。代入 $y(0)=5 \\implies C=5$。故 $y(x) = \\frac{{{c}}}{{2}}x^2 + 5$。代入 $x=2 \\implies y(2) = \\frac{{{c}}}{{2}}(4) + 5 = 2{c} + 5$。"
    ans_val = 2 * c + 5
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 9.2: Direction Fields and Euler's Method
sec2_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"利用方向場（Direction Fields），若在點 $(x, y)$ 處的斜率為 $x + {a}y$，則當 $x=1, y=0$ 時的切線斜率為何？"
        ans = "B" if i % 4 == 0 else "A"
        opts = ["$1$", f"${a}$", f"${a+1}$", "$0$"]
        sol = f"代入 $(1, 0)$ 到公式 $x + {a}y$ 中得 $1 + {a}(0) = 1$。"
    else:
        text = f"使用歐拉方法（Euler's Method）估算 $\\frac{{dy}}{{dx}} = f(x, y)$，其疊代公式為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["$y_{n+1} = y_n + h f(x_n, y_n)$", "$y_{n+1} = y_n + f(x_n, y_n)$", "$y_{n+1} = y_n + h x_n$", "$y_{n+1} = y_n + \\frac{h}{2} f(x_n, y_n)$"]
        sol = "歐拉方法疊代公式為 $y_{n+1} = y_n + h f(x_n, y_n)$，其中 $h$ 為步長。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"設 $\\frac{{dy}}{{dx}} = {c}$，初始值 $y(0) = 1$，利用歐拉方法以步長 $h=1$ 估計 $y(1)$ 的值。"
    sol = f"歐拉疊代：$y_1 = y_0 + h f(x_0, y_0) = 1 + 1\\cdot {c} = 1 + {c}$。"
    ans_val = 1 + c
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 9.3: Separable Equations
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求可分離變數方程 $\\frac{{dy}}{{dx}} = {a}xy$ 的最一般通解。"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"$y = C e^{{\\frac{{{a}}}{{2}}x^2}}$", f"$y = C e^{{{a}x}}$", f"$y = \\frac{{{a}}}{{2}}x^2 + C$", f"$y = C e^{{x^2}}$"]
        sol = f"分離變數得 $\\int \\frac{{1}}{{y}} dy = \\int {a}x dx \\implies \\ln|y| = \\frac{{{a}}}{{2}}x^2 + C_1 \\implies y = C e^{{\\frac{{{a}}}{{2}}x^2}}$。"
    else:
        text = f"對於 $\\frac{{dy}}{{dx}} = \\frac{{y}}{{x}}$，其最一般通解為何？"
        ans = "B" if i % 4 == 1 else "D"
        opts = ["$y = C x$", "$y = C e^x$", "$y = x + C$", "$y = C x^2$"]
        sol = "分離變數得 $\\int \\frac{1}{y} dy = \\int \\frac{1}{x} dx \\implies \\ln|y| = \\ln|x| + C_1 \\implies y = C x$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"解微分方程 $\\frac{{dy}}{{dx}} = {c}y$，若 $y(0) = 2$，求 $y(1)$ 之精確值（以 $e$ 的倍數表示，保留2位小數）。"
    sol = f"通解為 $y(x) = C e^{{{c}x}}$。代入 $y(0)=2 \\implies C=2$。故 $y(1) = 2 e^{{{c}}}$。結果為 {round(2 * 2.71828**c, 2)}。"
    ans_val = round(2 * 2.71828**c, 2)
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 9.4: Models for Population Growth
sec4_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"在邏輯斯增長模型中，當族群大小 $P(t)$ 遠小於環境承載量 $K$ 時，族群增長最接近哪種增長？"
        ans = "B" if i % 4 == 0 else "A"
        opts = ["指數增長", "線性增長", "對數增長", "恆定不變"]
        sol = "當 $P(t) \\ll K$ 時，邏輯斯微分方程 $\\frac{dP}{dt} = kP(1 - \\frac{P}{K})$ 中的 $(1 - \\frac{P}{K})$ 趨近於 1，故最接近指數增長。"
    else:
        text = f"邏輯斯增長模型（Logistic Growth Model）的微分方程形式為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["$\\frac{dP}{dt} = k P (1 - \\frac{P}{K})$", "$\\frac{dP}{dt} = k P$", "$\\frac{dP}{dt} = k P^2$", "$\\frac{dP}{dt} = k (K - P)$"]
        sol = "邏輯斯模型的標準微分方程形式為 $\\frac{dP}{dt} = k P (1 - \\frac{P}{K})$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"一族群大小滿足邏輯斯方程 $\\frac{{dP}}{{dt}} = {c} P (1 - \\frac{{P}}{{100}})$，求此族群的環境承載量 $K$。"
    sol = "承載量為公式中括號的分母值，即 $K = 100$。"
    ans_val = 100
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 9.5: Linear Equations
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求一階線性微分方程 $\\frac{{dy}}{{dx}} + {a}y = e^x$ 的積分因子（Integrating Factor）。"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"$e^{{{a}x}}$", f"$e^{{-{a}x}}$", f"$x^{{{a}}}$", f"$e^{{{a*2}x}}$"]
        sol = f"積分因子公式 $I(x) = e^{{\\int P(x) dx}} = e^{{\\int {a} dx}} = e^{{{a}x}}$。"
    else:
        text = f"對於一階線性微分方程 $\\frac{{dy}}{{dx}} + P(x)y = Q(x)$，應該乘上何種積分因子以進行化簡？"
        ans = "B" if i % 4 == 1 else "D"
        opts = ["$e^{\\int P(x) dx}$", "$e^{\\int Q(x) dx}$", "$\\int P(x) dx$", "$e^{P(x)}$"]
        sol = "一階線性微分方程最基本的求解技巧就是乘以積分因子 $I(x) = e^{\\int P(x) dx}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"已知一階線性微分方程之積分因子為 $I(x) = e^{{{c}x}}$，求 $P(x)$ 之值。"
    sol = f"因 $I(x) = e^{{\\int P(x) dx}} = e^{{{c}x}} \\implies P(x) = {c}$。"
    ans_val = c
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 9.6: Predator-Prey Systems
sec6_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"在洛特卡－沃爾泰拉（Lotka-Volterra）捕食者－獵物模型中，當沒有捕食者（$y=0$）存在時，獵物（$x$）族群呈現何種增長？"
        ans = "B" if i % 4 == 0 else "A"
        opts = ["指數增長", "邏輯斯增長", "線性增長", "隨機增長"]
        sol = "在洛特卡－沃爾泰拉模型中，獵物的方程為 $\\frac{dx}{dt} = k x - a x y$。當 $y=0$ 時，$\\frac{dx}{dt} = k x$，呈現典型的指數增長。"
    else:
        text = f"捕食者族群方程中，當沒有獵物（$x=0$）存在時，捕食者族群會如何變化？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["指數衰減", "指數增長", "維持常數", "對數增長"]
        sol = "捕食者方程為 $\\frac{dy}{dt} = -r y + b x y$。當 $x=0$ 時，$\\frac{dy}{dt} = -r y$，呈現指數衰減。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"在捕食者方程 $\\frac{{dy}}{{dt}} = -{c} y + 0.01 x y$ 中，捕食者的自然死亡率 $r$ 為多少？"
    sol = f"對應公式中死亡率項 $-r y$，死亡率 $r = {c}$。"
    ans_val = c
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_9")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch9_sec1.md").write_text(generate_section(9, 1, "微分方程建模", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch9_sec2.md").write_text(generate_section(9, 2, "方向場與歐拉方法", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch9_sec3.md").write_text(generate_section(9, 3, "可分離變數方程", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch9_sec4.md").write_text(generate_section(9, 4, "人口增長模型", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch9_sec5.md").write_text(generate_section(9, 5, "線性微分方程", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch9_sec6.md").write_text(generate_section(9, 6, "掠食者與獵物系統", sec6_choices, sec6_fills), encoding='utf-8')
    
    print("Chapter 9 sections generated successfully.")
