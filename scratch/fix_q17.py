import sys

file_path = '/home/toymsi/documents/examination/大學入學考試/md/115/學測/數B.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace indices 134 to 138
lines[134] = '（一）空間中與 $y$ 軸平行的直線，在畫布上的消失點為 $(0,15)$\n'
lines[135] = '（二）空間中與 $z$ 軸平行的直線，在畫布上都與 $y$ 軸平行\n'
lines[136] = '若點 $(0,0,0)$、$(3,4,0)$、$(3,0,3)$ 繪在畫布上分別為 $(0,0)$、$(\\frac{13}{5},2)$、$(3,3)$，則點 $(3,4,3)$ 繪在畫布上的 $y$ 坐標為 ____。（化為最簡分數）\n'
# line 137 is \n already
lines[138] = '（註：右圖為三點 $(3,4,0)$、$(3,0,3)$、$(3,4,3)$ 於坐標空間的位置關係）\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Recovery complete.")
