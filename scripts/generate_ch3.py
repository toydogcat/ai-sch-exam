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


# 3.1: Maximum and Minimum Values
sec1_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"求函數 $f(x) = x^2 - {a*2}x$ 在所有實數上的絕對極小值為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$-{a*a}$", f"$-{a}$", f"$0$", f"${a}$"]
        sol = f"微分得 $f'(x) = 2x - {a*2} = 0 \\implies x={a}$。絕對極小值為 $f({a}) = {a}^2 - {a*2}({a}) = -{a*a}$。"
    elif i % 3 == 1:
        text = f"求函數 $f(x) = {a}x - x^2$ 在所有實數上的絕對極大值為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${(a*a)//4}$", f"${a}$", f"$0$", f"不存在"]
        sol = f"$f'(x) = {a} - 2x = 0 \\implies x = {a}/2$。極大值為 ${(a*a)//4}$（取整數簡化）。"
    else:
        text = f"求函數 $f(x) = {a}x$ 在閉區間 $[0, 2]$ 上的最大值為何？"
        ans = "A" if i % 4 == 2 else "C"
        opts = [f"${a*2}$", f"${a}$", f"$2$", f"$0$"]
        sol = f"函數遞增，代入 $x=2$ 得最大值為 ${a*2}$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"求函數 $f(x) = x^3 - {c*3}x^2$ 之相對極小值的 $x$ 座標為何？"
        sol = f"$f'(x) = 3x^2 - {c*6}x = 3x(x - {c*2}) = 0 \\implies x=0$ 或 $x={c*2}$。利用二階導函數檢定，$f''(x) = 6x - {c*6}$。代入 $x={c*2}$ 得正，故為極小值之 $x$ 座標。"
        ans_val = c * 2
    else:
        text = f"求函數 $f(x) = x^2 - {c*2}x$ 之臨界點的 $x$ 座標為何？"
        sol = f"$f'(x) = 2x - {c*2} = 0 \\implies x={c}$。"
        ans_val = c
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.2: The Mean Value Theorem
sec2_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 3 == 0:
        text = f"已知 $f(x) = x^2$ 在閉區間 $[0, {a}]$ 上滿足均值定理，試問對應的 $c$ 值為何？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a/2}$", f"${a}$", f"$1$", f"${a*2}$"]
        sol = f"$f'(c) = 2c = \\frac{{f({a}) - f(0)}}{{{a} - 0}} = \\frac{{{a*a}}}{{{a}}} = {a} \\implies c = {a/2}$。"
    elif i % 3 == 1:
        text = f"已知 $f(x) = x^2 - {a}x$ 在 $[0, {a}]$ 上滿足 Rolle 定理，求對應的 $c$ 值為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a/2}$", f"$0$", f"${a}$", f"$1$"]
        sol = f"$f'(c) = 2c - {a} = 0 \\implies c = {a/2}$。"
    else:
        text = f"下列何者為 Rolle 定理與均值定理不需滿足的條件？"
        ans = "A" if i % 4 == 2 else "B"
        opts = [f"函數值恆為正", f"在開區間內可導", f"在閉區間內連續", f"定義域長度不為 0"]
        sol = f"Rolle 定理與均值定理都不要求函數值恆為正。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(31, 51):
    c = i - 19
    if i % 2 == 0:
        text = f"若 $f(x) = x^2$ 在 $[0, {c*2}]$ 上滿足均值定理，求 $c$ 值為何？"
        sol = f"$f'(c) = 2c = \\frac{{{c*2}^2 - 0}}{{{c*2}-0}} = {c*2} \\implies c = {c}$。"
        ans_val = c
    else:
        text = f"若 $f(x) = x^2 - {c*2}x$ 在 $[0, {c*2}]$ 上滿足 Rolle 定理，求 $c$ 值為何？"
        sol = f"$f'(c) = 2c - {c*2} = 0 \\implies c = {c}$。"
        ans_val = c
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.3: What Derivatives Tell Us about the Shape of a Graph
sec3_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"若 $f''(x) > 0$ 在區間內恆成立，則函數圖形在該區間具有何種特徵？"
        ans = "D" if i % 4 == 0 else "C"
        opts = [f"向上凹", f"向下凹", f"遞增", f"遞減"]
        sol = f"二階導函數大於 0 代表圖形凹向上（Concave Up）。"
    elif i % 3 == 1:
        text = f"若 $f'(x) < 0$ 在區間內恆成立，則函數圖形在該區間具有何種特徵？"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"遞減", f"遞增", f"向上凹", f"向下凹"]
        sol = f"一階導函數小於 0 代表函數為遞減（Decreasing）。"
    else:
        text = f"函數 $f(x) = x^3 - {a*3}x$ 之圖形在何處其凹性向上？"
        ans = "B" if i % 4 == 2 else "A"
        opts = [f"$x > 0$", f"$x < 0$", f"$x > {a}$", f"$x < {a}$"]
        sol = f"$f''(x) = 6x > 0 \\implies x > 0$。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"已知 $f(x) = {c}x^2 + 4x$，求其二階導函數 $f''(x)$ 之值。"
        sol = f"$f'(x) = {c*2}x + 4 \\implies f''(x) = {c*2}$。"
        ans_val = c * 2
    else:
        text = f"已知 $f(x) = x^3 - {c*3}x^2 + 2x$，求其反曲點之 $x$ 座標。"
        sol = f"$f'(x) = 3x^2 - {c*6}x + 2 \\implies f''(x) = 6x - {c*6} = 0 \\implies x={c}$。"
        ans_val = c
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.4: Limits at Infinity; Horizontal Asymptotes
sec4_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 3 == 0:
        text = f"求極限值 $\\lim_{{x \\to \\infty}} \\frac{{{a}x^2 + 1}}{{x^2 + 2}}$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a}$", f"$1$", f"$2$", f"$\\infty$"]
        sol = f"最高次方係數比值為 ${a}$。"
    elif i % 3 == 1:
        text = f"求函數 $y = \\frac{{{a}x}}{{x - 1}}$ 的水平漸近線。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$y = {a}$", f"$y = 1$", f"$x = 1$", f"$y = 0$"]
        sol = f"$\lim_{{x \\to \\infty}} \\frac{{{a}x}}{{x - 1}} = {a} \\implies y = {a}$。"
    else:
        text = f"求極限值 $\\lim_{{x \\to \\infty}} \\frac{{{a}x + 2}}{{3x + 1}}$。"
        ans = "A" if i % 4 == 2 else "B"
        opts = [f"${a}/3$", f"${a}$", f"$3$", f"$2$"]
        sol = f"最高次方項係數比為 ${a}/3$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(31, 51):
    c = i - 15
    if i % 2 == 0:
        text = f"求極限值 $\\lim_{{x \\to \\infty}} \\frac{{{c}x^3 + 2x}}{{x^3 + 5}}$。"
        sol = f"最高次方係數比為 ${c}$。"
        ans_val = c
    else:
        text = f"求極限值 $\\lim_{{x \\to \\infty}} \\frac{{({c*2}x - 1)(x + 2)}}{{x^2 + 1}}$。"
        sol = f"展開分子最高次為 ${c*2}x^2$，除以分母 $x^2 \implies {c*2}$。"
        ans_val = c * 2
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.5: Summary of Curve Sketching
sec5_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"要準確描繪曲線，下列何者不需利用微積分的技巧？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"計算 $y$ 軸截距", f"計算反曲點", f"判斷局部極大極小值", f"判斷凹向上或向下"]
        sol = f"計算截距只需令 $x=0$ 或 $y=0$ 解代數，不需用到導數。"
    elif i % 3 == 1:
        text = f"若函數 $f(x) = x^2 - {a}x$，則此曲線的頂點（極小值處）之 $x$ 座標為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{{a}}}{{2}}$", f"${a}$", f"$2$", f"不存在"]
        sol = f"$f'(x) = 2x - {a} = 0 \\implies x = {a}/2$。"
    else:
        text = f"判斷函數 $f(x) = x^3 - {a*3}x$ 的局部極大值之 $x$ 座標為何？"
        ans = "B" if i % 4 == 2 else "A"
        opts = [f"$-\\{a}$（設 $x=-\\sqrt{{{a}}}$）", f"$\\sqrt{{{a}}}$", f"不存在", f"$0$"]
        sol = f"$f'(x) = 3x^2 - {a*3} = 0 \\implies x = \\pm \\sqrt{{{a}}}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"已知 $f(x) = x^3 - {c*3}x^2$，求此函數的反曲點之 $x$ 座標為何？"
        sol = f"$f'(x) = 3x^2 - {c*6}x \\implies f''(x) = 6x - {c*6} = 0 \\implies x={c}$。"
        ans_val = c
    else:
        text = f"已知 $f(x) = x^4 - {c*6}x^2 + 1$，求其反曲點發生在 $x = \\pm c'$ 時，$c'$ 的平方值為何？"
        sol = f"$f'(x) = 4x^3 - {c*12}x \\implies f''(x) = 12x^2 - {c*12} = 0 \\implies x^2 = {c}$。"
        ans_val = c
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.6: Graphing with Calculus and Technology
sec6_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"使用繪圖軟體繪製函數 $y = x^4 - {a}x^2$ 時，主要可用微積分來精準驗證什麼？"
        ans = "B" if i % 4 == 0 else "C"
        opts = [f"極值與反曲點的精確位置", f"函數連續性", f"定義域", f"圖形的顏色"]
        sol = f"微積分可用來計算精確的極值和反曲點座標。"
    elif i % 3 == 1:
        text = f"使用繪圖科技描繪 $f(x) = x \\sin(x)$，下列何者正確？"
        ans = "D" if i % 4 == 1 else "A"
        opts = [f"圖形在正無窮大時振幅趨近無窮", f"圖形為對稱於 $y$ 軸", f"圖形無任何臨界點", f"圖形為週期函數"]
        sol = f"隨著 $x \\to \\infty$，振幅會被 $x$ 放大，所以振幅趨近於無窮。"
    else:
        text = f"若函數 $f(x) = x^3 - {a}x$ 使用科技繪製，圖形將在 $x$ 大於多少時恆為正？"
        ans = "A" if i % 4 == 2 else "B"
        opts = [f"$\\sqrt{{{a}}}$", f"${a}$", f"$0$", f"$1$"]
        sol = f"$x(x^2 - {a}) > 0 \\implies x > \\sqrt{{{a}}}$。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(31, 51):
    c = i - 16
    if i % 2 == 0:
        text = f"已知 $f(x) = {c}x^2 - 16$，求此曲線與 $x$ 軸正向之截距。"
        sol = f"${c}x^2 = 16 \\implies x = 4/\\sqrt{{{c}}}$（整數化表示，以 ${c}$ 為 1 時答案為 4 舉例）。若 $c=1$，則截距為 $4$。"
        ans_val = round(4 * (c ** -0.5), 2)
        if c == 16:
            ans_val = 1
        elif c == 4:
            ans_val = 2
    else:
        text = f"若函數 $f(x) = x^3 - {c*3}x + k$ 的反曲點 $x$ 座標為 $x_0$，求 $x_0$ 之值。"
        sol = f"$f'(x) = 3x^2 - {c*3} \\implies f''(x) = 6x = 0 \\implies x = 0$。"
        ans_val = 0
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.7: Optimization Problems
sec7_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 3 == 0:
        text = f"欲用長度為 {a*4} 的圍籬圍成一個面積最大的矩形，此最大面積為何？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a*a}$", f"${a*2}$", f"${a*a*4}$", f"$40$"]
        sol = f"正方形面積最大。正方形邊長為 $\\frac{{{a*4}}}{{4}} = {a} \\implies A = {a} \\times {a} = {a*a}$。"
    elif i % 3 == 1:
        text = f"兩正數之和為 {a*2}，欲使兩數乘積最大，此乘積最大值為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*a}$", f"${a*2}$", f"$0$", f"${a*a*4}$"]
        sol = f"當兩正數相等時，乘積最大。故 $x = y = {a} \\implies x y = {a*a}$。"
    else:
        text = f"在最佳化問題中，若目標函數在開區間內僅有一個臨界點且為極小值，則該極小值亦為："
        ans = "A" if i % 4 == 2 else "B"
        opts = [f"絕對極小值", f"絕對極大值", f"不一定", f"極大值"]
        sol = f"只有一個臨界點且為極小值，則為絕對極小值。"
    sec7_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec7_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"若兩正數之和為 {c*2}，求此兩數乘積之最大值。"
        sol = f"$x+y = {c*2} \\implies y = {c*2}-x$。$P(x) = x({c*2}-x) = {c*2}x - x^2 \\implies P'(x) = {c*2}-2x = 0 \\implies x={c}, y={c}$。最大乘積為 ${c*c}$。"
        ans_val = c * c
    else:
        text = f"一矩形之周長為 {c*4}，則其面積最大值為何？"
        sol = f"最大面積時為正方形。邊長為 ${c} \\implies \\text{{面積}} = {c} \\times {c} = {c*c}$。"
        ans_val = c * c
    sec7_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.8: Newton's Method
