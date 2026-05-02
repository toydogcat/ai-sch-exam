# 微積分題庫 - 1.5 節：函數的極限

本節收錄 1.5 節相關題目。

---

[q:1, type:single, ans:D]
若當 $x$ 從左側趨近於 $2$ 時，$f(x)$ 趨近於 $5$，這可以記作下列哪一個數學符號？
(A) $\lim_{x \to 2} f(x) = 5$
(B) $\lim_{x \to 2^+} f(x) = 5$
(C) $\lim_{x \to 5^-} f(x) = 2$
(D) $\lim_{x \to 2^-} f(x) = 5$
<!-- solution -->
從左側（比 2 小的方向）趨近於 2 記作 $x \to 2^-$。故極限記作 $\lim_{x \to 2^-} f(x) = 5$。

---

[q:2, type:single, ans:B]
已知 $f(x) = \frac{1}{|x|}$，試問當 $x \to 0$ 時，$f(x)$ 的極限狀態為何？
(A) $0$
(B) $\infty$
(C) $-\infty$
(D) 不存在
<!-- solution -->
當 $x \to 0$ 時，不論是從左側或右側趨近，$|x|$ 皆為趨近於 0 的正數，其倒數趨近於正無窮大 $\infty$。

---

[q:3, type:single, ans:A]
已知 $\lim_{x \to 1^-} f(x) = 3$ 且 $\lim_{x \to 1^+} f(x) = 3$，試問 $\lim_{x \to 1} f(x)$ 為多少？
(A) $3$
(B) $1$
(C) $6$
(D) 不存在
<!-- solution -->
當左極限等於右極限時，雙邊極限存在且等於該共同值，故為 3。

---

[q:4, type:single, ans:C]
已知函數 $f(x) = \begin{cases} 2x + 1 & \text{若 } x < 1 \\ 5 & \text{若 } x = 1 \\ x^2 + 2 & \text{若 } x > 1 \end{cases}$，求 $\lim_{x \to 1} f(x)$ 的值為何？
(A) $5$
(B) $1$
(C) $3$
(D) 不存在
<!-- solution -->
左極限：$\lim_{x \to 1^-} (2x+1) = 2(1) + 1 = 3$。
右極限：$\lim_{x \to 1^+} (x^2+2) = 1^2 + 2 = 3$。
左極限等於右極限，故雙邊極限為 3（不論 $f(1) = 5$ 為何）。

---

[q:5, type:single, ans:D]
求極限 $\lim_{x \to 3^+} \frac{2}{x - 3}$ 的值。
(A) $0$
(B) $2$
(C) $-\infty$
(D) $\infty$
<!-- solution -->
當 $x \to 3^+$ 時，$x-3$ 為趨近於 0 的正數。正數 2 除以趨近於 0 的正數趨近於正無窮大 $\infty$。

---

[q:6, type:single, ans:B]
若一函數的圖形在 $x = a$ 處有垂直漸近線，則下列哪一個敘述必成立？
(A) $f(a) = \infty$
(B) $\lim_{x \to a^+} f(x) = \pm\infty$ 或 $\lim_{x \to a^-} f(x) = \pm\infty$
(C) $\lim_{x \to a} f(x) = a$
(D) $f(a)$ 無定義
<!-- solution -->
垂直漸近線的定義即為當 $x \to a$ 的單邊或雙邊極限為無窮大。

---

[q:7, type:single, ans:A]
考慮極限 $\lim_{x \to 0} \sin\left(\frac{\pi}{x}\right)$。當 $x \to 0$ 時，此極限之狀態為何？
(A) 不存在，因函數值在 $-1$ 與 $1$ 之間劇烈震盪
(B) $0$
(C) $1$
(D) $\infty$
<!-- solution -->
當 $x \to 0$ 時，$\frac{\pi}{x} \to \pm\infty$，正弦函數值會在 $-1$ 與 $1$ 之間無限次震盪，極限不存在。

---

[q:8, type:single, ans:B]
已知 $f(x) = \frac{x-1}{x^2-1}$，試問此函數在何處有垂直漸近線？
(A) $x = 1$ 與 $x = -1$
(B) 僅在 $x = -1$ 處
(C) 僅在 $x = 1$ 處
(D) 無垂直漸近線
<!-- solution -->
$\lim_{x \to 1} \frac{x-1}{(x-1)(x+1)} = \lim_{x \to 1} \frac{1}{x+1} = \frac{1}{2}$（極限存在，此為可去不連續點）。
但 $\lim_{x \to -1} \frac{1}{x+1} = \pm\infty$，故僅在 $x = -1$ 處有垂直漸近線。

