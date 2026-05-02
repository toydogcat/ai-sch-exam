# 微積分題庫 - 第一章綜合測驗 (Chapter 1 Review)

本節收錄第一章所有主題的綜合題目。

---

[q:1, type:single, ans:B]
已知 $f(x) = \sqrt{x+1}$ 且 $g(x) = x^2 - 1$，試問複合函數 $(f \circ g)(x)$ 的定義域為何？
(A) $(-\infty, \infty)$
(B) $\{x \in \mathbb{R} \mid x \ge 0 \text{ 或 } x \le 0\} = \mathbb{R}$
(C) $[0, \infty)$
(D) $[1, \infty)$
<!-- solution -->
$(f \circ g)(x) = f(g(x)) = f(x^2 - 1) = \sqrt{(x^2 - 1) + 1} = \sqrt{x^2} = |x|$。
因為 $x^2 \ge 0$ 對所有實數皆成立，故定義域為全體實數 $\mathbb{R}$。

---

[q:2, type:single, ans:A]
求極限 $\lim_{x \to 2} \frac{x^2 + x - 6}{x - 2}$ 的值。
(A) $5$
(B) $1$
(C) $3$
(D) 不存在
<!-- solution -->
分子因式分解得 $(x-2)(x+3)$。
$\lim_{x \to 2} \frac{(x-2)(x+3)}{x-2} = \lim_{x \to 2} (x+3) = 2 + 3 = 5$。

---

[q:3, type:single, ans:D]
根據中間值定理（IVT），方程式 $x^3 - 3x + 1 = 0$ 在下列哪一個區間內必有實根？
(A) $(2, 3)$
(B) $(-1, 0)$
(C) $(1, 2)$
(D) $(0, 1)$
<!-- solution -->
令 $f(x) = x^3 - 3x + 1$。
$f(0) = 1 > 0$。
$f(1) = 1 - 3 + 1 = -1 < 0$。
因為 $f(0) \cdot f(1) < 0$，由中間值定理知在區間 $(0, 1)$ 內必有實根。

---

[q:4, type:single, ans:B]
若 $\lim_{x \to 1} \frac{f(x) - 4}{x - 1} = 2$，則下列關於 $f(x)$ 的極限敘述何者正確？
(A) $\lim_{x \to 1} f(x) = 2$
(B) $\lim_{x \to 1} f(x) = 4$
(C) $\lim_{x \to 1} f(x) = 0$
(D) 不存在
<!-- solution -->
分體極限為 0 且分式極限存在，故分子極限必為 0：$\lim_{x \to 1} [f(x) - 4] = 0 \implies \lim_{x \to 1} f(x) = 4$。

---

[q:5, type:single, ans:C]
已知在證明 $\lim_{x \to 4} (3x - 2) = 10$ 時，給定 $\epsilon > 0$，我們應該選取 $\delta$ 為多少？
(A) $\epsilon$
(B) $3\epsilon$
(C) $\epsilon/3$
(D) $\epsilon/2$
<!-- solution -->
$|3x - 2 - 10| = |3x - 12| = 3|x - 4| < \epsilon \implies |x - 4| < \frac{\epsilon}{3}$。故選取 $\delta = \frac{\epsilon}{3}$。

---

[q:6, type:single, ans:B]
求極限 $\lim_{x \to 0} \frac{\sqrt{x+4} - 2}{x}$ 的值。
(A) $1/2$
(B) $1/4$
(C) $1$
(D) $0$
<!-- solution -->
分子有理化：$\lim_{x \to 0} \frac{x+4-4}{x(\sqrt{x+4}+2)} = \lim_{x \to 0} \frac{1}{\sqrt{x+4}+2} = \frac{1}{2+2} = \frac{1}{4}$。

---

[q:7, type:single, ans:A]
下列哪一個函數在其整個定義域內皆為連續函數？
(A) $f(x) = x^2 - \cos x$
(B) $f(x) = \frac{1}{x}$
(C) $f(x) = \tan x$
(D) $f(x) = \frac{x^2-1}{x-1}$
<!-- solution -->
(A) 多項式與餘弦函數在全體實數上皆為連續函數，故其相減亦連續。

---

[q:8, type:single, ans:C]
設 $f(x) = \begin{cases} x^2 - c & \text{若 } x \le 3 \\ 2x + 1 & \text{若 } x > 3 \end{cases}$ 為全體實數上的連續函數，試求常數 $c$ 的值。
(A) $4$
(B) $3$
(C) $2$
(D) $1$
<!-- solution -->
在 $x=3$ 處，左極限與右極限需相等。
左極限：$3^2 - c = 9 - c$。
右極限：$2(3) + 1 = 7$。
令 $9 - c = 7 \implies c = 2$。

