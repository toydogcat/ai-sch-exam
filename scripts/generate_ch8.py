import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 8.{sec_id} 節：{title}",
        "",
        f"本節收錄 8.{sec_id} 節相關題目。",
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


# 8.1: Arc Length
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求函數 $y = {a}x^{{1.5}}$ 在區間 $[0, 1]$ 上的弧長（Arc Length）精確值。"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$\\frac{{1}}{{27}}(\\sqrt{{1 + {1.5*a}^2}} - 1)$", f"$\\sqrt{{1 + {a}^2}}$", f"${a}$", f"$\\frac{{2}}{{{a}}}$"]
        sol = "弧長公式 $L = \\int_a^b \\sqrt{1 + [f'(x)]^2} dx$。對於 $f(x) = " + str(a) + "x^{1.5} \\implies f'(x) = " + str(1.5*a) + "x^{0.5}$，$[f'(x)]^2 = " + str(2.25*a*a) + "x$。故弧長可用代換積分求得。"
    else:
        text = f"對於曲線 $x = g(y)$，在 $c \\le y \\le d$ 上的弧長公式為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["$\\int_c^d \\sqrt{1 + [g'(y)]^2} dy$", "$\\int_c^d (1 + g'(y)) dy$", "$\\int_c^d \\sqrt{1 - [g'(y)]^2} dy$", "$\\int_c^d [g'(y)]^2 dy$"]
        sol = "沿 $y$ 軸積分的弧長公式為 $L = \\int_c^d \\sqrt{1 + [g'(y)]^2} dy$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"設一平滑曲線 $y = {c}x + 2$，求其在 $[0, 3]$ 的弧長。"
    sol = f"此曲線為直線。$y' = {c}$，故弧長 $L = \\int_0^3 \\sqrt{{1 + {c}^2}} dx = 3\\sqrt{{1 + {c*c}}}$。結果為 {round(3 * (1 + c*c)**0.5, 2)}。"
    ans_val = round(3 * (1 + c*c)**0.5, 2)
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 8.2: Area of a Surface of Revolution
sec2_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"將曲線 $y = {a}x$ 在 $[0, 1]$ 繞 $x$ 軸旋轉所生成的表面積。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$\\pi {a}\\sqrt{{1 + {a*a}}}$", f"$2\\pi {a}$", f"$\\pi {a*a}$", f"$\\frac{{\\pi}}{{2}}$"]
        sol = "旋轉體表面積公式：$S = \\int 2\\pi y ds$。因 $y = ax \\implies y' = a$，積分得 $\\int_0^1 2\\pi (ax) \\sqrt{1 + a^2} dx = 2\\pi a\\sqrt{1 + a^2} [\\frac{x^2}{2}]_0^1 = \\pi a\\sqrt{1 + a^2}$。"
    else:
        text = f"若曲線繞 $y$ 軸旋轉，旋轉體表面積公式中應包含哪一項距離 $x$？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["$2\\pi x$", "$2\\pi y$", "$\\pi x^2$", "$2\\pi x^2$"]
        sol = "繞 $y$ 軸旋轉時，曲線上點到旋轉軸的距離為 $x$，故公式為 $S = \\int 2\\pi x ds$。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"將曲線 $y = {c}$（常數函數）在 $[0, 2]$ 繞 $x$ 軸旋轉產生的圓柱體表面積（不含兩底面，精確值以 $\\pi$ 的倍數表示）。"
    sol = f"圓柱側面積公式為 $2\\pi r h$。$r = {c}, h = 2$，故側面積 = $2\\pi ({c})(2) = 4{c}\\pi$。結果為 {round(4*c, 2)}。"
    ans_val = round(4 * c, 2)
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 8.3: Applications to Physics and Engineering
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"將一質量彈簧從平衡位置拉長 $x$ 公尺所需之力為 $f(x) = {a}x$ 牛頓。求將其拉長 $2$ 公尺所作之功（焦耳）。"
        ans = "A" if i % 4 == 0 else "C"
        opts = [f"${2*a}$", f"${a}$", f"${4*a}$", f"${a/2}$"]
        sol = f"功為 $W = \\int_0^2 {a}x dx = [\\frac{{{a}}}{{2}}x^2]_0^2 = 2{a}$ 焦耳。"
    else:
        text = f"水壓公式中，在水下深度 $d$ 處的流體靜壓力（Hydrostatic Pressure）與深度成何種關係？"
        ans = "B" if i % 4 == 1 else "D"
        opts = ["正比於深度 $d$", "正比於深度平方 $d^2$", "與深度無關", "反比於深度 $d$"]
        sol = "流體靜壓力為 $P = \\rho g d$，與深度 $d$ 成正比。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"一彈簧之彈性常數為 $k = {c}$ N/m，求將其由平衡位置拉長 $4$ 公尺所作之功。"
    sol = f"功 $W = \\int_0^4 {c}x dx = [\\frac{{{c}}}{{2}}x^2]_0^4 = 8{c}$ 焦耳。"
    ans_val = 8 * c
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 8.4: Applications to Economics and Biology
sec4_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"在經濟學中，當需求函數為 $p(x) = {100+a} - 0.5x$，且均衡產量為 $20$ 時，求消費者剩餘（Consumer Surplus）。"
        ans = "B" if i % 4 == 0 else "A"
        opts = ["$100$", "$200$", f"${100+a}$", "$50$"]
        sol = "均衡價格為 $p(20) = (100+a) - 10 = 90+a$。消費者剩餘為 $\\int_0^{20} [((100+a) - 0.5x) - (90+a)] dx = \\int_0^{20} (10 - 0.5x) dx = [10x - 0.25x^2]_0^{20} = 200 - 100 = 100$。"
    else:
        text = f"在生物學中，若血液在血管中的流速分布符合泊肅葉定律（Poiseuille's Law），則最大流速發生在血管的何處？"
        ans = "C" if i % 4 == 1 else "D"
        opts = ["中心軸線處", "血管壁邊緣處", "血管壁與中心的中間點", "任何位置流速皆相同"]
        sol = "流速公式為 $v(r) = \\frac{P}{4\\eta L}(R^2 - r^2)$。當 $r=0$（中心軸線）時，流速最大。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"一需求函數為 $p(x) = {c*10}$ 且為水平直線（固定價格），當產量由 $0$ 增至 $5$ 時，消費者剩餘為多少？"
    sol = f"消費者剩餘為 $\\int_0^5 (p(x) - p_0) dx = \\int_0^5 ({c*10} - {c*10}) dx = 0$。"
    ans_val = 0
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 8.5: Probability
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"設一機率密度函數 $f(x) = {a} e^{{-{a}x}}$ （$x \\ge 0$），求此連續隨機變數在 $[0, \\infty)$ 區間的總機率值。"
        ans = "A" if i % 4 == 0 else "C"
        opts = ["$1$", "$0.5$", f"${1/a}$", "$0$"]
        sol = "任何有效的機率密度函數在整個定義域上的總積分必須為 1。"
    else:
        text = f"對於連續型隨機變數 $X$ 且有機率密度函數 $f(x)$，其期望值 $E(X)$ 的微積分定義為何？"
        ans = "B" if i % 4 == 1 else "D"
        opts = ["$\\int_{-\\infty}^\\infty x f(x) dx$", "$\\int_{-\\infty}^\\infty f(x) dx$", "$\\int_{-\\infty}^\\infty x^2 f(x) dx$", "$1$"]
        sol = "期望值定義為 $E(X) = \\int_{-\\infty}^\\infty x f(x) dx$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"設一隨機變數 $X$ 在 $[0, {c}]$ 呈均勻分布（Uniform Distribution），求其機率密度函數在定義域內之常數值。"
    sol = f"總機率為 1。長度為 {c}，故高度（常數值）為 $\\frac{{1}}{{{c}}}$。結果為 {round(1/c, 3)}。"
    ans_val = round(1 / c, 3)
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_8")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch8_sec1.md").write_text(generate_section(8, 1, "弧長", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch8_sec2.md").write_text(generate_section(8, 2, "旋轉體的表面積", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch8_sec3.md").write_text(generate_section(8, 3, "物理與工程應用", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch8_sec4.md").write_text(generate_section(8, 4, "經濟與生物應用", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch8_sec5.md").write_text(generate_section(8, 5, "機率", sec5_choices, sec5_fills), encoding='utf-8')
    
    print("Chapter 8 sections generated successfully.")