---

[q:9, type:single, ans:A]
求極限 $\lim_{x \to 2^-} \frac{x}{x-2}$ 的值為何？
(A) $-\infty$
(B) $\infty$
(C) $0$
(D) $2$
<!-- solution -->
當 $x \to 2^-$ 時，分子為正數 2，分母 $x-2$ 為趨近於 0 的負數。正數除以趨近於 0 的負數趨近於 $-\infty$。

---

[q:10, type:single, ans:C]
對於極限 $\lim_{x \to a} f(x) = L$，下列哪一個敘述是正確的？
(A) 函數在 $x = a$ 必須有定義
(B) $f(a)$ 必須等於 $L$
(C) $x$ 趨近於 $a$ 時，$x$ 不能等於 $a$
(D) 若 $f(a)$ 無定義，極限必不存在
<!-- solution -->
極限考慮的是當 $x$ 在 $a$ 附近、但 $x \neq a$ 時的趨勢。與 $x=a$ 處是否有定義無關。

---

[q:11, type:single, ans:A]
求極限 $\lim_{x \to -2^+} \frac{x+1}{x+2}$ 的值。
(A) $-\infty$
(B) $\infty$
(C) $0$
(D) $-1$
<!-- solution -->
當 $x \to -2^+$ 時，分子趨近於 $-1$，分母為趨近於 0 的正數。負數除以趨近於 0 的正數趨近於 $-\infty$。

---

[q:12, type:single, ans:B]
若一函數滿足 $\lim_{x \to 0^+} f(x) = 1$ 且 $\lim_{x \to 0^-} f(x) = -1$，試問 $\lim_{x \to 0} f(x)$ 為何？
(A) $0$
(B) 不存在
(C) $1$
(D) $-1$
<!-- solution -->
左極限與右極限不相等，故極限不存在。

---

[q:13, type:single, ans:D]
已知 $f(x) = \frac{3}{x^2}$，試問當 $x \to 0$ 時此函數的極限為何？
(A) $0$
(B) $3$
(C) $-\infty$
(D) $\infty$
<!-- solution -->
不論 $x$ 是從左側或右側趨近於 0，$x^2$ 皆為趨近於 0 的正數。故分式趨近於正無窮大 $\infty$。

---

[q:14, type:single, ans:A]
下列哪一個極限式的值為 0？
(A) $\lim_{x \to 0^+} x \ln x$
(B) $\lim_{x \to 0^+} \frac{1}{x}$
(C) $\lim_{x \to 0^+} \frac{1}{\sqrt{x}}$
(D) $\lim_{x \to 0^-} \frac{1}{x}$
<!-- solution -->
由標準極限可知，當 $x \to 0^+$ 時，雖然 $\ln x \to -\infty$，但 $x$ 增長至 0 的速度較快，其乘積之極限為 0。

---

[q:15, type:single, ans:C]
求極限 $\lim_{x \to 0^-} \frac{1}{x^3}$ 的值為何？
(A) $0$
(B) $\infty$
(C) $-\infty$
(D) 不存在
<!-- solution -->
當 $x \to 0^-$ 時，$x^3$ 為趨近於 0 的負數。倒數為趨近於 $-\infty$。

---

[q:16, type:single, ans:B]
若 $f(x) = \frac{x^2 - 4}{x - 2}$，當 $x \to 2$ 時函數的極限為何？
(A) $2$
(B) $4$
(C) $0$
(D) 不存在
<!-- solution -->
$\lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x+2) = 2+2 = 4$。

---

[q:17, type:single, ans:A]
垂直漸近線是指函數圖形趨近於哪一種直線的現象？
(A) 垂直於 $x$ 軸的直線 $x = c$
(B) 平行於 $x$ 軸的直線 $y = c$
(C) 直線 $y = x$
(D) 原點
<!-- solution -->
垂直漸近線是一條形如 $x = c$ 的垂直線。

---

[q:18, type:single, ans:D]
已知 $\lim_{x \to a^+} f(x) = \infty$ 且 $\lim_{x \to a^-} f(x) = \infty$，試問 $\lim_{x \to a} f(x)$ 為何？
(A) 不存在
(B) $0$
(C) $-\infty$
(D) $\infty$
<!-- solution -->
兩側單邊極限皆為 $\infty$，故極限為 $\infty$。

