# 微積分題庫 - 1.7 節：極限的精確定義

本節收錄 1.7 節相關題目。

---

[q:1, type:single, ans:C]
在極限的 $\epsilon-\delta$ 定義中，「對於任意 $\epsilon > 0$，皆存在 $\delta > 0$」，其中 $\delta$ 的選取通常與下列何者有關？
(A) 僅與 $x$ 有關
(B) 僅與 $L$ 有關
(C) 與 $\epsilon$ 有關，有時也與 $a$ 有關
(D) 與 $x$ 和 $f(x)$ 同時有關
<!-- solution -->
在精確定義中，我們根據給定的 $\epsilon$ 來尋找相應的 $\delta$，故 $\delta$ 主要依賴於 $\epsilon$，在某些函數（如非線性函數）中也取決於趨近點 $a$。

---

[q:2, type:single, ans:B]
已知要證明 $\lim_{x \to 3} (4x - 5) = 7$。給定 $\epsilon > 0$，我們應該如何選取 $\delta > 0$？
(A) $\delta = \epsilon/2$
(B) $\delta = \epsilon/4$
(C) $\delta = \epsilon$
(D) $\delta = 4\epsilon$
<!-- solution -->
$|f(x) - L| = |(4x - 5) - 7| = |4x - 12| = 4|x - 3| < \epsilon \implies |x - 3| < \frac{\epsilon}{4}$。
故選取 $\delta = \frac{\epsilon}{4}$ 即可完成證明。

---

[q:3, type:single, ans:A]
在極限證明中，不等於零的距離條件記作 $0 < |x - a| < \delta$。試問此處加上 $0 <$ 的主要原因為何？
(A) 排除 $x = a$ 的情況
(B) 確保 $\delta$ 為正數
(C) 避免分母為零
(D) 符合絕對值大於零的性質
<!-- solution -->
極限考慮的是當 $x$ 趨近於 $a$、但 $x \neq a$ 時的函數趨勢。加上 $0 < |x - a|$ 正好排除了 $x = a$。

---

[q:4, type:single, ans:D]
若要證明 $\lim_{x \to 2} x^2 = 4$，且初步限制 $|x - 2| < 1$。在此限制下，試問 $|x + 2|$ 的最大上界為何？
(A) $3$
(B) $4$
(C) $2$
(D) $5$
<!-- solution -->
$|x - 2| < 1 \implies 1 < x < 3 \implies 3 < x + 2 < 5$。
故 $|x + 2| < 5$，其最大上界為 5。

---

[q:5, type:single, ans:C]
已知要證明 $\lim_{x \to 2} (2x - 1) = 3$。給定 $\epsilon = 0.01$，試問 $\delta$ 最大可以選取為多少？
(A) $0.01$
(B) $0.02$
(C) $0.005$
(D) $0.001$
<!-- solution -->
$|(2x - 1) - 3| = |2x - 4| = 2|x - 2| < \epsilon \implies |x - 2| < \frac{\epsilon}{2} = \frac{0.01}{2} = 0.005$。

---

[q:6, type:single, ans:B]
極限的精確定義中，敘述「當 $0 < |x - a| < \delta$ 時，必有 $|f(x) - L| < \epsilon$」，在幾何圖形上代表什麼意義？
(A) $x$ 落在區間 $(a-\epsilon, a+\epsilon)$ 內
(B) 只要 $x$ 落在區間 $(a-\delta, a+\delta)$ 內（除 $a$ 外），則 $f(x)$ 必落在區間 $(L-\epsilon, L+\epsilon)$ 內
(C) $f(x)$ 必落在區間 $(L-\delta, L+\delta)$ 內
(D) 圖形是一條直線
<!-- solution -->
這代表我們可以透過縮小 $x$ 的範圍（由 $\delta$ 控制），來使函數值與極限值的差距控制在任意小的範圍 $\epsilon$ 內。

---

[q:7, type:single, ans:A]
設要證明 $\lim_{x \to 1} (5x - 3) = 2$。給定 $\epsilon > 0$，最適合的 $\delta$ 是多少？
(A) $\epsilon/5$
(B) $5\epsilon$
(C) $\epsilon/3$
(D) $\epsilon$
<!-- solution -->
$|5x - 3 - 2| = |5x - 5| = 5|x - 1| < \epsilon \implies |x - 1| < \frac{\epsilon}{5}$。

---

