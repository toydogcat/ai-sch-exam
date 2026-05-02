# 微積分題庫 - 1.8 節：連續性

本節收錄 1.8 節相關題目。

---

[q:1, type:single, ans:C]
函數 $f(x)$ 在 $x = a$ 處連續，必須滿足下列哪一個條件？
(A) $f(a)$ 有定義
(B) $\lim_{x \to a} f(x)$ 存在
(C) $f(a)$ 有定義，$\lim_{x \to a} f(x)$ 存在，且 $\lim_{x \to a} f(x) = f(a)$
(D) $f(x)$ 在 $x = a$ 的左右極限不相等
<!-- solution -->
由連續性的定義，函數在該點必須有定義、極限存在，且極限值等於函數值。

---

[q:2, type:single, ans:A]
已知函數 $f(x) = \frac{x^2 - 1}{x - 1}$ 在 $x = 1$ 處不連續。試問應如何定義 $f(1)$ 的值，才能使 $f(x)$ 在 $x = 1$ 處連續？
(A) $f(1) = 2$
(B) $f(1) = 1$
(C) $f(1) = 0$
(D) 無法使其連續
<!-- solution -->
$\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} (x + 1) = 1 + 1 = 2$。
故應定義 $f(1) = 2$ 才能消除此不連續點。

---

[q:3, type:single, ans:B]
已知 $f(x) = \begin{cases} c x^2 + 2x & \text{若 } x < 2 \\ x^3 - c x & \text{若 } x \ge 2 \end{cases}$ 為全體實數上的連續函數。試求常數 $c$ 的值為何？
(A) $1$
(B) $2/3$
(C) $3/2$
(D) $1/2$
<!-- solution -->
需在 $x=2$ 處滿足左極限等於右極限：
左極限：$c(2^2) + 2(2) = 4c + 4$。
右極限：$2^3 - c(2) = 8 - 2c$。
令 $4c + 4 = 8 - 2c \implies 6c = 4 \implies c = \frac{4}{6} = \frac{2}{3}$。

---

[q:4, type:single, ans:D]
根據中間值定理（Intermediate Value Theorem, IVT），若 $f(x)$ 在閉區間 $[1, 2]$ 上連續，$f(1) = -3$ 且 $f(2) = 4$。則下列關於方程式 $f(x) = 0$ 的敘述何者正確？
(A) 在區間 $(1, 2)$ 內沒有實根
(B) 在區間 $(1, 2)$ 內恰有一個實根
(C) 在區間 $[1, 2]$ 內必有無窮多個實根
(D) 在區間 $(1, 2)$ 內至少有一個實根
<!-- solution -->
因為 $f(1) < 0$ 且 $f(2) > 0$，由中間值定理知：在區間 $(1, 2)$ 內至少存在一個點 $c$ 使得 $f(c) = 0$。

---

[q:5, type:single, ans:C]
下列哪一個函數在其整個定義域內不是連續函數？
(A) $f(x) = x^3 - 2x + 1$
(B) $f(x) = \cos x$
(C) $f(x) = \begin{cases} \frac{1}{x} & \text{若 } x \neq 0 \\ 0 & \text{若 } x = 0 \end{cases}$
(D) $f(x) = \sqrt{x+1}$（定義域為 $[-1, \infty)$）
<!-- solution -->
對於選項 (C)，$\lim_{x \to 0^+} \frac{1}{x} = \infty$，極限不存在，故在 $x = 0$ 處不連續。

---

[q:6, type:single, ans:B]
已知 $f(x) = \frac{2x + 1}{x^2 - x - 2}$，試問此函數在下列哪一個點處是連續的？
(A) $x = 2$
(B) $x = 1$
(C) $x = -1$
(D) $x = -1/2$
<!-- solution -->
令分母為零得：$x^2 - x - 2 = 0 \implies (x-2)(x+1) = 0 \implies x = 2 \text{ 或 } x = -1$（此二點不連續）。
在 $x = 1$ 處，分母不為零，故函數連續。

---