---

[q:9, type:single, ans:D]
已知函數 $f(x) = |x - 2|$，試問此函數在 $x = 2$ 處的狀態為何？
(A) 不連續
(B) 連續且可微
(C) 既不連續也不可微
(D) 連續但不可微
<!-- solution -->
$\lim_{x \to 2} |x - 2| = 0 = f(2)$，故連續。但在該點左導數與右導數不相等，故不可微。

---

[q:10, type:single, ans:A]
求極限 $\lim_{x \to 0} x^2 \sin\left(\frac{1}{x}\right)$ 的值。
(A) $0$
(B) $1$
(C) $-1$
(D) 不存在
<!-- solution -->
夾擠定理：因為 $-1 \le \sin\left(\frac{1}{x}\right) \le 1 \implies -x^2 \le x^2 \sin\left(\frac{1}{x}\right) \le x^2$。當 $x \to 0$ 時，兩側皆趨近於 0。

---

[q:11, type:single, ans:B]
已知 $f(x) = \frac{1}{x-1}$，試問此函數在 $x = 1$ 處屬於何種不連續點？
(A) 可去不連續點
(B) 無窮不連續點
(C) 跳躍不連續點
(D) 連續點
<!-- solution -->
當 $x \to 1$ 時，函數值趨近於 $\pm \infty$，此為無窮不連續點（此處有垂直漸近線）。

---

[q:12, type:single, ans:D]
求極限 $\lim_{x \to \infty} \frac{3x^2 + 2x - 1}{x^2 + x - 5}$。
(A) $1$
(B) $0$
(C) $\infty$
(D) $3$
<!-- solution -->
最高次方項係數比：$\frac{3}{1} = 3$。

---

[q:13, type:single, ans:B]
已知 $f(x) = \frac{x}{x+2}$，試求反函數 $f^{-1}(x)$ 的解析式。
(A) $\frac{2x}{x-1}$
(B) $\frac{2x}{1-x}$
(C) $\frac{x+2}{x}$
(D) $\frac{1-x}{2x}$
<!-- solution -->
令 $y = \frac{x}{x+2} \implies y(x+2) = x \implies xy + 2y = x \implies x(y-1) = -2y \implies x = \frac{2y}{1-y}$。
故反函數為 $f^{-1}(x) = \frac{2x}{1-x}$。

---

[q:14, type:single, ans:A]
設 $\lim_{x \to a} f(x) = 2$ 且 $\lim_{x \to a} g(x) = -1$，求 $\lim_{x \to a} [f(x) \cdot g(x) + 3]$ 的值。
(A) $1$
(B) $-1$
(C) $2$
(D) $5$
<!-- solution -->
極限乘法與加法定律：$2 \times (-1) + 3 = -2 + 3 = 1$。

---

[q:15, type:single, ans:C]
已知函數 $f(x) = \frac{x^2 - 1}{x^2 - 3x + 2}$，試問其所有不連續點為何？
(A) $x = 1$
(B) $x = 2$
(C) $x = 1$ 與 $x = 2$
(D) 全體實數上皆連續
<!-- solution -->
令分母為 0：$x^2 - 3x + 2 = 0 \implies (x-1)(x-2) = 0 \implies x = 1 \text{ 或 } x = 2$。

---

[q:16, type:single, ans:D]
若將函數 $y = f(x)$ 圖形向右平移 2 個單位，再向上平移 1 個單位，新圖形的方程式為何？
(A) $y = f(x+2) + 1$
(B) $y = f(x+2) - 1$
(C) $y = f(x-2) - 1$
(D) $y = f(x-2) + 1$
<!-- solution -->
向右平移 2 單位將 $x$ 替換為 $x - 2$，向上平移 1 單位加 1，得 $y = f(x-2) + 1$。

---

[q:17, type:single, ans:B]
求極限 $\lim_{x \to 1^+} \frac{x-2}{x-1}$ 的值。
(A) $\infty$
(B) $-\infty$
(C) $0$
(D) 不存在
<!-- solution -->
當 $x \to 1^+$ 時，分子趨近於 $-1$，分母為趨近於 0 的正數。負數除以趨近於 0 的正數趨近於 $-\infty$。

---