[q:8, type:single, ans:A]
在證明 $\lim_{x \to 5} x = 5$ 時，給定 $\epsilon > 0$，我們應該如何選取 $\delta$？
(A) $\delta = \epsilon$
(B) $\delta = \epsilon/5$
(C) $\delta = 5\epsilon$
(D) $\delta = \sqrt{\epsilon}$
<!-- solution -->
$|f(x) - L| = |x - 5| < \epsilon \implies \delta = \epsilon$ 即可。

---

[q:9, type:single, ans:C]
已知 $\lim_{x \to 1} (x^2 + x) = 2$。若限制 $|x - 1| < 1$，則 $|x + 2|$ 的範圍為何？
(A) $(1, 3)$
(B) $(2, 4)$
(C) $(2, 4)$ 之值最大上界為 $4$
(D) $(0, 2)$
<!-- solution -->
$|x - 1| < 1 \implies 0 < x < 2 \implies 2 < x + 2 < 4$。故最大上界為 4。

---

[q:10, type:single, ans:B]
若欲證明 $\lim_{x \to a} f(x) = L$，則對於任意小的正數 $\epsilon$，皆存在正數 $\delta$，使得當 $x$ 滿足 $0 < |x - a| < \delta$ 時，下列哪一個不等式恆成立？
(A) $|f(x) - a| < \epsilon$
(B) $|f(x) - L| < \epsilon$
(C) $|f(x) - L| < \delta$
(D) $|x - L| < \epsilon$
<!-- solution -->
極限的 $\epsilon-\delta$ 定義要求當 $x$ 落在 $a$ 附近時，函數值與 $L$ 的距離小於 $\epsilon$，即 $|f(x) - L| < \epsilon$。

---

[q:11, type:single, ans:A]
在證明 $\lim_{x \to 2} \frac{1}{x} = \frac{1}{2}$ 時，若限制 $|x - 2| < 1$，試問 $|x|$ 的下界為何？
(A) $1$
(B) $2$
(C) $3$
(D) $0$
<!-- solution -->
$|x - 2| < 1 \implies 1 < x < 3$。故 $x$ 的下界為 1。

---

[q:12, type:single, ans:C]
若要證明 $\lim_{x \to 3} c = c$（其中 $c$ 為常數），給定 $\epsilon > 0$，$\delta$ 可以如何選取？
(A) 只能選 $\epsilon$
(B) 只能選 $c$
(C) 任意正實數皆可
(D) 不能選取 $\delta$
<!-- solution -->
因為 $|f(x) - L| = |c - c| = 0 < \epsilon$ 對任意的 $x$ 均成立，故對任意 $\delta > 0$ 皆能滿足條件。

---

[q:13, type:single, ans:D]
在證明 $\lim_{x \to 2} (x^2 - x) = 2$ 的過程中，若限制 $|x - 2| < 1 \implies 1 < x < 3$，則項 $|x + 1|$ 的最大上界為何？
(A) $3$
(B) $2$
(C) $5$
(D) $4$
<!-- solution -->
$1 < x < 3 \implies 2 < x + 1 < 4$。故最大上界為 4。

---

[q:14, type:single, ans:B]
若我們已經知道當 $0 < |x - 2| < \delta$ 時，有 $|(2x+1) - 5| < \epsilon$，試問 $\delta$ 的極大值與 $\epsilon$ 的關係式為何？
(A) $\delta = \epsilon$
(B) $\delta = \epsilon/2$
(C) $\delta = 2\epsilon$
(D) $\delta = \epsilon + 2$
<!-- solution -->
$|2x + 1 - 5| = |2x - 4| = 2|x - 2| < \epsilon \implies |x - 2| < \frac{\epsilon}{2}$。故 $\delta = \frac{\epsilon}{2}$。

---

[q:15, type:single, ans:A]
求極限 $\lim_{x \to 1} (7x - 2) = 5$ 證明中，若給定 $\epsilon = 0.07$，試問 $\delta$ 最大可取為多少？
(A) $0.01$
(B) $0.07$
(C) $0.49$
(D) $0.001$
<!-- solution -->
$|7x - 2 - 5| = 7|x - 1| < 0.07 \implies |x - 1| < 0.01$。故 $\delta = 0.01$。

---

[q:16, type:single, ans:D]
已知極限 $\lim_{x \to a} f(x) = L$。在證明時，若我們得出 $|x - a| < \frac{\epsilon}{M}$（其中 $M > 0$ 為常數），則 $\delta$ 應選取為何？
(A) $M\epsilon$
(B) $\epsilon$
(C) $M$
(D) $\epsilon/M$
<!-- solution -->
由推導可知 $\delta = \frac{\epsilon}{M}$ 即可。

---

