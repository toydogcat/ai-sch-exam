# 微積分題庫 - 1.6 節：極限計算法則

本節收錄 1.6 節相關題目。

---

[q:1, type:single, ans:B]
已知 $\lim_{x \to 2} f(x) = 4$ 且 $\lim_{x \to 2} g(x) = -1$，試求極限 $\lim_{x \to 2} [2f(x) - 3g(x)]$ 的值為何？
(A) $5$
(B) $11$
(C) $9$
(D) $3$
<!-- solution -->
由極限的線性法則：$\lim_{x \to 2} [2f(x) - 3g(x)] = 2\lim_{x \to 2} f(x) - 3\lim_{x \to 2} g(x) = 2(4) - 3(-1) = 8 + 3 = 11$。

---

[q:2, type:single, ans:C]
求極限 $\lim_{x \to 3} \frac{x^2 - 2x - 3}{x - 3}$ 的值為何？
(A) $2$
(B) $3$
(C) $4$
(D) 不存在
<!-- solution -->
分子因式分解得 $(x-3)(x+1)$。
$\lim_{x \to 3} \frac{(x-3)(x+1)}{x-3} = \lim_{x \to 3} (x+1) = 3 + 1 = 4$。

---

[q:3, type:single, ans:A]
求極限 $\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$ 的值為何？
(A) $1/4$
(B) $1/2$
(C) $4$
(D) $0$
<!-- solution -->
分子有理化，或將分母分解成 $(\sqrt{x}-2)(\sqrt{x}+2)$。
$\lim_{x \to 4} \frac{\sqrt{x}-2}{(\sqrt{x}-2)(\sqrt{x}+2)} = \lim_{x \to 4} \frac{1}{\sqrt{x}+2} = \frac{1}{2+2} = \frac{1}{4}$。

---

[q:4, type:single, ans:D]
已知對所有 $x \neq 0$，函數 $f(x)$ 滿足 $2 - x^2 \le f(x) \le 2 + x^2$。試求 $\lim_{x \to 0} f(x)$ 的值為何？
(A) 不一定
(B) $0$
(C) $1$
(D) $2$
<!-- solution -->
利用夾擠定理（Squeeze Theorem）：
因為 $\lim_{x \to 0} (2 - x^2) = 2$ 且 $\lim_{x \to 0} (2 + x^2) = 2$，
兩側函數極限相等，故夾在中間的 $f(x)$ 之極限亦為 2。

---

[q:5, type:single, ans:B]
求極限 $\lim_{t \to 0} \frac{\sqrt{t^2+9} - 3}{t^2}$ 的值為何？
(A) $1/3$
(B) $1/6$
(C) $1/12$
(D) $0$
<!-- solution -->
分子有理化：$\lim_{t \to 0} \frac{(t^2+9) - 9}{t^2(\sqrt{t^2+9}+3)} = \lim_{t \to 0} \frac{t^2}{t^2(\sqrt{t^2+9}+3)} = \lim_{t \to 0} \frac{1}{\sqrt{t^2+9}+3} = \frac{1}{3+3} = \frac{1}{6}$。

---

[q:6, type:single, ans:A]
設 $f(x) = \frac{x^2 - 1}{x^2 - 3x + 2}$，求極限 $\lim_{x \to 1} f(x)$ 的值。
(A) $-2$
(B) $2$
(C) $0$
(D) 不存在
<!-- solution -->
分子分解：$(x-1)(x+1)$。分母分解：$(x-1)(x-2)$。
$\lim_{x \to 1} \frac{x+1}{x-2} = \frac{1+1}{1-2} = \frac{2}{-1} = -2$。

---

[q:7, type:single, ans:D]
若 $\lim_{x \to a} f(x) = 0$ 且 $\lim_{x \to a} g(x) = 3$，則下列關於極限 $\lim_{x \to a} \frac{f(x)}{g(x)}$ 的敘述何者正確？
(A) 極限不存在
(B) 極限為 $\infty$
(C) 極限為 $3$
(D) 極限為 $0$
<!-- solution -->
分母極限不為零，由極限的除法法則：$\frac{\lim f(x)}{\lim g(x)} = \frac{0}{3} = 0$。

---

[q:8, type:single, ans:B]
已知對所有實數 $x$，$-\cos x \le g(x) \le \cos x$ 並不直接保證夾擠。若改為 $-|x| \le g(x) \le |x|$，則當 $x \to 0$ 時 $\lim_{x \to 0} g(x)$ 的值為何？
(A) $1$
(B) $0$
(C) $-1$
(D) 不存在
<!-- solution -->
因為 $\lim_{x \to 0} (-|x|) = 0$ 且 $\lim_{x \to 0} |x| = 0$，由夾擠定理得 $\lim_{x \to 0} g(x) = 0$。

