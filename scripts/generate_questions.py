import os
from pathlib import Path

def gen_ch0_sec1():
    # Algebra and Arithmetic: 20 choice + 10 fill
    lines = [
        "# 微積分題庫 - 0.1 節：代數與算術基礎",
        "",
        "本節收錄 0.1 節相關題目。",
        ""
    ]
    
    # 20 Single Choice Questions
    for i in range(1, 21):
        # vary the numbers
        a = i + 1
        b = i * 2
        correct = (a * b) - i
        ans = "A"
        if i % 4 == 0: ans = "A"
        elif i % 4 == 1: ans = "B"
        elif i % 4 == 2: ans = "C"
        else: ans = "D"
        
        # provide some actual math content variations
        if i % 3 == 0:
            text = f"化簡代數式 $x^{{{a}}} \\cdot x^{{{b}}} / x^{{{i}}}$ 的結果為何？"
            opts = [f"$x^{{{a+b-i}}}$", f"$x^{{{a+b+i}}}$", f"$x^{{{a*b-i}}}$", f"$x^{{{a*b+i}}}$"]
            sol = f"利用指數律：$x^{{{a}}} \\cdot x^{{{b}}} / x^{{{i}}} = x^{{{a}+{b}-{i}}} = x^{{{a+b-i}}}$。"
        elif i % 3 == 1:
            text = f"已知 $f(x) = {a}x + {b}$，試問 $f({i})$ 的值為下列何者？"
            val = a * i + b
            opts = [f"${val - 2}$", f"${val}$", f"${val + 2}$", f"${val * 2}$"]
            sol = f"直接將 $x={i}$ 代入：$f({i}) = {a}({i}) + {b} = {val}$。"
        else:
            text = f"若 $x^2 - {a*a} = 0$，則 $x$ 的可能值為下列何者？"
            opts = [f"${a}$", f"$-{a}$", f"$\\pm {a}$", f"$\\pm {a*a}$"]
            sol = f"利用平方差公式：$x^2 - {a*a} = (x-{a})(x+{a}) = 0 \\implies x = \\pm {a}$。"
            
        # Match options with the correct answer label
        options_formatted = []
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        
        # swap correct option to its place
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        
        for idx, lbl in enumerate(labels):
            options_formatted.append(f"({lbl}) {opts[idx]}")
            
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:single, ans:{ans}]")
        lines.append(text)
        for opt in options_formatted:
            lines.append(opt)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    # 10 Fill-In Questions
    for i in range(21, 31):
        c = i - 15
        d = i + 2
        ans_val = c + d
        text = f"化簡多項式 $(x+{c})(x+{d}) - x^2$，並求其 $x$ 項之係數為何？"
        sol = f"展開原式：$(x^2 + {c+d}x + {c*d}) - x^2 = {c+d}x + {c*d}$。因此 $x$ 項係數為 {c+d}。"
        
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{ans_val}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    return "\n".join(lines)


