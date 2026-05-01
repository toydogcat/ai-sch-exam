import re

clean_q_text = """已知實係數多項式 $f(x)$ 的次數大於 5，且其最高次項係數為正。又 $f(x)$ 在 $x=1, 2, 4$ 處有極小值，且在 $x=3, 5$ 處有極大值。根據上述，試選出正確的選項。
(A) $f(1)<f(3)$
(B) 存在實數 $a,b$ 滿足 $1<a<b<2$，使得 $f^{\prime}(a)>0$且 $f^{\prime}(b)<0$
(C) $f^{\prime\prime}(3)>0$
(D) 存在實數 $c>5$，使得 $f^{\prime}(c)>0$
(E) $f(x)$ 的次數大於 7"""

clean_q_text = clean_q_text.replace("<", "&lt;").replace(">", "&gt;")

opt_matches = re.findall(r'\(([A-G])\)\s*(.*?)(?=\s*\([A-G]\)|$)', clean_q_text, re.DOTALL)
print("opt_matches with [A-G]:", opt_matches)