---

[q:19, type:single, ans:B]
求極限 $\lim_{x \to 4} \frac{1}{(x-4)^2}$ 的值。
(A) $0$
(B) $\infty$
(C) $-\infty$
(D) 不存在
<!-- solution -->
分母為完全平方項，趨近於 0 的正數，故分式趨近於 $\infty$。

---

[q:20, type:single, ans:C]
已知 $f(x) = \frac{x}{|x|}$，試問 $\lim_{x \to 0} f(x)$ 之極限為何？
(A) $1$
(B) $-1$
(C) 不存在
(D) $0$
<!-- solution -->
左極限為 $-1$（因 $x<0$ 時 $\frac{x}{-x} = -1$）。
右極限為 $1$（因 $x>0$ 時 $\frac{x}{x} = 1$）。
兩者不相等，極限不存在。

---

[q:21, type:single, ans:B]
已知 $f(x) = x+2$，當 $x \to 1$ 時函數的極限為何？
(A) $1$
(B) $3$
(C) $2$
(D) $0$
<!-- solution -->
直接代入：$1+2 = 3$。

---

[q:22, type:single, ans:A]
求極限 $\lim_{x \to 0} (x^2 + 1)$ 的值。
(A) $1$
(B) $0$
(C) $2$
(D) $\infty$
<!-- solution -->
直接代入 $x=0 \implies 0^2 + 1 = 1$。

---

[q:23, type:single, ans:C]
已知 $\lim_{x \to 3} f(x) = 5$，試問此函數在 $x=3$ 處的值 $f(3)$ 必須為多少？
(A) 必為 $5$
(B) 必無定義
(C) 不一定
(D) 必為 $0$
<!-- solution -->
極限與該點的函數值無關。

---

[q:24, type:single, ans:B]
求極限 $\lim_{x \to 2^+} \frac{1}{x-2}$。
(A) $-\infty$
(B) $\infty$
(C) $0$
(D) $2$
<!-- solution -->
當 $x \to 2^+$ 時，$x-2$ 趨近於 $0^+$，倒數趨近於 $\infty$。

---

[q:25, type:single, ans:D]
下列關於單邊極限的敘述何者錯誤？
(A) $\lim_{x \to c^+} f(x)$ 代表從右側趨近
(B) $\lim_{x \to c^-} f(x)$ 代表從左側趨近
(C) 單邊極限存在不代表雙邊極限存在
(D) 雙邊極限存在不代表單邊極限存在
<!-- solution -->
若雙邊極限存在，則兩個單邊極限必存在且相等。故 D 選項錯誤。

---

[q:26, type:single, ans:A]
求極限 $\lim_{x \to 0} \frac{x^2}{x}$ 的值。
(A) $0$
(B) $1$
(C) 不存在
(D) $\infty$
<!-- solution -->
$\lim_{x \to 0} x = 0$。

---

[q:27, type:single, ans:B]
已知 $f(x) = 2x$，若 $\lim_{x \to 4} f(x) = L$，則 $L$ 為多少？
(A) $4$
(B) $8$
(C) $2$
(D) $6$
<!-- solution -->
代入 $x=4 \implies 2(4) = 8$。

---

[q:28, type:single, ans:C]
求極限 $\lim_{x \to 1^-} \frac{1}{x-1}$ 的值。
(A) $0$
(B) $\infty$
(C) $-\infty$
(D) $1$
<!-- solution -->
當 $x \to 1^-$ 時，$x-1$ 趨近於 $0^-$，倒數趨近於 $-\infty$。

---

[q:29, type:single, ans:A]
已知 $\lim_{x \to 2^-} f(x) = 4, \lim_{x \to 2^+} f(x) = 4$，則 $\lim_{x \to 2} f(x)$ 等於：
(A) $4$
(B) $2$
(C) 不存在
(D) $0$
<!-- solution -->
單邊極限相等，極限為 4。

---

[q:30, type:single, ans:D]
求極限 $\lim_{x \to 0} \frac{x+1}{x^2}$ 的值。
(A) $1$
(B) $0$
(C) $-\infty$
(D) $\infty$
<!-- solution -->
當 $x \to 0$ 時，分母為 $0^+$，分子為 1。故趨近於 $\infty$。

---

[q:31, type:fill, ans:4]
已知函數 $f(x) = \begin{cases} 2x & \text{若 } x < 2 \\ 5 & \text{若 } x \ge 2 \end{cases}$。試問左極限 $\lim_{x \to 2^-} f(x)$ 的精確值為多少？
<!-- solution -->
左極限代入第一段：$\lim_{x \to 2^-} 2x = 2(2) = 4$。

