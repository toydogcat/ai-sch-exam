# 微積分題庫 - 3.8 節：牛頓法

本節收錄 3.8 節相關題目。

---

[q:1, type:single, ans:C]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 直接收斂到精確根
(B) 收斂速度變快
(C) 無法繼續進行疊代（分母為 0）
(D) 跳轉到另一根
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:2, type:single, ans:A]
利用牛頓法求 $x^2 - 3 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $2.0$
(B) $-2$
(C) $3$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 3, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 3}{2x_1} = 1 - \frac{1 - 3}{2} = \frac{1 + 3}{2}$。

---

[q:3, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:4, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:5, type:single, ans:B]
利用牛頓法求 $x^2 - 6 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-5$
(B) $3.5$
(C) $6$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 6, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 6}{2x_1} = 1 - \frac{1 - 6}{2} = \frac{1 + 6}{2}$。

---

[q:6, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:7, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:8, type:single, ans:B]
利用牛頓法求 $x^2 - 9 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-8$
(B) $5.0$
(C) $9$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 9, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 9}{2x_1} = 1 - \frac{1 - 9}{2} = \frac{1 + 9}{2}$。

---

[q:9, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:10, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:11, type:single, ans:B]
利用牛頓法求 $x^2 - 12 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-11$
(B) $6.5$
(C) $12$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 12, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 12}{2x_1} = 1 - \frac{1 - 12}{2} = \frac{1 + 12}{2}$。

---

[q:12, type:single, ans:B]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:13, type:single, ans:C]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 直接收斂到精確根
(B) 收斂速度變快
(C) 無法繼續進行疊代（分母為 0）
(D) 跳轉到另一根
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:14, type:single, ans:A]
利用牛頓法求 $x^2 - 15 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $8.0$
(B) $-14$
(C) $15$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 15, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 15}{2x_1} = 1 - \frac{1 - 15}{2} = \frac{1 + 15}{2}$。

---

[q:15, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:16, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:17, type:single, ans:B]
利用牛頓法求 $x^2 - 18 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-17$
(B) $9.5$
(C) $18$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 18, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 18}{2x_1} = 1 - \frac{1 - 18}{2} = \frac{1 + 18}{2}$。

---

[q:18, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:19, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:20, type:single, ans:B]
利用牛頓法求 $x^2 - 21 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-20$
(B) $11.0$
(C) $21$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 21, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 21}{2x_1} = 1 - \frac{1 - 21}{2} = \frac{1 + 21}{2}$。

---

[q:21, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:22, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:23, type:single, ans:B]
利用牛頓法求 $x^2 - 24 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-23$
(B) $12.5$
(C) $24$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 24, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 24}{2x_1} = 1 - \frac{1 - 24}{2} = \frac{1 + 24}{2}$。

---

[q:24, type:single, ans:B]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:25, type:single, ans:C]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 直接收斂到精確根
(B) 收斂速度變快
(C) 無法繼續進行疊代（分母為 0）
(D) 跳轉到另一根
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:26, type:single, ans:A]
利用牛頓法求 $x^2 - 27 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $14.0$
(B) $-26$
(C) $27$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 27, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 27}{2x_1} = 1 - \frac{1 - 27}{2} = \frac{1 + 27}{2}$。

---

[q:27, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:28, type:single, ans:D]
利用牛頓法求解方程式時，若 $f'(x_n) = 0$，疊代將會發生什麼情況？
(A) 跳轉到另一根
(B) 收斂速度變快
(C) 直接收斂到精確根
(D) 無法繼續進行疊代（分母為 0）
<!-- solution -->
當導函數為 0 時分母為 0，疊代無法繼續。

---

