import sys

file_path = '/home/toymsi/documents/examination/大學入學考試/md/115/學測/數B.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Locate the indices
# Line 142 (index 141): group image
lines[141] = '<br><div style=\"text-align: center;\"><img src=\"/images/ceec/115/學測/數B/group18_fig5.webp\" style=\"max-width: 400px;\" alt=\"星軌照片示意圖\"></div><br>\n'

# Line 146 (index 145): Q18 duplicate/broken image to delete
lines[145] = ''

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Updates saved successfully.")