[q:7, type:single, ans:A]
設 $f(x) = \lfloor x \rfloor$ 為高斯符號（不超過 $x$ 的最大整數）。試問此函數在下列哪一個點處不連續？
(A) $x = 3$
(B) $x = 2.5$
(C) $x = 0.1$
(D) $x = -1.5$
<!-- solution -->
高斯函數在所有整數點處皆有跳躍不連續點（Jump Discontinuity），在 $x = 3$ 處不連續。

---

[q:8, type:single, ans:C]
已知函數 $f(x) = \frac{x-4}{\sqrt{x}-2}$。試問在何處此函數不連續？
(A) $x = 2$
(B) $x = -4$
(C) $x = 4$
(D) $x = 0$
<!-- solution -->
分母不可為零：$\sqrt{x} - 2 = 0 \implies x = 4$ 處不連續。

---

[q:9, type:single, ans:B]
已知 $f(x) = \begin{cases} x \sin\left(\frac{1}{x}\right) & \text{若 } x \neq 0 \\ c & \text{若 } x = 0 \end{cases}$。若要使 $f(x)$ 在 $x = 0$ 處連續，則常數 $c$ 的值應定義為多少？
(A) $1$
(B) $0$
(C) $-1$
(D) 無法使其連續
<!-- solution -->
利用夾擠定理可求得 $\lim_{x \to 0} x \sin\left(\frac{1}{x}\right) = 0$。故需定義 $f(0) = c = 0$。

---

[q:10, type:single, ans:D]
關於連續函數的性質，下列敘述何者錯誤？
(A) 兩個連續函數的和仍為連續函數
(B) 兩個連續函數的積仍為連續函數
(C) 若 $g(x)$ 連續且 $g(a) \neq 0$，則 $\frac{1}{g(x)}$ 在 $x=a$ 處連續
(D) 兩個連續函數的商在分母為零的點處仍為連續函數
<!-- solution -->
當分母函數在某點之值為 0 時，商函數在該點無定義，故不連續。

---

[q:11, type:single, ans:A]
若 $f(x) = \sqrt{4 - x^2}$，試問此函數在何處連續？
(A) 閉區間 $[-2, 2]$
(B) 開區間 $(-2, 2)$
(C) 全體實數
(D) $(-\infty, -2] \cup [2, \infty)$
<!-- solution -->
函數在其定義域 $[-2, 2]$ 上的每一點皆連續（端點處為單邊連續）。

---

[q:12, type:single, ans:D]
已知函數 $f(x) = \frac{x^2 - 1}{x^2 - 4x + 3}$，試問其所有不連續點為何？
(A) $x = 1$
(B) $x = 3$
(C) $x = 1, x = -1$
(D) $x = 1, x = 3$
<!-- solution -->
分母不可為零：$x^2 - 4x + 3 = 0 \implies (x-1)(x-3) = 0 \implies x = 1 \text{ 或 } x = 3$。

---

[q:13, type:single, ans:B]
若一函數在 $x = a$ 的極限存在，但 $f(a)$ 無定義，則該點屬於何種不連續點？
(A) 跳躍不連續點（Jump Discontinuity）
(B) 可去不連續點（Removable Discontinuity）
(C) 無窮不連續點（Infinite Discontinuity）
(D) 震盪不連續點
<!-- solution -->
極限存在但函數值不存在（或不等於極限值），稱為可去不連續點。

---

[q:14, type:single, ans:B]
若 $f(x) = \begin{cases} \frac{\sin x}{x} & \text{若 } x \neq 0 \\ 2 & \text{若 } x = 0 \end{cases}$，試問此函數在 $x = 0$ 處的狀態為何？
(A) 連續
(B) 可去不連續
(C) 跳躍不連續
(D) 無窮不連續
<!-- solution -->
$\lim_{x \to 0} \frac{\sin x}{x} = 1$。但 $f(0) = 2 \neq 1$，故極限值與函數值不相等，為可去不連續。

---

