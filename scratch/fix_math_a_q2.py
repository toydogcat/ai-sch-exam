import sys

file_path = '/home/toymsi/documents/examination/大學入學考試/md/115/學測/數A.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix spacing in lines 18, 20-24 (indices 17, 19-23)
lines[17] = '對任一實數 $a$，令 $[a]$ 代表滿足 $[a] \\le a < [a]+1$ 的整數，例如：$[3]=3, [3.1]=3, [-3.1]=-4$。\n'
lines[19] = '(1) $f(-20) \\le f(0) < f(1)$\n'
lines[20] = '(2) $f(-20) < f(1) \\le f(0)$\n'
lines[21] = '(3) $f(1) < f(-20) \\le f(0)$\n'
lines[22] = '(4) $f(0) < f(-20) \\le f(1)$\n'
lines[23] = '(5) $f(0) \\le f(1) < f(-20)$\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Math A Question 2 spacing fixes implemented.")