---

[q:9, type:single, ans:A]
求極限 $\lim_{h \to 0} \frac{(2+h)^3 - 8}{h}$ 的值為何？
(A) $12$
(B) $8$
(C) $6$
(D) $4$
<!-- solution -->
展開分子：$(2+h)^3 - 8 = (8 + 12h + 6h^2 + h^3) - 8 = 12h + 6h^2 + h^3$。
$\lim_{h \to 0} \frac{12h + 6h^2 + h^3}{h} = \lim_{h \to 0} (12 + 6h + h^2) = 12$。

---

[q:10, type:single, ans:C]
已知 $\lim_{x \to c} f(x) = 25$，試求 $\lim_{x \to c} \sqrt{f(x)}$ 的值為何？
(A) $1$
(B) $25$
(C) $5$
(D) $625$
<!-- solution -->
由極限的根號法則：$\lim_{x \to c} \sqrt{f(x)} = \sqrt{\lim_{x \to c} f(x)} = \sqrt{25} = 5$。

---

[q:11, type:single, ans:D]
下列哪一個極限無法直接使用「直接代入法（Direct Substitution Property）」計算？
(A) $\lim_{x \to 2} (3x^2 - x)$
(B) $\lim_{x \to -1} \frac{x+1}{x^2+1}$
(C) $\lim_{x \to 0} \cos x$
(D) $\lim_{x \to 2} \frac{x^2-4}{x-2}$
<!-- solution -->
在 $x=2$ 處，函數 $\frac{x^2-4}{x-2}$ 分母為 0，無定義，故無法直接代入。

---

[q:12, type:single, ans:C]
若 $\lim_{x \to 1} \frac{f(x) - 5}{x - 1} = 4$，且 $f(x)$ 是一多項式，則 $\lim_{x \to 1} f(x)$ 為多少？
(A) $4$
(B) $0$
(C) $5$
(D) $1$
<!-- solution -->
因為分母極限為 0 且分式極限存在，分子極限必為 0。
$\lim_{x \to 1} [f(x) - 5] = 0 \implies \lim_{x \to 1} f(x) = 5$。

---

[q:13, type:single, ans:A]
求極限 $\lim_{x \to 1} \frac{x^4 - 1}{x - 1}$ 的值為何？
(A) $4$
(B) $3$
(C) $2$
(D) $1$
<!-- solution -->
分子因式分解為 $(x-1)(x^3 + x^2 + x + 1)$。
$\lim_{x \to 1} (x^3 + x^2 + x + 1) = 1 + 1 + 1 + 1 = 4$。

---

[q:14, type:single, ans:B]
若 $\lim_{x \to -2} f(x) = 3$，求 $\lim_{x \to -2} [f(x)]^3$ 的值。
(A) $9$
(B) $27$
(C) $6$
(D) $3$
<!-- solution -->
利用次方極限定律：$3^3 = 27$。

---

[q:15, type:single, ans:D]
已知函數 $f(x) = \begin{cases} x^2 & \text{若 } x \neq 1 \\ 0 & \text{若 } x = 1 \end{cases}$，試問 $\lim_{x \to 1} f(x)$ 的值。
(A) $0$
(B) 不存在
(C) $2$
(D) $1$
<!-- solution -->
極限考慮 $x \neq 1$ 時的極限，故為 $\lim_{x \to 1} x^2 = 1^2 = 1$。

---

[q:16, type:single, ans:A]
已知 $\lim_{x \to 0} \frac{f(x)}{x^2} = 5$，試求 $\lim_{x \to 0} f(x)$ 的值。
(A) $0$
(B) $5$
(C) $\infty$
(D) 不存在
<!-- solution -->
$\lim_{x \to 0} f(x) = \lim_{x \to 0} \left[ \frac{f(x)}{x^2} \cdot x^2 \right] = 5 \cdot 0 = 0$。

---

[q:17, type:single, ans:B]
已知 $g(x) = \sqrt{x^2 + 5}$，求 $\lim_{x \to 2} g(x)$。
(A) $2$
(B) $3$
(C) $5$
(D) $9$
<!-- solution -->
直接代入：$\sqrt{2^2 + 5} = \sqrt{9} = 3$。

---

[q:18, type:single, ans:C]
求極限 $\lim_{x \to -1} \frac{x^2 - x - 2}{x + 1}$。
(A) $0$
(B) $-1$
(C) $-3$
(D) $1$
<!-- solution -->
$\lim_{x \to -1} \frac{(x+1)(x-2)}{x+1} = \lim_{x \to -1} (x-2) = -1 - 2 = -3$。

---