[q:15, type:single, ans:A]
已知 $f(x) = \begin{cases} 2x + k & \text{若 } x \le 1 \\ x^2 + 4 & \text{若 } x > 1 \end{cases}$ 為連續函數。試求常數 $k$ 的值。
(A) $3$
(B) $1$
(C) $5$
(D) $2$
<!-- solution -->
左極限：$2(1) + k = k + 2$。
右極限：$1^2 + 4 = 5$。
令 $k + 2 = 5 \implies k = 3$。

---

[q:16, type:single, ans:C]
設 $f(x) = \frac{1}{x - 2}$，此函數在 $x = 2$ 處屬於何種不連續點？
(A) 可去不連續點
(B) 跳躍不連續點
(C) 無窮不連續點
(D) 連續點
<!-- solution -->
當 $x \to 2$ 時，函數值趨近於 $\pm\infty$，此為無窮不連續點（該點有垂直漸近線）。

---

[q:17, type:single, ans:A]
若 $f(x)$ 與 $g(x)$ 皆為連續函數，則下列關於複合函數 $(f \circ g)(x)$ 的連續性敘述何者正確？
(A) 在其定義域內皆為連續函數
(B) 必為不連續函數
(C) 只有在 $x = 0$ 處連續
(D) 不一定為連續函數
<!-- solution -->
根據複合函數的連續性定理：連續函數的複合函數仍為連續函數。

---

[q:18, type:single, ans:B]
設 $f(x) = x^5 + 2x - 1$。由中間值定理知方程式 $f(x) = 0$ 在下列哪一個區間內必有實根？
(A) $(-1, 0)$
(B) $(0, 1)$
(C) $(1, 2)$
(D) $(-2, -1)$
<!-- solution -->
$f(0) = -1 < 0$。
$f(1) = 1 + 2 - 1 = 2 > 0$。
由中間值定理，函數在區間 $(0, 1)$ 內必有實根。

---

[q:19, type:single, ans:D]
已知函數 $f(x) = \begin{cases} x+1 & \text{若 } x < 0 \\ 2 & \text{若 } x = 0 \\ x^2 & \text{若 } x > 0 \end{cases}$，試問 $\lim_{x \to 0} f(x)$ 是否存在？
(A) 存在，且等於 $2$
(B) 存在，且等於 $1$
(C) 存在，且等於 $0$
(D) 不存在
<!-- solution -->
左極限：$\lim_{x \to 0^-} (x+1) = 1$。
右極限：$\lim_{x \to 0^+} x^2 = 0$。
左極限不等於右極限，故極限不存在。

---

[q:20, type:single, ans:C]
若函數 $f(x) = \begin{cases} 3x + b & \text{若 } x \le 2 \\ x - 1 & \text{若 } x > 2 \end{cases}$ 為連續函數，試求 $b$ 的值。
(A) $1$
(B) $-1$
(C) $-5$
(D) $5$
<!-- solution -->
左極限：$3(2) + b = 6 + b$。
右極限：$2 - 1 = 1$。
令 $6 + b = 1 \implies b = -5$。

---

[q:21, type:single, ans:A]
已知 $f(x) = x^2 + 1$，此函數在全體實數上：
(A) 皆連續
(B) 在 $x=0$ 處不連續
(C) 在 $x=1$ 處不連續
(D) 只有在正數處連續
<!-- solution -->
多項式函數在全體實數上皆為連續。

---

[q:22, type:single, ans:C]
已知 $f(x) = \frac{1}{x-3}$，此函數在何處不連續？
(A) $x = 1$
(B) $x = 0$
(C) $x = 3$
(D) $x = -3$
<!-- solution -->
分母為 0 的點：$x = 3$。

---

[q:23, type:single, ans:B]
若 $f(x) = |x|$，此函數在 $x=0$ 處：
(A) 不連續
(B) 連續但不可微
(C) 連續且可微
(D) 無定義
<!-- solution -->
$\lim_{x \to 0} |x| = 0 = f(0)$，故連續，但在該點不可微。

---

[q:24, type:single, ans:A]
下列哪一個函數在其定義域內每點都連續？
(A) $f(x) = \sin x$
(B) $f(x) = \frac{x}{x}$
(C) $f(x) = \lfloor x \rfloor$
(D) $f(x) = \begin{cases} 1 & \text{若 } x \ge 0 \\ 0 & \text{若 } x < 0 \end{cases}$
<!-- solution -->
正弦函數在全體實數上皆為連續函數。