[q:29, type:single, ans:B]
利用牛頓法求 $x^2 - 30 = 0$ 的根，若 $x_1 = 1$，疊代一次後 $x_2$ 的值為何？
(A) $-29$
(B) $15.5$
(C) $30$
(D) $2$
<!-- solution -->
$f(x) = x^2 - 30, f'(x) = 2x \implies x_2 = x_1 - \frac{x_1^2 - 30}{2x_1} = 1 - \frac{1 - 30}{2} = \frac{1 + 30}{2}$。

---

[q:30, type:single, ans:A]
牛頓法（Newton's Method）的遞迴疊代公式為何？
(A) $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
(B) $x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
(C) $x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
(D) $x_{n+1} = x_n - f(x_n)$
<!-- solution -->
牛頓法遞迴式公式為 $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。

---

[q:31, type:fill, ans:16]
已知 $f(x) = x^2 - 31$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (31)}{2} = \frac{1 + 31}{2} = 16$。

---

[q:32, type:fill, ans:9.0]
已知 $f(x) = x^2 - 17$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 17}{2} = \frac{1 + 17}{2}$。

---

[q:33, type:fill, ans:18]
已知 $f(x) = x^2 - 35$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (35)}{2} = \frac{1 + 35}{2} = 18$。

---

[q:34, type:fill, ans:10.0]
已知 $f(x) = x^2 - 19$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 19}{2} = \frac{1 + 19}{2}$。

---

[q:35, type:fill, ans:20]
已知 $f(x) = x^2 - 39$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (39)}{2} = \frac{1 + 39}{2} = 20$。

---

[q:36, type:fill, ans:11.0]
已知 $f(x) = x^2 - 21$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 21}{2} = \frac{1 + 21}{2}$。

---

[q:37, type:fill, ans:22]
已知 $f(x) = x^2 - 43$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (43)}{2} = \frac{1 + 43}{2} = 22$。

---

[q:38, type:fill, ans:12.0]
已知 $f(x) = x^2 - 23$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 23}{2} = \frac{1 + 23}{2}$。

---

[q:39, type:fill, ans:24]
已知 $f(x) = x^2 - 47$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (47)}{2} = \frac{1 + 47}{2} = 24$。

---

[q:40, type:fill, ans:13.0]
已知 $f(x) = x^2 - 25$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 25}{2} = \frac{1 + 25}{2}$。

---

[q:41, type:fill, ans:26]
已知 $f(x) = x^2 - 51$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (51)}{2} = \frac{1 + 51}{2} = 26$。

---

[q:42, type:fill, ans:14.0]
已知 $f(x) = x^2 - 27$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 27}{2} = \frac{1 + 27}{2}$。

---

[q:43, type:fill, ans:28]
已知 $f(x) = x^2 - 55$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (55)}{2} = \frac{1 + 55}{2} = 28$。

---

[q:44, type:fill, ans:15.0]
已知 $f(x) = x^2 - 29$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 29}{2} = \frac{1 + 29}{2}$。

---

[q:45, type:fill, ans:30]
已知 $f(x) = x^2 - 59$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (59)}{2} = \frac{1 + 59}{2} = 30$。

---

[q:46, type:fill, ans:16.0]
已知 $f(x) = x^2 - 31$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 31}{2} = \frac{1 + 31}{2}$。

---

[q:47, type:fill, ans:32]
已知 $f(x) = x^2 - 63$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (63)}{2} = \frac{1 + 63}{2} = 32$。

---

[q:48, type:fill, ans:17.0]
已知 $f(x) = x^2 - 33$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 33}{2} = \frac{1 + 33}{2}$。

---

[q:49, type:fill, ans:34]
已知 $f(x) = x^2 - 67$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - (67)}{2} = \frac{1 + 67}{2} = 34$。

---

[q:50, type:fill, ans:18.0]
已知 $f(x) = x^2 - 35$。若 $x_1 = 1$，求利用牛頓法疊代一次後的 $x_2$ 值。
<!-- solution -->
$x_2 = 1 - \frac{1 - 35}{2} = \frac{1 + 35}{2}$。