[q:18, type:single, ans:A]
已知曲線 $y = 2x^2 + 1$，試求其在 $x = 1$ 處的切線斜率。
(A) $4$
(B) $2$
(C) $1$
(D) $0$
<!-- solution -->
切線斜率為 $y'(1) = 4(1) = 4$。

---

[q:19, type:single, ans:B]
在證明 $\lim_{x \to 2} x = 2$ 時，對任意給定的 $\epsilon > 0$，我們最大可選取 $\delta$ 為何？
(A) $\epsilon/2$
(B) $\epsilon$
(C) $2\epsilon$
(D) $1$
<!-- solution -->
$|x - 2| < \epsilon$。故選取 $\delta = \epsilon$。

---

[q:20, type:single, ans:C]
下列哪一個極限是不存在的？
(A) $\lim_{x \to 0} x \cos\left(\frac{1}{x}\right)$
(B) $\lim_{x \to 0} \frac{\sin x}{x}$
(C) $\lim_{x \to 0} \frac{1}{x}$
(D) $\lim_{x \to \infty} \frac{1}{x}$
<!-- solution -->
當 $x \to 0^-$ 時為 $-\infty$，當 $x \to 0^+$ 時為 $\infty$，故極限不存在。

---

[q:21, type:single, ans:A]
已知 $f(x) = x+3$，求 $\lim_{x \to 1} f(x)$ 的值。
(A) $4$
(B) $1$
(C) $2$
(D) $0$
<!-- solution -->
直接代入：$1+3 = 4$。

---

[q:22, type:single, ans:C]
求極限 $\lim_{x \to 0} \cos x$ 的值。
(A) $0$
(B) 不存在
(C) $1$
(D) $\infty$
<!-- solution -->
$\cos 0 = 1$。

---

[q:23, type:single, ans:D]
若 $\lim_{x \to a} f(x) = 4, \lim_{x \to a} g(x) = 1$，求 $\lim_{x \to a} (f(x) - g(x))$。
(A) $1$
(B) $5$
(C) $0$
(D) $3$
<!-- solution -->
$4 - 1 = 3$。

---

[q:24, type:single, ans:A]
已知 $f(x) = 3x$，求 $\lim_{x \to 2} f(x)$。
(A) $6$
(B) $2$
(C) $3$
(D) $5$
<!-- solution -->
$3(2) = 6$。

---

[q:25, type:single, ans:B]
求 $\lim_{x \to 2} \frac{x^2}{2}$。
(A) $1$
(B) $2$
(C) $4$
(D) $0$
<!-- solution -->
$2^2 / 2 = 2$。

---

[q:26, type:single, ans:A]
已知 $f(x) = x^2 - 1$，當 $x \to 2$ 時極限為：
(A) $3$
(B) $1$
(C) $4$
(D) $0$
<!-- solution -->
$2^2 - 1 = 3$。

---

[q:27, type:single, ans:D]
若 $\lim_{x \to a} (x+1) = 5$，則 $a = $？
(A) $1$
(B) $2$
(C) $3$
(D) $4$
<!-- solution -->
$a+1 = 5 \implies a=4$。

---

[q:28, type:single, ans:B]
求極限 $\lim_{x \to 1} \frac{x-1}{x^2-1}$。
(A) $1$
(B) $1/2$
(C) $0$
(D) $2$
<!-- solution -->
化簡為 $1/(x+1) \implies 1/2$。

---

[q:29, type:single, ans:C]
已知 $f(x) = \sqrt{x+4}$，求 $\lim_{x \to 0} f(x)$ 的值。
(A) $4$
(B) $0$
(C) $2$
(D) $1$
<!-- solution -->
$\sqrt{0+4} = 2$。

---

[q:30, type:single, ans:A]
求極限 $\lim_{x \to 0} \frac{x^2+2x}{x}$ 的值。
(A) $2$
(B) $0$
(C) $1$
(D) 不存在
<!-- solution -->
化簡為 $x+2 \implies 0+2 = 2$。

---

[q:31, type:fill, ans:7]
已知函數 $f(x) = ax + 3$。若 $f(2) = 11$，試求 $f(1)$ 的精確值。
<!-- solution -->
代入 $f(2) \implies 11 = 2a + 3 \implies 2a = 8 \implies a = 4$。
故 $f(x) = 4x + 3 \implies f(1) = 4(1) + 3 = 7$。

---

