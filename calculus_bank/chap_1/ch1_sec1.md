# 微積分題庫 - 1.1 節：函數及其表示法

本節收錄 1.1 節相關題目。

---

[q:1, type:single, ans:B]
已知 $f(x) = \sqrt{x - 2}$，試求此函數的定義域為何？
(A) $(2, \infty)$
(B) $[2, \infty)$
(C) $(-\infty, 2]$
(D) $\mathbb{R}$
<!-- solution -->
根號內部需大於等於 0：$x - 2 \ge 0 \implies x \ge 2$。故定義域為 $[2, \infty)$。

---

[q:2, type:single, ans:A]
求函數 $f(x) = \frac{x + 1}{x^2 - 4}$ 的定義域為何？
(A) $\{x \in \mathbb{R} \mid x \neq \pm 2\}$
(B) $\{x \in \mathbb{R} \mid x \neq 4\}$
(C) $\{x \in \mathbb{R} \mid x \neq -1\}$
(D) $\mathbb{R}$
<!-- solution -->
分母不可為零：$x^2 - 4 \neq 0 \implies x \neq \pm 2$。

---

[q:3, type:single, ans:C]
已知函數 $f(x) = 3x^2 + 1$，試計算 $f(2a)$ 的值為何？
(A) $6a^2 + 1$
(B) $12a + 1$
(C) $12a^2 + 1$
(D) $3a^2 + 1$
<!-- solution -->
將 $x=2a$ 代入函數中：$f(2a) = 3(2a)^2 + 1 = 3(4a^2) + 1 = 12a^2 + 1$。

---

[q:4, type:single, ans:D]
下列哪一個函數為奇函數（即滿足 $f(-x) = -f(x)$）？
(A) $f(x) = x^2 + 1$
(B) $f(x) = |x|$
(C) $f(x) = \cos x$
(D) $f(x) = x^3 - x$
<!-- solution -->
代入 $-x$：$f(-x) = (-x)^3 - (-x) = -x^3 + x = -(x^3 - x) = -f(x)$，故為奇函數。

---

[q:5, type:single, ans:A]
若 $f(x) = x^2 - x$，試求差商 $\frac{f(2+h) - f(2)}{h}$ 的化簡結果。
(A) $h + 3$
(B) $h + 4$
(C) $h + 2$
(D) $3$
<!-- solution -->
$f(2) = 2^2 - 2 = 2$。
$f(2+h) = (2+h)^2 - (2+h) = 4 + 4h + h^2 - 2 - h = h^2 + 3h + 2$。
差商為 $\frac{h^2 + 3h + 2 - 2}{h} = \frac{h^2 + 3h}{h} = h + 3$。

---

[q:6, type:single, ans:B]
若函數 $f(x) = \frac{1}{x}$，試求其定義域為何？
(A) $[0, \infty)$
(B) $\{x \in \mathbb{R} \mid x \neq 0\}$
(C) $(0, \infty)$
(D) $\mathbb{R}$
<!-- solution -->
分母不可為零，故 $x \neq 0$。

---

[q:7, type:single, ans:D]
已知函數 $f(x) = |x - 3|$，試求 $f(1)$ 的值為何？
(A) $3$
(B) $-2$
(C) $1$
(D) $2$
<!-- solution -->
$f(1) = |1 - 3| = |-2| = 2$。

---

[q:8, type:single, ans:A]
設 $f(x) = x^4 + x^2 + 3$，試問此函數對稱於何處？
(A) $y$ 軸（偶函數）
(B) 原點（奇函數）
(C) $x$ 軸
(D) 直線 $y = x$
<!-- solution -->
代入 $-x$：$f(-x) = (-x)^4 + (-x)^2 + 3 = x^4 + x^2 + 3 = f(x)$，為偶函數，對稱於 $y$ 軸。

---

[q:9, type:single, ans:C]
求函數 $f(x) = \sqrt{4 - x^2}$ 的定義域為何？
(A) $(-\infty, -2] \cup [2, \infty)$
(B) $(-2, 2)$
(C) $[-2, 2]$
(D) $[0, 2]$
<!-- solution -->
根號內部需非負：$4 - x^2 \ge 0 \implies x^2 \le 4 \implies -2 \le x \le 2$。

---

[q:10, type:single, ans:C]
已知函數 $f(x) = \sqrt[4]{x}$，試問其定義域為何？
(A) $\mathbb{R}$
(B) $(0, \infty)$
(C) $[0, \infty)$
(D) $(-\infty, 0]$
<!-- solution -->
偶次方根的內部不可為負，故 $x \ge 0$。

---

