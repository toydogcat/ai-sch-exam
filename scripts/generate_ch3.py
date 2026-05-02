import os
from pathlib import Path

def generate_section(ch_id, sec_id, title, choice_templates, fill_templates):
    lines = [
        f"# 微積分題庫 - 3.{sec_id} 節：{title}",
        "",
        f"本節收錄 3.{sec_id} 節相關題目。",
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


# 3.1: Maximum and Minimum Values
sec1_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"求函數 $f(x) = x^2 - {a*2}x$ 在所有實數上的絕對極小值（Absolute Minimum）為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"$-{a*a}$", f"$-{a}$", f"$0$", f"${a}$"]
        sol = f"微分得 $f'(x) = 2x - {a*2} = 0 \\implies x={a}$。絕對極小值為 $f({a}) = {a}^2 - {a*2}({a}) = -{a*a}$。"
    else:
        text = f"求函數 $f(x) = {a}x$ 在閉區間 $[0, 2]$ 上的最大值（Absolute Maximum）為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"${a*2}$", f"${a}$", f"$2$", f"$0$"]
        sol = f"閉區間最大值在端點或臨界點。$f'(x)={a} > 0$，故為遞增函數。代入端點 $x=2$ 得最大值 ${a*2}$。"
    sec1_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec1_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"求函數 $f(x) = x^2 - {c*2}x$ 之臨界點（Critical Point）的 $x$ 座標為何？"
    sol = f"臨界點即導函數為 0 之處。$f'(x) = 2x - {c*2} = 0 \\implies x={c}$。"
    ans_val = c
    sec1_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.2: The Mean Value Theorem
sec2_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"已知 $f(x) = x^2$ 在閉區間 $[0, {a}]$ 上滿足均值定理，試問對應的 $c$ 值為何？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a/2}$", f"${a}$", f"$1$", f"${a*2}$"]
        sol = f"根據均值定理：$f'(c) = \\frac{{f({a}) - f(0)}}{{{a} - 0}} = \\frac{{{a*a}}}{{{a}}} = {a}$。又 $f'(x) = 2x \\implies 2c = {a} \\implies c = \\frac{{{a}}}{{2}}$。"
    else:
        text = f"均值定理的先決條件不包含下列哪一項？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"在開區間內為遞增", f"在閉區間 $[a, b]$ 上連續", f"在開區間 $(a, b)$ 上可導", f"區間長度大於 0"]
        sol = f"均值定理之條件僅要求連續與可導，不要求函數在開區間內為遞增。"
    sec2_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec2_fills = []
for i in range(21, 31):
    c = i - 19
    text = f"若 $f(x) = x^2$ 在 $[0, {c*2}]$ 上滿足均值定理，求 $c$ 值為多少？"
    sol = f"均值定理要求 $f'(c) = 2c = \\frac{{{c*2}^2 - 0}}{{{c*2}-0}} = {c*2} \\implies c = {c}$。"
    ans_val = c
    sec2_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.3: What Derivatives Tell Us about the Shape of a Graph
sec3_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"若 $f''(x) > 0$ 在區間內恆成立，則函數圖形在該區間具有何種特徵？"
        ans = "D" if i % 4 == 0 else "C"
        opts = [f"向上凹（Concave Up）", f"向下凹（Concave Down）", f"遞增", f"遞減"]
        sol = f"二階導函數大於 0 代表圖形凹向上（Concave Up）。"
    else:
        text = f"若 $f'(x) < 0$ 在區間內恆成立，則函數圖形在該區間具有何種特徵？"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"遞減（Decreasing）", f"遞增（Increasing）", f"向上凹", f"向下凹"]
        sol = f"一階導函數小於 0 代表函數為遞減（Decreasing）。"
    sec3_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec3_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"已知 $f(x) = {c}x^2 + 4x$，求其二階導函數 $f''(x)$ 之值。"
    sol = f"一階導函數為 $f'(x) = {c*2}x + 4$。二階導函數為 $f''(x) = {c*2}$。"
    ans_val = c * 2
    sec3_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.4: Limits at Infinity; Horizontal Asymptotes