def gen_ch0_sec2():
    # Geometry and Trigonometry: 20 choice + 10 fill
    lines = [
        "# 微積分題庫 - 0.2 節：幾何與三角函數",
        "",
        "本節收錄 0.2 節相關題目。",
        ""
    ]
    
    # 20 Single Choice Questions
    for i in range(1, 21):
        a = i * 2
        ans = "A"
        if i % 4 == 0: ans = "B"
        elif i % 4 == 1: ans = "C"
        elif i % 4 == 2: ans = "D"
        else: ans = "A"
        
        if i % 3 == 0:
            text = f"若一個圓的半徑為 ${i}$，試問其面積為何？"
            opts = [f"${i*i}\\pi$", f"${i*2}\\pi$", f"${i}\\pi$", f"${i*i*i}\\pi$"]
            sol = f"圓面積公式為 $A = \\pi r^2$。代入 $r={i} \\implies {i*i}\\pi$。"
        elif i % 3 == 1:
            text = f"設 $\\theta = {a*15}^\\circ$，試問換算為弧度（Radian）後的值為何？"
            val = round((a * 15) / 180, 2)
            opts = [f"${val}\\pi$", f"${val*2}\\pi$", f"${val+1}\\pi$", f"${val-0.5}\\pi$"]
            sol = f"角度轉弧度公式為 $\\theta \\times \\frac{{\\pi}}{{180}}$。代入：${a*15}^\\circ \\times \\frac{{\\pi}}{{180}} = {val}\\pi$。"
        else:
            text = f"若 $\\sin \\theta = 0.6$，且 $\\theta$ 在第一象限，試問 $\\cos \\theta$ 的值為多少？"
            opts = [f"$0.8$", f"$0.4$", f"$0.2$", f"$0.6$"]
            sol = f"由 $\\sin^2 \\theta + \\cos^2 \\theta = 1$ 可知：$\\cos \\theta = \\sqrt{{1 - 0.6^2}} = \\sqrt{{0.64}} = 0.8$。"
            
        options_formatted = []
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        
        for idx, lbl in enumerate(labels):
            options_formatted.append(f"({lbl}) {opts[idx]}")
            
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:single, ans:{ans}]")
        lines.append(text)
        for opt in options_formatted:
            lines.append(opt)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    # 10 Fill-In Questions
    for i in range(21, 31):
        r = i - 18
        ans_val = r * r
        text = f"若一個圓的半徑為 ${r}$，試求其面積除以 $\\pi$ 後的精確值為多少？"
        sol = f"圓面積為 $\\pi r^2 = {r*r}\\pi$。除以 $\\pi$ 後為 {r*r}。"
        
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{ans_val}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    return "\n".join(lines)


def gen_ch1_sec1():
    # Functions and Their Representations: 20 choice + 10 fill
    lines = [
        "# 微積分題庫 - 1.1 節：函數及其表示法",
        "",
        "本節收錄 1.1 節相關題目。",
        ""
    ]
    
    # 20 Single Choice Questions
    for i in range(1, 21):
        ans = "C"
        if i % 4 == 0: ans = "D"
        elif i % 4 == 1: ans = "C"
        elif i % 4 == 2: ans = "B"
        else: ans = "A"
        
        if i % 3 == 0:
            text = f"求函數 $f(x) = \\sqrt{{x - {i}}}$ 的定義域為何？"
            opts = [f"$[{i}, \\infty)$", f"$({i}, \\infty)$", f"$(-\\infty, {i}]$", f"$\\mathbb{{R}}$"]
            sol = f"根號內部不可為負數，故 $x - {i} \\geq 0 \\implies x \\geq {i}$，即 $[{i}, \\infty)$。"
        elif i % 3 == 1:
            text = f"已知 $f(x) = {i}x^2 + 2$，試問此函數在 $y$ 軸上的截距為何？"
            opts = [f"$2$", f"${i}$", f"${i+2}$", f"$0$"]
            sol = f"截距即為 $x=0$ 時的函數值：$f(0) = {i}(0)^2 + 2 = 2$。"
        else:
            text = f"下列哪一個函數的對稱軸為 $y$ 軸（即偶函數）？"
            opts = [f"$f(x) = x^{{{i*2}}}$", f"$f(x) = x^{{{i*2+1}}}$", f"$f(x) = x + {i}$", f"$f(x) = \\sin(x)$"]
            sol = f"偶函數滿足 $f(-x) = f(x)$。若最高次方為偶數 $2n$，則對應為偶函數。"
            
        options_formatted = []
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        
        for idx, lbl in enumerate(labels):
            options_formatted.append(f"({lbl}) {opts[idx]}")
            
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:single, ans:{ans}]")
        lines.append(text)
        for opt in options_formatted:
            lines.append(opt)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    # 10 Fill-In Questions
    for i in range(21, 31):
        val = i * 2
        text = f"已知 $f(x) = 3x - 1$，試求當 $x = {i}$ 時，$f(x)$ 的精確函數值為何？"
        sol = f"直接代入 $x={i} \\implies 3({i}) - 1 = {3*i-1}$。"
        
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{3*i-1}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    return "\n".join(lines)