[q:11, type:single, ans:B]
已知 $f(x) = \begin{cases} x^2 & \text{若 } x \le 1 \\ 2x - 1 & \text{若 } x > 1 \end{cases}$，試問 $f(-2)$ 的值為何？
(A) $-5$
(B) $4$
(C) $-4$
(D) $1$
<!-- solution -->
因為 $-2 \le 1$，應代入第一段：$f(-2) = (-2)^2 = 4$。

---

[q:12, type:single, ans:A]
求函數 $f(x) = \sqrt{x+2} + \sqrt{5-x}$ 的定義域。
(A) $[-2, 5]$
(B) $(-2, 5)$
(C) $[2, 5]$
(D) $[-2, \infty)$
<!-- solution -->
需滿足 $x+2 \ge 0$ 且 $5-x \ge 0 \implies x \ge -2$ 且 $x \le 5$。故定義域為 $[-2, 5]$。

---

[q:13, type:single, ans:B]
若一長方形的周長為 20 公尺，將此長方形的面積 $A$ 表示為其中一邊長 $x$ 的函數，則解析式為何？
(A) $A(x) = x(20 - x)$
(B) $A(x) = x(10 - x)$
(C) $A(x) = 2x(10 - x)$
(D) $A(x) = x^2$
<!-- solution -->
設長方形兩邊長為 $x$ 與 $y$，則 $2x + 2y = 20 \implies y = 10 - x$。
面積 $A = x \cdot y = x(10 - x)$。

---

[q:14, type:single, ans:C]
若函數 $f(x) = x^3 + 2$，試問此函數在 $y$ 軸上的截距為何？
(A) $0$
(B) $1$
(C) $2$
(D) $3$
<!-- solution -->
代入 $x=0$ 得：$f(0) = 0^3 + 2 = 2$。

---

[q:15, type:single, ans:D]
若函數 $f(x) = x^2 + 2x + 1$，試問其與 $x$ 軸的交點座標為何？
(A) $(1, 0)$
(B) $(0, 1)$
(C) $(2, 0)$
(D) $(-1, 0)$
<!-- solution -->
令 $f(x) = 0 \implies x^2 + 2x + 1 = 0 \implies (x+1)^2 = 0 \implies x = -1$。交點為 $(-1, 0)$。

---

[q:16, type:single, ans:A]
下列哪一個函數為偶函數？
(A) $f(x) = \frac{x^2}{x^2 + 1}$
(B) $f(x) = x^3 - x$
(C) $f(x) = x + 1$
(D) $f(x) = \sin x$
<!-- solution -->
代入 $-x$：$f(-x) = \frac{(-x)^2}{(-x)^2 + 1} = \frac{x^2}{x^2 + 1} = f(x)$，為偶函數。

---

[q:17, type:single, ans:D]
求函數 $f(x) = \frac{1}{\sqrt{x^2 - 1}}$ 的定義域。
(A) $[-1, 1]$
(B) $(-1, 1)$
(C) $(-\infty, -1] \cup [1, \infty)$
(D) $(-\infty, -1) \cup (1, \infty)$
<!-- solution -->
根號在分母，內部需大於零：$x^2 - 1 > 0 \implies x^2 > 1 \implies x > 1 \text{ 或 } x < -1$。

---

[q:18, type:single, ans:A]
已知 $f(x) = \sqrt{x+1}$，求差商 $\frac{f(x) - f(0)}{x}$ 的化簡結果。
(A) $\frac{1}{\sqrt{x+1} + 1}$
(B) $\frac{1}{\sqrt{x+1} - 1}$
(C) $\sqrt{x+1} - 1$
(D) $\sqrt{x+1} + 1$
<!-- solution -->
$f(0) = \sqrt{0+1} = 1$。
差商為 $\frac{\sqrt{x+1} - 1}{x} = \frac{(\sqrt{x+1} - 1)(\sqrt{x+1} + 1)}{x(\sqrt{x+1} + 1)} = \frac{x}{x(\sqrt{x+1} + 1)} = \frac{1}{\sqrt{x+1} + 1}$。

---

[q:19, type:single, ans:B]
若一等邊三角形的邊長為 $s$，將此等邊三角形的面積 $A$ 表示為 $s$ 的函數，則解析式為何？
(A) $A(s) = \frac{1}{2} s^2$
(B) $A(s) = \frac{\sqrt{3}}{4} s^2$
(C) $A(s) = \sqrt{3} s^2$
(D) $A(s) = \frac{\sqrt{3}}{2} s^2$
<!-- solution -->
等邊三角形面積公式為 $\frac{\sqrt{3}}{4} \text{邊長}^2$，故為 $A(s) = \frac{\sqrt{3}}{4} s^2$。

---