sec8_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"牛頓法（Newton's Method）的遞迴疊代公式為何？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$x_{{n+1}} = x_n - \\frac{{f(x_n)}}{{f'(x_n)}}$", f"$x_{{n+1}} = x_n + \\frac{{f(x_n)}}{{f'(x_n)}}$", f"$x_{{n+1}} = x_n - \\frac{{f'(x_n)}}{{f(x_n)}}$", f"$x_{{n+1}} = x_n - f(x_n)$"]
        sol = f"牛頓法遞迴式公式為 $x_{{n+1}} = x_n - \\frac{{f(x_n)}}{{f'(x_n)}}$。"
    elif i % 3 == 1:
        text = f"利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"無法繼續進行疊代（分母為 0）", f"收斂速度變快", f"直接收斂到精確根", f"跳轉到另一根"]
        sol = f"當導函數為 0 時分母為 0，疊代無法繼續。"
    else:
        text = f"利用牛頓法求 $x^2 - {a} = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？"
        ans = "A" if i % 4 == 2 else "B"
        opts = [f"${(1+a)/2}$", f"${1-a}$", f"${a}$", f"$2$"]
        sol = f"$f(x) = x^2 - {a}, f'(x) = 2x \\implies x_2 = x_1 - \\frac{{x_1^2 - {a}}}{{2x_1}} = 1 - \\frac{{1 - {a}}}{{2}} = \\frac{{1 + {a}}}{{2}}$。"
    sec8_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec8_fills = []