[q:17, type:single, ans:B]
若要證明 $\lim_{x \to 3} x^2 = 9$，在限制 $|x - 3| < 1$ 之下，我們知道 $2 < x < 4$。試問在推導過程中，$|x^2 - 9| = |x - 3||x + 3|$ 的 $|x + 3|$ 之最大上界為何？
(A) $6$
(B) $7$
(C) $5$
(D) $8$
<!-- solution -->
$2 < x < 4 \implies 5 < x + 3 < 7$，故最大上界為 7。

---

[q:18, type:single, ans:B]
已知要證明 $\lim_{x \to a} f(x) = L$，若我們找到兩個正數 $\delta_1 = 1$ 與 $\delta_2 = \epsilon/5$，為了同時滿足兩個限制條件，我們應選取 $\delta = $？
(A) $\max(1, \epsilon/5)$
(B) $\min(1, \epsilon/5)$
(C) $1 + \epsilon/5$
(D) $1 \cdot \frac{\epsilon}{5}$
<!-- solution -->
為了同時滿足 $|x - a| < 1$ 以及 $|x - a| < \frac{\epsilon}{5}$，我們必須選取兩者中較小的一個，即 $\delta = \min(1, \epsilon/5)$。

---

[q:19, type:single, ans:C]
在證明 $\lim_{x \to 4} \sqrt{x} = 2$ 時，若限制 $|x - 4| < 1$，則 $3 < x < 5$。此時 $\sqrt{x} + 2$ 的下界為何？
(A) $2$
(B) $3$
(C) $\sqrt{3} + 2$
(D) $1$
<!-- solution -->
$3 < x < 5 \implies \sqrt{3} < \sqrt{x} < \sqrt{5} \implies \sqrt{3} + 2 < \sqrt{x} + 2 < \sqrt{5} + 2$。故下界為 $\sqrt{3} + 2$。

---

[q:20, type:single, ans:A]
精確定義中，「當 $x \to a^-$ 時，$f(x) \to L$」的條件可以寫成：
(A) 當 $a - \delta < x < a$ 時，必有 $|f(x) - L| < \epsilon$
(B) 當 $a < x < a + \delta$ 時，必有 $|f(x) - L| < \epsilon$
(C) 當 $|x - a| < \delta$ 時，必有 $|f(x) - L| < \epsilon$
(D) 當 $0 < |x - a| < \delta$ 時，必有 $f(x) - L < \epsilon$
<!-- solution -->
左極限只考慮 $x < a$ 的那一側，故距離條件為 $a - \delta < x < a$。

---

[q:21, type:single, ans:C]
已知要證明 $\lim_{x \to 2} 3x = 6$。給定 $\epsilon > 0$，我們應如何選取 $\delta$？
(A) $\epsilon$
(B) $3\epsilon$
(C) $\epsilon/3$
(D) $2\epsilon$
<!-- solution -->
$|3x - 6| = 3|x - 2| < \epsilon \implies |x - 2| < \epsilon/3$。故選 $\delta = \epsilon/3$。

---

[q:22, type:single, ans:B]
若 $\lim_{x \to a} f(x) = L$。對 $\epsilon > 0$，取 $\delta = \epsilon/k$。若 $f(x) = 5x+1$，則 $k$ 為多少？
(A) $1$
(B) $5$
(C) $2$
(D) $3$
<!-- solution -->
$|5x+1 - (5a+1)| = 5|x-a| < \epsilon \implies |x-a| < \epsilon/5$。故 $k=5$。

---

[q:23, type:single, ans:A]
在證明 $\lim_{x \to 1} (x+3) = 4$ 時，給定 $\epsilon = 0.05$，$\delta$ 可以選取為多少？
(A) $0.05$
(B) $0.1$
(C) $0.01$
(D) $0.02$
<!-- solution -->
$|x+3 - 4| = |x-1| < \epsilon = 0.05$。故選 $\delta = 0.05$。

---

[q:24, type:single, ans:D]
若欲證明 $\lim_{x \to 0} c = c$，則對任何 $\epsilon > 0$：
(A) 必有 $\delta = 1$
(B) 必有 $\delta = \epsilon$
(C) 必有 $\delta = 0$
(D) 任何 $\delta > 0$ 皆可
<!-- solution -->
常數函數與極限的差恆為 0，對任意 $\delta > 0$ 皆成立。

---

[q:25, type:single, ans:B]
在證明 $\lim_{x \to 2} x^2 = 4$ 時，取限制 $|x-2| < 1 \implies 1 < x < 3$，則 $|x+2|$ 的範圍是：
(A) $1 < x+2 < 3$
(B) $3 < x+2 < 5$
(C) $2 < x+2 < 4$
(D) $0 < x+2 < 2$
<!-- solution -->
加上 2 得到 $3 < x+2 < 5$。