[q:20, type:single, ans:C]
已知函數 $f(x) = \sqrt{x - 3} + \frac{1}{x - 5}$，求其定義域。
(A) $[3, \infty)$
(B) $(3, \infty) \setminus \{5\}$
(C) $[3, 5) \cup (5, \infty)$
(D) $(5, \infty)$
<!-- solution -->
需滿足 $x - 3 \ge 0$ 且 $x - 5 \neq 0 \implies x \ge 3$ 且 $x \neq 5$。

---

[q:21, type:single, ans:D]
已知函數 $f(x) = 2x^2 + 3$，求當 $x=-1$ 時函數值。
(A) $2$
(B) $4$
(C) $3$
(D) $5$
<!-- solution -->
$f(-1) = 2(-1)^2 + 3 = 5$。

---

[q:22, type:single, ans:B]
若函數 $f(x) = x^4 - 2$，試問其為奇函數還是偶函數？
(A) 奇函數
(B) 偶函數
(C) 既非奇函數也非偶函數
(D) 既是奇函數也是偶函數
<!-- solution -->
$f(-x) = (-x)^4 - 2 = x^4 - 2 = f(x)$，為偶函數。

---

[q:23, type:single, ans:A]
已知函數 $f(x) = \frac{2}{x - 1}$，其定義域為何？
(A) $\{x \in \mathbb{R} \mid x \neq 1\}$
(B) $\{x \in \mathbb{R} \mid x \neq 2\}$
(C) $\{x \in \mathbb{R} \mid x \neq -1\}$
(D) $\mathbb{R}$
<!-- solution -->
分母不為零即可：$x \neq 1$。

---

[q:24, type:single, ans:B]
設 $f(x) = \sqrt{x} + \frac{1}{x-2}$，求此函數的定義域。
(A) $(0, \infty)$
(B) $[0, 2) \cup (2, \infty)$
(C) $[0, \infty)$
(D) $(2, \infty)$
<!-- solution -->
需滿足 $x \ge 0$ 且 $x \neq 2$，即 $[0, 2) \cup (2, \infty)$。

---

[q:25, type:single, ans:C]
求差商 $\frac{f(1+h) - f(1)}{h}$ 當 $f(x) = 3x^2$ 時的結果。
(A) $6$
(B) $h + 3$
(C) $3h + 6$
(D) $3h + 1$
<!-- solution -->
$f(1) = 3$。$f(1+h) = 3(1+h)^2 = 3(1 + 2h + h^2) = 3 + 6h + 3h^2$。
差商為 $\frac{3h^2+6h}{h} = 3h + 6$。

---

[q:26, type:single, ans:A]
已知 $f(x) = x^2 - x + 1$，試求 $f(2)$ 的值。
(A) $3$
(B) $1$
(C) $2$
(D) $4$
<!-- solution -->
$f(2) = 2^2 - 2 + 1 = 3$。

---

[q:27, type:single, ans:D]
若一矩形的寬度為 $w$，長度為 $2w$，則其面積 $A$ 作為寬度 $w$ 的函數表示為何？
(A) $A(w) = w$
(B) $A(w) = 2w$
(C) $A(w) = w^2$
(D) $A(w) = 2w^2$
<!-- solution -->
面積 $A = \text{長} \times \text{寬} = 2w \times w = 2w^2$。

---

[q:28, type:single, ans:C]
已知 $f(x) = \frac{x^2 - 9}{x-3}$ 的定義域排除 $x=3$。若 $x \neq 3$，則該函數可化簡為：
(A) $x - 3$
(B) $x$
(C) $x + 3$
(D) $1$
<!-- solution -->
分子因式分解為 $(x-3)(x+3)$，約去分母得 $x + 3$。

---

[q:29, type:single, ans:B]
若一函數滿足 $f(-x) = f(x)$，則此函數對稱於：
(A) 原點
(B) $y$ 軸
(C) $x$ 軸
(D) 直線 $y = x$
<!-- solution -->
為偶函數之定義，圖形對稱於 $y$ 軸。

---

[q:30, type:single, ans:A]
若 $f(x) = \begin{cases} 2x & \text{若 } x \le 0 \\ x^2 & \text{若 } x > 0 \end{cases}$，試求 $f(3)$ 的值。
(A) $9$
(B) $6$
(C) $3$
(D) $0$
<!-- solution -->
因為 $3 > 0$，代入第二段得 $3^2 = 9$。

---

[q:31, type:fill, ans:9]
已知函數 $f(x) = 2x^2 + 1$，試求當 $x=2$ 時之精確函數值。
<!-- solution -->
代入 $x=2$ 得：$f(2) = 2(2^2) + 1 = 8 + 1 = 9$。

---