for i in range(31, 51):
    c = i - 15
    if i % 2 == 0:
        text = f"已知 $f(x) = x^2 - {c}$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。"
        sol = f"$x_2 = 1 - \\frac{{1 - {c}}}{{2}} = \\frac{{1 + {c}}}{{2}}$。"
        ans_val = (1 + c) / 2
    else:
        text = f"已知 $f(x) = x^2 - {c*2-1}$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。"
        sol = f"$x_2 = 1 - \\frac{{1 - ({c*2-1})}}{{2}} = \\frac{{1 + {c*2-1}}}{{2}} = {c}$。"
        ans_val = c
    sec8_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.9: Antiderivatives
sec9_choices = []
for i in range(1, 31):
    a = i + 2
    if i % 3 == 0:
        text = f"求函數 $f(x) = {a}x^2$ 的最一般反導函數。"
        ans = "C" if i % 4 == 0 else "D"
        opts = [f"$\\frac{{{a}}}{{3}}x^3 + C$", f"${a*2}x + C$", f"${a}x^3 + C$", f"$\\frac{{{a}}}{{2}}x^2 + C$"]
        sol = f"對 ${a}x^2$ 進行積分得 $\\frac{{{a}}}{{3}}x^3 + C$。"
    elif i % 3 == 1:
        text = f"求 $f(x) = \\cos x$ 的最一般反導函數。"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"$\\sin x + C$", f"$-\\sin x + C$", f"$\\cos x + C$", f"$-\\cos x + C$"]
        sol = f"$(\\sin x)' = \\cos x \\implies \\sin x + C$。"
    else:
        text = f"求 $f(x) = \\sin x$ 的最一般反導函數。"
        ans = "B" if i % 4 == 2 else "C"
        opts = [f"$-\\cos x + C$", f"$\\cos x + C$", f"$\\sin x + C$", f"$-\\sin x + C$"]
        sol = f"$(-\\cos x)' = \\sin x \\implies -\\cos x + C$。"
    sec9_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec9_fills = []
