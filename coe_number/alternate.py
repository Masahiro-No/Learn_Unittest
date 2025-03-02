import re
from itertools import combinations

def alternate(s):
    max_length = 0 # ความยาวของ substring ที่ยาวที่สุด
    for first, second in combinations(set(s), 2): # วนลูปทุกคู่ที่เป็นไปได้ของตัวอักษรที่ไม่ซ้ำกันใน s
        substring = re.sub(f"[^{first}{second}]", "", s) # ลบตัวอักษรที่ไม่ใช่ first หรือ second ออกจาก s
        if not re.search(r"(.)\1", substring): # ถ้าไม่มีตัวอักษรที่ซ้ำกันใน substring
            max_length = max(max_length, len(substring)) # หาความยาวของ substring ที่ยาวที่สุด
    return max_length

print(alternate("beabeefeab")) # ควรได้ 5
print(alternate("asdcbsdcagfsdbgdfanfghbsfdab")) # ควรได้ 8
print(alternate("ab")) # ควรได้ 2
print(alternate("abc")) # ควรได้ 2
print(alternate("abcabc")) # ควรได้ 4
print(alternate("")) # ควรได้ 0
print(alternate("a")) # ควรได้ 0
print(alternate("aabbcc")) # ควรได้ 0
print(alternate("   ")) # ควรได้ 0
print(alternate(".,.,.,")) # ควรได้ 6
print(alternate("กขกขกขกขก")) # ควรได้ 9
print(alternate("กกขขคค")) # ควรได้ 0
print(alternate("12121212")) # ควรได้ 8