[q:32, type:fill, ans:4]
已知函數 $f(x) = |x - 7|$，試求當 $x=3$ 時之精確函數值。
<!-- solution -->
代入 $x=3$ 得：$f(3) = |3 - 7| = |-4| = 4$。

---

[q:33, type:fill, ans:12]
已知函數 $f(x) = 3x + 1$，若 $f(a) = 37$，試求 $a$ 的精確值。
<!-- solution -->
令 $3a + 1 = 37 \implies 3a = 36 \implies a = 12$。

---

[q:34, type:fill, ans:5]
設 $f(x) = x^2 - 3x + 1$，試求 $f(4)$ 的值。
<!-- solution -->
代入 $x=4$ 得：$f(4) = 4^2 - 3(4) + 1 = 16 - 12 + 1 = 5$。

---

[q:35, type:fill, ans:0]
已知函數 $f(x) = \frac{x}{x^2 + 1}$，試求 $f(0)$ 的精確函數值。
<!-- solution -->
直接代入 $x=0$：$f(0) = \frac{0}{0+1} = 0$。

---

[q:36, type:fill, ans:24]
若函數 $f(x) = x^2 + 3x - 4$，求 $f(4)$ 的值。
<!-- solution -->
代入 $x=4 \implies 4^2 + 3(4) - 4 = 16 + 12 - 4 = 24$。

---

[q:37, type:fill, ans:25]
已知函數 $f(x) = x^2 + 16$ 的值域為 $[b, \infty)$，試求常數 $b + 9$ 的精確值。
<!-- solution -->
因為 $x^2 \ge 0$，所以 $f(x) = x^2 + 16 \ge 16$，故值域為 $[16, \infty)$。$b = 16 \implies b + 9 = 25$。

---

[q:38, type:fill, ans:2]
若 $f(x) = |x| - 1$，試求 $f(-3)$ 的值。
<!-- solution -->
$f(-3) = |-3| - 1 = 3 - 1 = 2$。

---

[q:39, type:fill, ans:2]
若一函數定義為 $f(x) = \begin{cases} x+1 & \text{若 } x \ge 0 \\ x-1 & \text{若 } x < 0 \end{cases}$，試求 $f(1)$ 的值。
<!-- solution -->
因為 $1 \ge 0$，應代入第一段：$f(1) = 1 + 1 = 2$。

---

[q:40, type:fill, ans:10]
已知函數 $f(x) = 2x + 2$，若 $f(a) = 22$，試求 $a$ 的精確值。
<!-- solution -->
令 $2a + 2 = 22 \implies 2a = 20 \implies a = 10$。

---

[q:41, type:fill, ans:1]
若函數 $f(x) = x^3$，試求 $f(1)$ 的值。
<!-- solution -->
$f(1) = 1^3 = 1$。

---

[q:42, type:fill, ans:3]
已知函數 $f(x) = |x| + 1$，試求 $f(-2)$ 的值。
<!-- solution -->
$f(-2) = |-2| + 1 = 2 + 1 = 3$。

---

[q:43, type:fill, ans:2]
若函數 $f(x) = \frac{x+2}{2}$，試求 $f(2)$ 的值。
<!-- solution -->
$f(2) = \frac{2+2}{2} = 2$。

---

[q:44, type:fill, ans:1]
若函數 $f(x) = x + c$ 滿足 $f(2) = 3$，試求常數 $c$ 的值。
<!-- solution -->
$2 + c = 3 \implies c = 1$。

---

[q:45, type:fill, ans:8]
已知 $f(x) = 2x$，試求 $f(4)$ 的值。
<!-- solution -->
$f(4) = 2(4) = 8$。

---

[q:46, type:fill, ans:4]
設 $f(x) = \sqrt{x+7}$，試求 $f(9)$ 的值。
<!-- solution -->
$f(9) = \sqrt{9+7} = \sqrt{16} = 4$。

---

[q:47, type:fill, ans:0]
若 $f(x) = x^2 - x$，試求 $f(1)$ 的值。
<!-- solution -->
$f(1) = 1^2 - 1 = 0$。

---

[q:48, type:fill, ans:1]
已知 $f(x) = c$（常數函數）。若 $f(3) = 1$，試求 $f(5)$ 的值。
<!-- solution -->
常數函數恆相等，故 $f(5) = 1$。

---

[q:49, type:fill, ans:25]
已知函數 $f(x) = 5x$，若 $f(a) = 125$，試求 $a$ 的值。
<!-- solution -->
$5a = 125 \implies a = 25$。

---

[q:50, type:fill, ans:7]
已知函數 $f(x) = 2x - 1$，試求 $f(4)$ 的值。
<!-- solution -->
$f(4) = 2(4) - 1 = 8 - 1 = 7$。