for i in range(31, 51):
    c = i - 16
    if i % 2 == 0:
        text = f"若 $f(x) = {c}x + 2$，其滿足 $F(0)=0$ 的反導函數為 $F(x) = Ax^2 + Bx$，試求 $A$ 的值為何？"
        sol = f"積分得 $F(x) = \\frac{{{c}}}{{2}}x^2 + 2x + C$。$F(0)=0 \\implies C=0$。故 $A = \\frac{{{c}}}{{2}}$。"
        ans_val = c / 2
    else:
        text = f"求函數 $f(x) = {c*3}x^2$ 的最一般反導函數為 $Ax^3 + C$，求 $A$ 的值為何？"
        sol = f"對 ${c*3}x^2$ 進行積分得 ${c}x^3 + C$，故 $A = {c}$。"
        ans_val = c
    sec9_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# ch3_final: Review
sec_final_choices = []
for i in range(1, 31):
    a = i + 1
    if i % 3 == 0:
        text = f"【綜合】求函數 $f(x) = x^2 - {a*2}x$ 之臨界點為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a}$", f"$-{a}$", f"$0$", f"$1$"]
        sol = f"$f'(x) = 2x - {a*2} = 0 \\implies x = {a}$。"
    elif i % 3 == 1:
        text = f"【綜合】求極限值 $\\lim_{{x \\to \\infty}} \\frac{{{a}x^2 + 1}}{{x^2 + 2}}$。"
        ans = "B" if i % 4 == 1 else "C"
        opts = [f"${a}$", f"$1$", f"$2$", f"$\\infty$"]
        sol = f"最高次方係數比值為 ${a}$。"
    else:
        text = f"【綜合】求 $f(x) = \\cos x$ 的最一般反導函數。"
        ans = "C" if i % 4 == 2 else "D"
        opts = [f"$\\sin x + C$", f"$-\\sin x + C$", f"$\\cos x + C$", f"$-\\cos x + C$"]
        sol = f"積分得 $\\sin x + C$。"
    sec_final_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec_final_fills = []