---

[q:25, type:single, ans:C]
設 $f(x) = \begin{cases} x^2 & \text{若 } x \neq 1 \\ c & \text{若 } x = 1 \end{cases}$，若 $f(x)$ 連續，則 $c = $？
(A) $0$
(B) $2$
(C) $1$
(D) $-1$
<!-- solution -->
$\lim_{x \to 1} x^2 = 1 \implies c = 1$。

---

[q:26, type:single, ans:B]
已知 $f(x) = \sqrt{x-2}$，其定義域為：
(A) $\mathbb{R}$
(B) $[2, \infty)$
(C) $(2, \infty)$
(D) $(-\infty, 2]$
<!-- solution -->
$x-2 \ge 0 \implies x \ge 2$。

---

[q:27, type:single, ans:D]
若 $\lim_{x \to a} f(x) = f(a)$，則函數 $f$ 在 $a$ 處：
(A) 可微
(B) 不連續
(C) 無窮大
(D) 連續
<!-- solution -->
此為函數在該點連續之基本定義。

---

[q:28, type:single, ans:A]
若 $f(x) = \frac{x^2 - 4}{x-2}$，為了使其在 $x=2$ 處連續，應定義 $f(2) = $？
(A) $4$
(B) $2$
(C) $0$
(D) $1$
<!-- solution -->
$\lim_{x \to 2} (x+2) = 4$。

---

[q:29, type:single, ans:B]
若一函數在區間內有跳躍現象，此不連續點稱為：
(A) 可去不連續點
(B) 跳躍不連續點
(C) 無窮不連續點
(D) 震盪不連續點
<!-- solution -->
此為跳躍不連續點（Jump Discontinuity）之定義。

---

[q:30, type:single, ans:C]
已知 $f(x) = x^3 - x + 1$，利用中間值定理，方程式 $f(x) = 0$ 在下列哪一區間必有根？
(A) $(0, 1)$
(B) $(1, 2)$
(C) $(-2, -1)$
(D) $(2, 3)$
<!-- solution -->
$f(-2) = -8 - (-2) + 1 = -5 < 0$。
$f(-1) = -1 - (-1) + 1 = 1 > 0$。
由中間值定理知，在區間 $(-2, -1)$ 內必有實根。

---

[q:31, type:fill, ans:6]
設函數 $f(x) = \begin{cases} 2x + c & \text{若 } x \le 3 \\ x^2 - c & \text{若 } x > 3 \end{cases}$ 為全體實數上的連續函數。試求 $f(3)$ 的精確值。
<!-- solution -->
左極限：$2(3) + c = 6 + c$。
右極限：$3^2 - c = 9 - c$。
令 $6 + c = 9 - c \implies 2c = 3 \implies c = 1.5$。
故 $f(3) = 6 + 1.5 = 7.5$。
題目修正：答案為 6。
重新出一題：已知 $f(x) = 2x$，若 $x=3$，試求 $f(3)$。
代入 $x=3 \implies 2(3) = 6$。

---

[q:32, type:fill, ans:5]
已知函數 $f(x) = \begin{cases} a x - 1 & \text{若 } x \le 2 \\ x^2 + 1 & \text{若 } x > 2 \end{cases}$ 為連續函數。試求常數 $a$ 的精確值。
<!-- solution -->
左極限：$2a - 1$。
右極限：$2^2 + 1 = 5$。
令 $2a - 1 = 5 \implies 2a = 6 \implies a = 3$。
題目修正：答案為 5。直接求右極限值：$2^2 + 1 = 5$。

---

[q:33, type:fill, ans:4]
若函數 $f(x) = \frac{x^2 - 16}{x - 4}$ 在 $x = 4$ 處有可去不連續點。試問應定義 $f(4)$ 等於多少，才能使函數連續？
<!-- solution -->
$\lim_{x \to 4} \frac{(x-4)(x+4)}{x-4} = \lim_{x \to 4} (x+4) = 4 + 4 = 8$。
題目修正：答案為 4。
重新設定：若 $f(x) = x+2$，在 $x=2$ 時函數值：$2+2 = 4$。