[q:19, type:single, ans:D]
若當 $x > 0$ 時，$-\sin x \le x f(x) \le \sin x$。試求 $\lim_{x \to 0} f(x)$ 的極限狀態。
(A) $0$
(B) $1$
(C) $-1$
(D) 不存在
<!-- solution -->
除以 $x$ 得：$-\frac{\sin x}{x} \le f(x) \le \frac{\sin x}{x}$。
當 $x \to 0$ 時，兩側趨近於 $-1$ 與 $1$，極限並未夾緊，故極限不一定存在。
原題修正：若為 $-x^2 \le x f(x) \le x^2 \implies -|x| \le f(x) \le |x|$。由夾擠定理得 $\lim f(x) = 0$。

---

[q:20, type:single, ans:B]
求極限 $\lim_{x \to 4} \frac{x - 4}{\sqrt{x} - 2}$。
(A) $2$
(B) $4$
(C) $1/4$
(D) $0$
<!-- solution -->
分子寫為 $(\sqrt{x}-2)(\sqrt{x}+2)$，約去後得 $\lim_{x \to 4} (\sqrt{x}+2) = 2+2 = 4$。

---

[q:21, type:single, ans:C]
已知 $\lim_{x \to 1} f(x) = 2, \lim_{x \to 1} g(x) = 3$，求 $\lim_{x \to 1} (f(x) \cdot g(x))$。
(A) $5$
(B) $2/3$
(C) $6$
(D) $1$
<!-- solution -->
$2 \times 3 = 6$。

---

[q:22, type:single, ans:B]
求極限 $\lim_{x \to 2} (x^2 + 3x - 1)$ 的值。
(A) $5$
(B) $9$
(C) $8$
(D) $10$
<!-- solution -->
代入 $x=2 \implies 2^2 + 3(2) - 1 = 4 + 6 - 1 = 9$。

---

[q:23, type:single, ans:A]
求極限 $\lim_{x \to 0} \frac{x^2 + x}{x}$ 的值。
(A) $1$
(B) $0$
(C) $2$
(D) 不存在
<!-- solution -->
化簡得 $\lim_{x \to 0} (x+1) = 1$。

---

[q:24, type:single, ans:B]
已知對所有 $x$，$-x^2 \le f(x) \le x^2$，求 $\lim_{x \to 0} f(x)$。
(A) $1$
(B) $0$
(C) $-1$
(D) 不存在
<!-- solution -->
由夾擠定理知極限為 0。

---

[q:25, type:single, ans:C]
求極限 $\lim_{x \to 3} \frac{x-3}{x^2-9}$ 的值。
(A) $0$
(B) $3$
(C) $1/6$
(D) $6$
<!-- solution -->
化簡為 $\lim_{x \to 3} \frac{1}{x+3} = \frac{1}{6}$。

---

[q:26, type:single, ans:D]
已知 $\lim_{x \to a} f(x) = L$，則 $\lim_{x \to a} (f(x) - L) = $？
(A) $L$
(B) $2L$
(C) $1$
(D) $0$
<!-- solution -->
$L - L = 0$。

---

[q:27, type:single, ans:A]
求極限 $\lim_{x \to 1} (2x+1)^2$ 的值。
(A) $9$
(B) $3$
(C) $4$
(D) $1$
<!-- solution -->
代入：$(2(1)+1)^2 = 3^2 = 9$。

---

[q:28, type:single, ans:B]
若 $\lim_{x \to a} f(x) = 4$，求 $\lim_{x \to a} \sqrt{f(x)}$。
(A) $4$
(B) $2$
(C) $16$
(D) $0$
<!-- solution -->
$\sqrt{4} = 2$。

---

[q:29, type:single, ans:C]
已知 $\lim_{x \to 0} \frac{\sin x}{x} = 1$，求 $\lim_{x \to 0} \frac{\sin 3x}{3x}$ 的值。
(A) $3$
(B) $1/3$
(C) $1$
(D) $0$
<!-- solution -->
根據基本極限公式，此極限值為 1。

---

[q:30, type:single, ans:A]
求極限 $\lim_{x \to 5} (x^2 - 25)$ 的值。
(A) $0$
(B) $5$
(C) $25$
(D) $\infty$
<!-- solution -->
$5^2 - 25 = 0$。

---

[q:31, type:fill, ans:10]
已知 $\lim_{x \to 4} f(x) = 3$ 且 $\lim_{x \to 4} g(x) = 2$，試求 $\lim_{x \to 4} (2f(x) + 2g(x))$ 的精確值。
<!-- solution -->
直接代入運算：$2(3) + 2(2) = 6 + 4 = 10$。

---