sec4_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求極限值 $\\lim_{{x \\to \\infty}} \\frac{{{a}x^2 + 1}}{{x^2 + 2}}$。"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"${a}$", f"$1$", f"$2$", f"$\\infty$"]
        sol = f"同除以分子分母的最高次方 $x^2$ 得 $\\frac{{{a} + 1/x^2}}{{1 + 2/x^2}} \\to {a}$。"
    else:
        text = f"求函數 $y = \\frac{{{a}x}}{{x - 1}}$ 的水平漸近線（Horizontal Asymptote）。"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$y = {a}$", f"$y = 1$", f"$x = 1$", f"$y = 0$"]
        sol = f"水平漸近線即為 $\\lim_{{x \\to \\infty}} f(x) = \\lim_{{x \\to \\infty}} \\frac{{{a}x}}{{x - 1}} = {a}$。故 $y = {a}$。"
    sec4_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec4_fills = []
for i in range(21, 31):
    c = i - 15
    text = f"求極限值 $\\lim_{{x \\to \\infty}} \\frac{{{c}x^3 + 2x}}{{x^3 + 5}}$。"
    sol = f"當 $x$ 趨向無窮大時，最高次方的係數比值即為極限：${c}$。"
    ans_val = c
    sec4_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.5: Summary of Curve Sketching
sec5_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"要準確描繪曲線，下列何者通常不需特別考慮？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"函數在原點的旋轉對稱", f"定義域與值域", f"漸近線與截距", f"一階及二階導函數的資訊"]
        sol = f"曲線描繪的基本步驟中，不包含原點的旋轉對稱，但通常會考慮定義域、漸近線、一階與二階導函數。"
    else:
        text = f"若函數 $f(x) = x^2 - {a}x$，則此曲線的最低點座標之 $x$ 座標為何？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"$\\frac{{{a}}}{{2}}$", f"${a}$", f"$2$", f"不存在"]
        sol = f"$f'(x) = 2x - {a} = 0 \\implies x = \\frac{{{a}}}{{2}}$。"
    sec5_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec5_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"已知 $f(x) = x^3 - {c*3}x$，求該函數的反曲點（Inflection Point）的 $x$ 座標。"
    sol = f"一階導函數為 $f'(x) = 3x^2 - {c*3}$。二階導函數為 $f''(x) = 6x = 0 \\implies x=0$。"
    ans_val = 0
    sec5_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.6: Graphing with Calculus and Technology
sec6_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"使用繪圖軟體繪製函數 $y = x^4 - {a}x^2$ 時，主要用微積分來驗證什麼？"
        ans = "B" if i % 4 == 0 else "C"
        opts = [f"確認極值與反曲點的精確位置", f"確認函數在某點的切線", f"繪製函數的反函數", f"確認數值計算精度"]
        sol = f"繪圖軟體提供視覺輔助，但微積分能提供極值與反曲點的精確位置來做驗證。"
    else:
        text = f"在微積分中，利用科技輔助繪圖通常最有利於應對何種情境？"
        ans = "D" if i % 4 == 1 else "A"
        opts = [f"高次多項式極值點與根的數值逼近", f"基本線性函數繪製", f"常數函數繪製", f"判斷多項式之定義域"]
        sol = f"科技最適合用來處理複雜函數的數值逼近。"
    sec6_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec6_fills = []
for i in range(21, 31):
    c = i - 16
    text = f"求函數 $f(x) = {c}x^2 - 1$ 與 $x$ 軸之所有正截距的值。"
    sol = f"令 $f(x) = 0 \\implies {c}x^2 = 1 \\implies x = \\frac{{1}}{{\\sqrt{{{c}}}}}$。"
    ans_val = round(c ** -0.5, 2)
    sec6_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.7: Optimization Problems
sec7_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"欲用長度為 {a*4} 的圍籬圍成一個面積最大的矩形，此最大面積為何？"
        ans = "A" if i % 4 == 0 else "B"
        opts = [f"${a*a*4}$", f"${a*a}$", f"${a*2}$", f"$40$"]
        sol = f"周長 $2(x+y) = {a*4} \\implies x+y = {a*2}$。矩形面積最大之條件為正方形：$x = y = {a} \\implies \\text{{最大面積}} = {a} \\times {a} \\times 4$（若算式中考慮正方形邊長為 {a} 時）或考慮 $x=y={a*2/2} = {a} \\implies {a} \\times {a} = {a*a*4}$。"
        opts = [f"${a*a*4}$", f"${a*a}$", f"${a*2}$", f"$40$"]
        sol = f"當周長為 {a*4} 時，矩形邊長相等時面積最大。正方形邊長為 $\\frac{{{a*4}}}{{4}} = {a}$。故最大面積為 ${a} \\times {a} = {a*a}$。"
        ans = "B"
    else:
        text = f"在最佳化問題中，若目標函數在開區間內僅有一個臨界點且為極大值，則該極大值亦為："
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"絕對極大值", f"絕對極小值", f"相對極小值", f"不一定"]
        sol = f"若開區間內僅有一個臨界點且為極大值，則其為絕對極大值（Absolute Maximum）。"
    sec7_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec7_fills = []