for i in range(31, 51):
    c = i - 18
    if i % 2 == 0:
        text = f"【綜合】兩正數之和為 {c*2}，求此兩數乘積之最大值。"
        sol = f"最大乘積為正方形，邊長為 $c \\implies c \\times c = {c*c}$。"
        ans_val = c * c
    else:
        text = f"【綜合】求 $f(x) = {c*3}x^2$ 其滿足 $F(0)=0$ 的反導函數之 $x^3$ 項係數。"
        sol = f"對 ${c*3}x^2$ 進行積分得 ${c}x^3 + C$。$F(0)=0 \\implies C=0$。故係數為 ${c}$。"
        ans_val = c
    sec_final_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank/chap_3")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "ch3_sec1.md").write_text(generate_section(3, 1, "最大值與最小值", sec1_choices, sec1_fills), encoding='utf-8')
    (out_dir / "ch3_sec2.md").write_text(generate_section(3, 2, "均值定理", sec2_choices, sec2_fills), encoding='utf-8')
    (out_dir / "ch3_sec3.md").write_text(generate_section(3, 3, "導函數如何告訴我們圖形的形狀", sec3_choices, sec3_fills), encoding='utf-8')
    (out_dir / "ch3_sec4.md").write_text(generate_section(3, 4, "無窮遠處的極限與水平漸近線", sec4_choices, sec4_fills), encoding='utf-8')
    (out_dir / "ch3_sec5.md").write_text(generate_section(3, 5, "曲線描繪摘要", sec5_choices, sec5_fills), encoding='utf-8')
    (out_dir / "ch3_sec6.md").write_text(generate_section(3, 6, "微積分與科技作圖", sec6_choices, sec6_fills), encoding='utf-8')
    (out_dir / "ch3_sec7.md").write_text(generate_section(3, 7, "最佳化問題", sec7_choices, sec7_fills), encoding='utf-8')
    (out_dir / "ch3_sec8.md").write_text(generate_section(3, 8, "牛頓法", sec8_choices, sec8_fills), encoding='utf-8')
    (out_dir / "ch3_sec9.md").write_text(generate_section(3, 9, "反導函數", sec9_choices, sec9_fills), encoding='utf-8')
    
    (out_dir / "ch3_final.md").write_text(generate_review(3, "綜合題目", sec_final_choices, sec_final_fills), encoding='utf-8')
    
    print("All Chapter 3 files and review generated successfully.")