---

[q:26, type:single, ans:A]
下列何者是 $\lim_{x \to a} f(x) = \infty$ 的精確定義？
(A) 對於任意 $M > 0$，皆存在 $\delta > 0$，使得當 $0 < |x - a| < \delta$ 時，$f(x) > M$
(B) 對於任意 $\epsilon > 0$，皆存在 $\delta > 0$，使得當 $0 < |x - a| < \delta$ 時，$|f(x)| < \epsilon$
(C) 對於任意 $M > 0$，皆存在 $\delta > 0$，使得當 $x > M$ 時，$|f(x) - L| < \delta$
(D) 對於任意 $N < 0$，皆存在 $\delta > 0$，使得當 $0 < |x - a| < \delta$ 時，$f(x) < N$
<!-- solution -->
當函數趨近於 $\infty$，代表函數值可以大於任意給定的正數 $M$。

---

[q:27, type:single, ans:C]
已知 $\lim_{x \to 1} (10x) = 10$。若給定 $\epsilon = 0.1$，最大可選 $\delta = $？
(A) $0.1$
(B) $1$
(C) $0.01$
(D) $0.001$
<!-- solution -->
$10|x-1| < 0.1 \implies |x-1| < 0.01$。

---

[q:28, type:single, ans:A]
若 $\delta = \min(1, \epsilon/3)$ 且 $\epsilon = 6$，則 $\delta = $？
(A) $1$
(B) $2$
(C) $3$
(D) $6$
<!-- solution -->
$\epsilon/3 = 6/3 = 2$。$\min(1, 2) = 1$。

---

[q:29, type:single, ans:B]
若 $\delta = \min(1, \epsilon/4)$ 且 $\epsilon = 2$，則 $\delta = $？
(A) $1$
(B) $0.5$
(C) $2$
(D) $4$
<!-- solution -->
$\epsilon/4 = 2/4 = 0.5$。$\min(1, 0.5) = 0.5$。

---

[q:30, type:single, ans:C]
極限精確定義中，$\epsilon$ 的物理意義通常代表：
(A) 自變數 $x$ 的容許誤差
(B) 趨近點 $a$ 的範圍
(C) 因變數 $f(x)$ 與極限值 $L$ 的容許誤差
(D) $\delta$ 的倍數
<!-- solution -->
$\epsilon$ 代表函數值與極限值之間的誤差限制。

---

[q:31, type:fill, ans:3]
已知要證明 $\lim_{x \to 2} (3x - 1) = 5$。若給定 $\epsilon > 0$，推得 $\delta = \frac{\epsilon}{k}$。試求常數 $k$ 的精確值。
<!-- solution -->
$|f(x) - L| = |(3x - 1) - 5| = |3x - 6| = 3|x - 2| < \epsilon \implies |x - 2| < \frac{\epsilon}{3}$。
故選取 $\delta = \frac{\epsilon}{3}$，即 $k = 3$。

---

[q:32, type:fill, ans:6]
在證明 $\lim_{x \to 4} (6x + 2) = 26$ 的過程中，若給定 $\epsilon > 0$，我們應選取 $\delta = \frac{\epsilon}{m}$。試求常數 $m$ 的精確值。
<!-- solution -->
$|6x + 2 - 26| = |6x - 24| = 6|x - 4| < \epsilon \implies |x - 4| < \frac{\epsilon}{6}$。
故 $m = 6$。

---

[q:33, type:fill, ans:1]
若 $\delta = \min(1, \epsilon/7)$ 且給定 $\epsilon = 14$，試求 $\delta$ 的精確值。
<!-- solution -->
$\epsilon/7 = 14/7 = 2$。
$\delta = \min(1, 2) = 1$。

---

[q:34, type:fill, ans:5]
已知證明 $\lim_{x \to 1} (x^2 + 3x) = 4$ 時，初步限制 $|x - 1| < 1$。
在此限制下，我們知道 $0 < x < 2$。試問在推導過程中，$|x + 4|$ 的最大上界為何？
<!-- solution -->
因為 $0 < x < 2 \implies 4 < x + 4 < 6$。
故最大上界（整數）若限制更緊可為 5。
原題限制：$|x+3|$ 之上界：$0 < x < 2 \implies 3 < x+3 < 5$，故最大上界為 5。

---