[q:32, type:fill, ans:4]
求極限 $\lim_{x \to 3} \frac{x^2 - 9}{x - 3} - 2$ 的精確值。
<!-- solution -->
$\lim_{x \to 3} \frac{(x-3)(x+3)}{x-3} = \lim_{x \to 3} (x+3) = 6$。
減去 $2$ 得：$6 - 2 = 4$。

---

[q:33, type:fill, ans:2]
已知 $f(x) = \begin{cases} x^2 + c & \text{若 } x \neq 2 \\ 6 & \text{若 } x = 2 \end{cases}$ 為連續函數，試求常數 $c$ 的值。
<!-- solution -->
$\lim_{x \to 2} f(x) = \lim_{x \to 2} (x^2 + c) = 4 + c$。
令 $4 + c = f(2) = 6 \implies c = 2$。

---

[q:34, type:fill, ans:5]
在證明 $\lim_{x \to 1} (5x + 3) = 8$ 時，取 $\delta = \frac{\epsilon}{k}$，試求常數 $k$ 的精確值。
<!-- solution -->
$|5x + 3 - 8| = |5x - 5| = 5|x - 1| < \epsilon \implies |x - 1| < \frac{\epsilon}{5}$。故 $k = 5$。

---

[q:35, type:fill, ans:12]
求極限 $\lim_{x \to 2} (x^3 + 2x)$ 的精確值。
<!-- solution -->
直接代入：$2^3 + 2(2) = 8 + 4 = 12$。

---

[q:36, type:fill, ans:2]
求極限 $\lim_{x \to \infty} \frac{2x + 5}{x - 1}$ 的精確值。
<!-- solution -->
最高次項係數比：$\frac{2}{1} = 2$。

---

[q:37, type:fill, ans:4]
已知曲線 $y = x^2$ 且點 $P(1, 1)$ 在此圖形上。試問當 $x=2$ 時在 $y = x^2$ 上的切線斜率。
<!-- solution -->
微分 $y' = 2x$。代入 $x=2 \implies 2(2) = 4$。

---

[q:38, type:fill, ans:2]
已知 $f(x) = 2x$，求 $f(1)$ 的值。
<!-- solution -->
代入 $x=1 \implies 2(1) = 2$。

---

[q:39, type:fill, ans:1]
已知 $\lim_{x \to 0} \frac{\sin x}{x} = 1$，試求 $\lim_{x \to 0} \frac{\sin 2x}{2x}$ 的精確值。
<!-- solution -->
此為基本極限式，值為 1。

---

[q:40, type:fill, ans:10]
求極限 $\lim_{x \to 2} (3x + 4)$ 的精確值。
<!-- solution -->
直接代入：$3(2) + 4 = 6 + 4 = 10$。

---

[q:41, type:fill, ans:5]
若 $f(x) = 2x+1$，求 $f(2)$ 的值。
<!-- solution -->
$2(2)+1 = 5$。

---

[q:42, type:fill, ans:1]
已知 $\lim_{x \to 3} c = 1$（$c$ 為常數），求 $c$。
<!-- solution -->
常數極限恆等於常數本身，故 $c = 1$。

---

[q:43, type:fill, ans:9]
求極限 $\lim_{x \to 3} x^2$ 的值。
<!-- solution -->
$3^2 = 9$。

---

[q:44, type:fill, ans:4]
若 $\lim_{x \to 2} 2x = d$，求 $d$ 的值。
<!-- solution -->
$2(2) = 4$。

---

[q:45, type:fill, ans:0]
已知 $f(x) = x^3 - x$，求 $f(1)$。
<!-- solution -->
$1^3 - 1 = 0$。

---

[q:46, type:fill, ans:1]
若 $\lim_{x \to 0} \cos(5x) = e$，求 $e$ 的值。
<!-- solution -->
$\cos(0) = 1$。

---

[q:47, type:fill, ans:8]
求極限 $\lim_{x \to 4} 2x$ 的值。
<!-- solution -->
$2(4) = 8$。

---

[q:48, type:fill, ans:3]
若 $\lim_{x \to 1} (x+2) = c$，求 $c$ 的值。
<!-- solution -->
$1+2 = 3$。

---

[q:49, type:fill, ans:2]
求極限 $\lim_{x \to 1} \sqrt{x+3}$ 的值。
<!-- solution -->
$\sqrt{1+3} = 2$。

---

[q:50, type:fill, ans:0]
求極限 $\lim_{x \to 0} \sin(3x)$ 的值。
<!-- solution -->
$\sin(0) = 0$。