for i in range(21, 31):
    c = i - 18
    text = f"若兩正數之和為 {c*2}，求此兩數乘積之最大值。"
    sol = f"設兩數為 $x$ 與 $y$，則 $x+y = {c*2} \\implies y = {c*2}-x$。乘積 $P(x) = x({c*2}-x) = {c*2}x - x^2$。微分 $P'(x) = {c*2}-2x = 0 \\implies x={c}, y={c}$。最大乘積為 ${c} \\times {c} = {c*c}$。"
    ans_val = c * c
    sec7_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.8: Newton's Method
sec8_choices = []
for i in range(1, 21):
    a = i + 1
    if i % 2 == 0:
        text = f"牛頓法的疊代公式為何？"
        ans = "B" if i % 4 == 0 else "A"
        opts = [f"$x_{{n+1}} = x_n - \\frac{{f(x_n)}}{{f'(x_n)}}$", f"$x_{{n+1}} = x_n + \\frac{{f(x_n)}}{{f'(x_n)}}$", f"$x_{{n+1}} = x_n - \\frac{{f'(x_n)}}{{f(x_n)}}$", f"$x_{{n+1}} = x_n - f(x_n)$"]
        sol = f"牛頓法的遞迴式公式為 $x_{{n+1}} = x_n - \\frac{{f(x_n)}}{{f'(x_n)}}$。"
    else:
        text = f"利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？"
        ans = "C" if i % 4 == 1 else "D"
        opts = [f"無法繼續進行疊代（分母為 0）", f"收斂速度變快", f"直接收斂到精確根", f"跳轉到另一根"]
        sol = f"當 $f'(x_n) = 0$ 時，疊代式分母為 0，疊代無法繼續進行。"
    sec8_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec8_fills = []
for i in range(21, 31):
    c = i - 15
    text = f"已知 $f(x) = x^2 - {c}$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。"
    sol = f"$f'(x) = 2x$。疊代式為 $x_2 = x_1 - \\frac{{x_1^2 - {c}}}{{2x_1}} = 1 - \\frac{{1 - {c}}}{{2}} = 1 - \\frac{{1 - {c}}}{{2}} = \\frac{{1 + {c}}}{{2}}$。"
    ans_val = (1 + c) / 2
    sec8_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


# 3.9: Antiderivatives
sec9_choices = []
for i in range(1, 21):
    a = i + 2
    if i % 2 == 0:
        text = f"求函數 $f(x) = {a}x^2$ 的最一般反導函數（Most General Antiderivative）。"
        ans = "C" if i % 4 == 0 else "D"
        opts = [f"$\\frac{{{a}}}{{3}}x^3 + C$", f"${a*2}x + C$", f"${a}x^3 + C$", f"$\\frac{{{a}}}{{2}}x^2 + C$"]
        sol = f"對 ${a}x^2$ 進行積分得 $\\frac{{{a}}}{{3}}x^3 + C$。"
    else:
        text = f"求 $f(x) = \\cos x$ 的最一般反導函數為何？"
        ans = "A" if i % 4 == 1 else "B"
        opts = [f"$\\sin x + C$", f"$-\\sin x + C$", f"$\\cos x + C$", f"$-\\cos x + C$"]
        sol = f"因為 $(\\sin x + C)' = \\cos x$，故反導函數為 $\\sin x + C$。"
    sec9_choices.append(lambda idx, t=text, a=ans, o=opts, s=sol: (t, a, o, s))

sec9_fills = []
for i in range(21, 31):
    c = i - 16
    text = f"若 $f(x) = {c}x + 2$，其滿足 $F(0)=0$ 的反導函數為 $F(x) = Ax^2 + Bx$，試求 $A$ 的值為何？"
    sol = f"反導函數為 $F(x) = \\frac{{{c}}}{{2}}x^2 + 2x + C$。$F(0)=0 \\implies C=0$。故 $A = \\frac{{{c}}}{{2}}$。"
    ans_val = c / 2
    sec9_fills.append(lambda idx, t=text, a=ans_val, s=sol: (t, a, s))


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
    
    print("Chapter 3 sections generated successfully.")