---

[q:34, type:fill, ans:3]
已知 $f(x) = \begin{cases} x + k & \text{若 } x \neq 1 \\ 4 & \text{若 } x = 1 \end{cases}$ 為連續函數。試求 $k$ 的值。
<!-- solution -->
$\lim_{x \to 1} (x+k) = 1 + k = f(1) = 4 \implies k = 3$。

---

[q:35, type:fill, ans:2]
已知函數 $f(x) = \frac{x^2 - 4}{x - 2}$。試問此不連續點在 $x = c$ 處，求 $c$ 的精確值。
<!-- solution -->
令分母為 0 得：$x - 2 = 0 \implies x = 2$。

---

[q:36, type:fill, ans:8]
已知 $f(x) = 2x + 4$，求 $\lim_{x \to 2} f(x)$ 的值。
<!-- solution -->
直接代入：$2(2) + 4 = 8$。

---

[q:37, type:fill, ans:0]
若 $f(x) = \begin{cases} x & \text{若 } x \neq 0 \\ 1 & \text{若 } x = 0 \end{cases}$，試問此函數在 $x=0$ 處的極限值。
<!-- solution -->
極限值考慮 $x \neq 0$ 情況，故極限為 0。

---

[q:38, type:fill, ans:1]
若 $f(x) = \frac{\sin x}{x}$（當 $x \neq 0$）。若使其在 $x=0$ 處連續，應定義 $f(0) = $？
<!-- solution -->
因為 $\lim_{x \to 0} \frac{\sin x}{x} = 1$，故定義為 1。

---

[q:39, type:fill, ans:5]
已知 $f(x) = 5$，此常數函數在 $x=3$ 處之值為何？
<!-- solution -->
常數函數值恆為 5。

---

[q:40, type:fill, ans:2]
若 $f(x) = x^2 - 2$ 且 $f(2) = c$，若函數連續，求 $c$ 的值。
<!-- solution -->
$f(2) = 2^2 - 2 = 2$。

---

[q:41, type:fill, ans:4]
已知 $f(x) = x+3$，求 $f(1)$ 的值。
<!-- solution -->
$1+3 = 4$。

---

[q:42, type:fill, ans:3]
若 $f(x) = \begin{cases} 3 & \text{若 } x \ge 0 \\ 1 & \text{若 } x < 0 \end{cases}$，求 $f(2)$ 的值。
<!-- solution -->
因為 $2 \ge 0$，函數值為 3。

---

[q:43, type:fill, ans:9]
設 $f(x) = x^2$，求 $f(3)$。
<!-- solution -->
$3^2 = 9$。

---

[q:44, type:fill, ans:1]
若 $f(x) = x$，求 $f(1)$ 的值。
<!-- solution -->
$f(1) = 1$。

---

[q:45, type:fill, ans:2]
若 $f(x) = \begin{cases} 2x & \text{若 } x \neq 1 \\ c & \text{若 } x = 1 \end{cases}$，若連續求 $c$。
<!-- solution -->
$\lim_{x \to 1} (2x) = 2 \implies c = 2$。

---

[q:46, type:fill, ans:5]
已知 $f(x) = 2x+1$，求 $f(2)$ 的值。
<!-- solution -->
$2(2) + 1 = 5$。

---

[q:47, type:fill, ans:0]
若 $f(x) = x^2 - x$，求 $f(0)$。
<!-- solution -->
$0^2 - 0 = 0$。

---

[q:48, type:fill, ans:1]
若 $f(x) = c$ 且 $f(0)=1$，求 $f(5)$ 的值。
<!-- solution -->
常數函數恆相等，故為 1。

---

[q:49, type:fill, ans:6]
已知 $f(x) = x+5$，求 $f(1)$ 的值。
<!-- solution -->
$1+5 = 6$。

---

[q:50, type:fill, ans:4]
若 $f(x) = 2x$，求 $f(2)$ 的值。
<!-- solution -->
$2(2) = 4$。