def gen_ch1_sec2():
    # Limit of a Function: 20 choice + 10 fill
    lines = [
        "# 微積分題庫 - 1.2 節：極限的概念與計算",
        "",
        "本節收錄 1.2 節相關題目。",
        ""
    ]
    
    # 20 Single Choice Questions
    for i in range(1, 21):
        ans = "B"
        if i % 4 == 0: ans = "B"
        elif i % 4 == 1: ans = "A"
        elif i % 4 == 2: ans = "D"
        else: ans = "C"
        
        if i % 3 == 0:
            text = f"求極限值 $\\lim_{{x \\to {i}}} ({i}x + 1)$。"
            val = i * i + 1
            opts = [f"${val}$", f"${val-2}$", f"${val+3}$", f"${val*2}$"]
            sol = f"直接將 $x={i}$ 代入：${i}({i}) + 1 = {val}$。"
        elif i % 3 == 1:
            text = f"求極限值 $\\lim_{{x \\to {i}}} \\frac{{x^2 - {i*i}}}{{x - {i}}}$。"
            val = i * 2
            opts = [f"${val}$", f"${i}$", f"${i*i}$", f"不存在"]
            sol = f"因式分解分子：$\\lim_{{x \\to {i}}} \\frac{{(x-{i})(x+{i})}}{{x-{i}}} = \\lim_{{x \\to {i}}} (x+{i}) = {val}$。"
        else:
            text = f"已知極限 $\\lim_{{x \\to {i}}} \\frac{{k}}{{x}} = 2$，試問常數 $k$ 的值為何？"
            val = i * 2
            opts = [f"${val}$", f"${i}$", f"${val+1}$", f"${val-1}$"]
            sol = f"代入極限：$\\frac{{k}}{{{i}}} = 2 \\implies k = {val}$。"
            
        options_formatted = []
        labels = ["A", "B", "C", "D"]
        correct_idx = labels.index(ans)
        opts[0], opts[correct_idx] = opts[correct_idx], opts[0]
        
        for idx, lbl in enumerate(labels):
            options_formatted.append(f"({lbl}) {opts[idx]}")
            
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:single, ans:{ans}]")
        lines.append(text)
        for opt in options_formatted:
            lines.append(opt)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    # 10 Fill-In Questions
    for i in range(21, 31):
        val = i + 1
        text = f"求極限值 $\\lim_{{x \\to {i}}} (x^2 - 1)$。"
        sol = f"直接代入 $x={i} \\implies {i}^2 - 1 = {i*i-1}$。"
        
        lines.append(f"---")
        lines.append("")
        lines.append(f"[q:{i}, type:fill, ans:{i*i-1}]")
        lines.append(text)
        lines.append("<!-- solution -->")
        lines.append(sol)
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    out_dir = Path("/home/toymsi/documents/examination/Github/ai-sch-exam/calculus_bank")
    (out_dir / "chap_0").mkdir(parents=True, exist_ok=True)
    (out_dir / "chap_1").mkdir(parents=True, exist_ok=True)
    
    # Write files
    (out_dir / "chap_0" / "ch0_sec1.md").write_text(gen_ch0_sec1(), encoding='utf-8')
    (out_dir / "chap_0" / "ch0_sec2.md").write_text(gen_ch0_sec2(), encoding='utf-8')
    (out_dir / "chap_1" / "ch1_sec1.md").write_text(gen_ch1_sec1(), encoding='utf-8')
    (out_dir / "chap_1" / "ch1_sec2.md").write_text(gen_ch1_sec2(), encoding='utf-8')
    
    print("Files successfully generated.")