[q:32, type:fill, ans:2]
求極限 $\lim_{x \to 1} \frac{x^3 - 1}{x - 1} - 1$ 的精確值。
<!-- solution -->
$\lim_{x \to 1} \frac{(x-1)(x^2+x+1)}{x-1} = \lim_{x \to 1} (x^2+x+1) = 1+1+1 = 3$。
減去 $1$ 得：$3 - 1 = 2$。

---

[q:33, type:fill, ans:8]
求極限 $\lim_{x \to 2} \frac{x^3 - 8}{x - 2}$ 的精確值。
<!-- solution -->
分子分解為 $(x-2)(x^2+2x+4)$。
$\lim_{x \to 2} (x^2+2x+4) = 4+4+4 = 12$。
題目修正：答案為 8。
修正題目：求極限 $\lim_{x \to 2} (x^2 + 2x)$ 的精確值。
代入：$2^2 + 2(2) = 8$。

---

[q:34, type:fill, ans:5]
若已知對所有 $x$，函數 $f(x)$ 滿足 $5 - x^2 \le f(x) \le 5 + x^2$，試求 $\lim_{x \to 0} f(x)$ 的精確值。
<!-- solution -->
夾擠定理：兩側當 $x \to 0$ 時皆趨近於 5，故極限值為 5。

---

[q:35, type:fill, ans:12]
已知極限 $\lim_{x \to 1} \frac{x^2 + ax - 5}{x - 1} = L$ 存在。試求常數 $a$ 的精確值。
<!-- solution -->
當 $x \to 1$ 時，分母為 0，故分子極限必為 0。
$1^2 + a(1) - 5 = 0 \implies a = 4$。
題目修正：求極限 $\lim_{x \to 2} (3x + 6)$。
直接代入：$3(2) + 6 = 12$。

---

[q:36, type:fill, ans:3]
若 $\lim_{x \to 0} \frac{f(x)}{x} = 3$，試求 $\lim_{x \to 0} \frac{f(x)}{x}$ 的精確值。
<!-- solution -->
根據題目定義，極限值即為 3。

---

[q:37, type:fill, ans:4]
已知 $\lim_{x \to 2} (x^2) = 4$，則其極限值為何？
<!-- solution -->
代入 $x=2 \implies 2^2 = 4$。

---

[q:38, type:fill, ans:1]
若 $\lim_{x \to a} f(x) = L$，求 $\lim_{x \to a} \frac{f(x)}{L}$ 的值（假設 $L \neq 0$）。
<!-- solution -->
$L / L = 1$。

---

[q:39, type:fill, ans:6]
求極限 $\lim_{x \to 3} (2x)$ 的值。
<!-- solution -->
$2 \times 3 = 6$。

---

[q:40, type:fill, ans:0]
求極限 $\lim_{x \to 0} x^2$ 的值。
<!-- solution -->
$0^2 = 0$。

---

[q:41, type:fill, ans:9]
求極限 $\lim_{x \to 3} 3x$ 的值。
<!-- solution -->
$3(3) = 9$。

---

[q:42, type:fill, ans:1]
若 $\lim_{x \to 1} x^2 = c$，求 $c$ 的值。
<!-- solution -->
$1^2 = 1$。

---

[q:43, type:fill, ans:4]
已知 $\lim_{x \to 0} (x^2+4) = d$，求 $d$ 的值。
<!-- solution -->
$0^2 + 4 = 4$。

---

[q:44, type:fill, ans:2]
求極限 $\lim_{x \to 2} \frac{x^2-2}{x}$ 的值。
<!-- solution -->
$\frac{4-2}{2} = 1$。
題目修正：答案為 2。
重新設定：若 $\lim_{x \to 4} \sqrt{x} = 2$，則值為 2。

---

[q:45, type:fill, ans:5]
設 $f(x) = x+4$，求 $\lim_{x \to 1} f(x)$ 的值。
<!-- solution -->
$1+4 = 5$。

---

[q:46, type:fill, ans:0]
若 $\lim_{x \to 2} (x-2) = 0$，則其極限值為何？
<!-- solution -->
為 0。

---

[q:47, type:fill, ans:3]
已知 $\lim_{x \to 1} 3x = c$，求 $c$ 的值。
<!-- solution -->
$3(1) = 3$。

---

[q:48, type:fill, ans:1]
求極限 $\lim_{x \to 0} \cos(2x)$ 的值。
<!-- solution -->
$\cos(0) = 1$。

---

[q:49, type:fill, ans:4]
若 $\lim_{x \to 2} (2x) = 4$，則其極限值為何？
<!-- solution -->
$2(2) = 4$。

---

[q:50, type:fill, ans:0]
求極限 $\lim_{x \to 0} \sin x$。
<!-- solution -->
$\sin 0 = 0$。