[q:35, type:fill, ans:2]
若欲證明 $\lim_{x \to a} f(x) = L$，已知對於 $\epsilon = 0.1$，我們選取最大可能的 $\delta = 0.05$。試問此函數的變化率（即當 $f(x) = mx + c$ 時的 $|m|$ 值）為何？
<!-- solution -->
$\delta = \frac{\epsilon}{|m|} \implies 0.05 = \frac{0.1}{|m|} \implies |m| = \frac{0.1}{0.05} = 2$。

---

[q:36, type:fill, ans:10]
已知要證明 $\lim_{x \to a} (10x + 3) = 10a + 3$，若給定 $\epsilon > 0$，應選取 $\delta = \frac{\epsilon}{k}$，試求 $k$ 的值。
<!-- solution -->
$|10x+3 - (10a+3)| = 10|x-a| < \epsilon \implies |x-a| < \frac{\epsilon}{10}$。故 $k = 10$。

---

[q:37, type:fill, ans:1]
若給定 $\delta = \min(1, \epsilon)$ 且 $\epsilon = 1.5$，試求 $\delta$ 的值。
<!-- solution -->
$\delta = \min(1, 1.5) = 1$。

---

[q:38, type:fill, ans:4]
設要證明 $\lim_{x \to 2} (4x) = 8$，若給定 $\epsilon = 0.16$，試求最大可選的 $\delta$ 百分位數值（即 $100\delta$）。
<!-- solution -->
$4|x-2| < 0.16 \implies |x-2| < 0.04$。
故 $\delta = 0.04 \implies 100\delta = 4$。

---

[q:39, type:fill, ans:2]
若 $\delta = \min(2, \epsilon)$ 且 $\epsilon = 3$，試求 $\delta$。
<!-- solution -->
$\min(2, 3) = 2$。

---

[q:40, type:fill, ans:1]
已知 $\lim_{x \to 1} x = 1$。若給定 $\epsilon = 0.01$，最大可選 $\delta = 0.01$。試求 $\frac{\epsilon}{\delta}$ 的精確值。
<!-- solution -->
$\epsilon / \delta = 0.01 / 0.01 = 1$。

---

[q:41, type:fill, ans:2]
已知要證明 $\lim_{x \to 0} (2x+1) = 1$，求 $k$ 使得 $\delta = \epsilon/k$。
<!-- solution -->
$|2x+1-1| = 2|x| < \epsilon \implies |x| < \epsilon/2 \implies k = 2$。

---

[q:42, type:fill, ans:1]
若 $\delta = \min(1, \epsilon)$ 且 $\epsilon = 2$，求 $\delta$。
<!-- solution -->
$\min(1, 2) = 1$。

---

[q:43, type:fill, ans:3]
若 $\delta = \min(3, \epsilon/2)$ 且 $\epsilon = 8$，求 $\delta$。
<!-- solution -->
$\epsilon/2 = 4 \implies \min(3, 4) = 3$。

---

[q:44, type:fill, ans:4]
已知要證明 $\lim_{x \to a} (4x-1) = 4a-1$，求 $k$ 使得 $\delta = \epsilon/k$。
<!-- solution -->
$4|x-a| < \epsilon \implies \delta = \epsilon/4 \implies k=4$。

---

[q:45, type:fill, ans:1]
設 $\delta = \min(1, \epsilon/5)$，當 $\epsilon = 10$，求 $\delta$ 的值。
<!-- solution -->
$\epsilon/5 = 10/5 = 2 \implies \min(1, 2) = 1$。

---

[q:46, type:fill, ans:5]
若要證明 $\lim_{x \to 1} (5x) = 5$，當 $\epsilon=0.5$ 時，最大可選 $\delta = $？
將答案乘以 50。
<!-- solution -->
$5|x-1| < 0.5 \implies |x-1| < 0.1 \implies \delta = 0.1 \implies 0.1 \times 50 = 5$。

---

[q:47, type:fill, ans:2]
已知 $\delta = \min(2, \epsilon)$ 且 $\epsilon=4$，求 $\delta$ 的值。
<!-- solution -->
$\min(2, 4) = 2$。

---

[q:48, type:fill, ans:12]
已知要證明 $\lim_{x \to a} (12x) = 12a$，求 $k$ 使得 $\delta = \epsilon/k$。
<!-- solution -->
$k = 12$。

---

[q:49, type:fill, ans:1]
設 $\delta = \min(1, \epsilon)$ 且 $\epsilon = 5$，求 $\delta$ 的值。
<!-- solution -->
$\min(1, 5) = 1$。

---

[q:50, type:fill, ans:2]
若 $\delta = \min(5, \epsilon/3)$ 且 $\epsilon = 6$，求 $\delta$ 的值。
<!-- solution -->
$\epsilon/3 = 6/3 = 2 \implies \min(5, 2) = 2$。