---

[q:32, type:fill, ans:2]
已知當 $x \to 3^-$ 時，函數 $f(x) \to 2$。試問極限 $\lim_{x \to 3^-} (f(x))^2 - 2$ 的精確值。
<!-- solution -->
由極限的四則運算定律知，原式之值為 $2^2 - 2 = 4 - 2 = 2$。

---

[q:33, type:fill, ans:6]
求極限 $\lim_{x \to 2} (x^2 + x)$ 的精確值。
<!-- solution -->
直接代入：$2^2 + 2 = 6$。

---

[q:34, type:fill, ans:1]
若函數 $f(x) = \frac{x^2 - 1}{x - 1}$，試求 $\lim_{x \to 1} f(x) - 1$ 的精確值。
<!-- solution -->
$\lim_{x \to 1} \frac{(x-1)(x+1)}{x-1} = \lim_{x \to 1} (x+1) = 1+1 = 2$。
最後減去 1 得：$2 - 1 = 1$。

---

[q:35, type:fill, ans:8]
已知極限 $\lim_{x \to 4} (2x) = a$，試求 $a$ 的精確值。
<!-- solution -->
直接代入 $x=4$：$2(4) = 8$。

---

[q:36, type:fill, ans:2]
若 $f(x) = \begin{cases} 2 & \text{若 } x \neq 0 \\ 0 & \text{若 } x = 0 \end{cases}$，試求 $\lim_{x \to 0} f(x)$ 的精確值。
<!-- solution -->
極限考慮 $x \neq 0$ 的情況，故極限為 2。

---

[q:37, type:fill, ans:0]
求極限 $\lim_{x \to 1^+} (x-1)$ 的值。
<!-- solution -->
代入 $x=1 \implies 1 - 1 = 0$。

---

[q:38, type:fill, ans:5]
設 $f(x) = 2x + 1$，試求 $\lim_{x \to 2} f(x)$。
<!-- solution -->
代入 $x=2 \implies 2(2) + 1 = 5$。

---

[q:39, type:fill, ans:1]
已知 $\lim_{x \to 0} (x+1)$ 的值為多少？
<!-- solution -->
代入 $x=0 \implies 0 + 1 = 1$。

---

[q:40, type:fill, ans:3]
若 $\lim_{x \to 1^-} f(x) = 3$，試求左極限值。
<!-- solution -->
極限值即為 3。

---

[q:41, type:fill, ans:9]
求 $\lim_{x \to 3} x^2$ 的值。
<!-- solution -->
$3^2 = 9$。

---

[q:42, type:fill, ans:4]
已知 $f(x) = x+3$，求 $\lim_{x \to 1} f(x)$ 的值。
<!-- solution -->
$1+3 = 4$。

---

[q:43, type:fill, ans:10]
若 $\lim_{x \to 2} (x^2 + 3x) = b$，求 $b$ 的值。
<!-- solution -->
$2^2 + 3(2) = 4 + 6 = 10$。

---

[q:44, type:fill, ans:2]
已知 $\lim_{x \to 0} \frac{x^2 + 2x}{x}$ 的值。
<!-- solution -->
化簡為 $x+2 \implies 0+2 = 2$。

---

[q:45, type:fill, ans:1]
若 $f(x) = c$ 為常數函數且 $f(0) = 1$，求 $\lim_{x \to 4} f(x)$ 的值。
<!-- solution -->
常數函數極限恆為 1。

---

[q:46, type:fill, ans:0]
求極限 $\lim_{x \to 0} x^3$。
<!-- solution -->
$0^3 = 0$。

---

[q:47, type:fill, ans:5]
已知 $\lim_{x \to 1} (5x)$ 的值。
<!-- solution -->
$5(1) = 5$。

---

[q:48, type:fill, ans:7]
若 $\lim_{x \to 2} (x+5) = c$，試求 $c$ 的值。
<!-- solution -->
$2+5 = 7$。

---

[q:49, type:fill, ans:1]
已知 $\lim_{x \to 0} \cos x = d$，求 $d$ 的值。
<!-- solution -->
$\cos 0 = 1$。

---

[q:50, type:fill, ans:1]
若 $\lim_{x \to 2} \frac{x}{2} = e$，試求 $e$ 的值。
<!-- solution -->
$2/2 = 1$。
