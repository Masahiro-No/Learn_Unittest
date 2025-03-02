import re
from itertools import combinations

def alternate(s):
    max_length = 0 # ความยาวของ substring ที่ยาวที่สุด
    for first, second in combinations(set(s), 2): # วนลูปทุกคู่ที่เป็นไปได้ของตัวอักษรที่ไม่ซ้ำกันใน s
        substring = re.sub(f"[^{first}{second}]", "", s) # ลบตัวอักษรที่ไม่ใช่ first หรือ second ออกจาก s
        if not re.search(r"(.)\1", substring): # ถ้าไม่มีตัวอักษรที่ซ้ำกันใน substring
            max_length = max(max_length, len(substring)) # หาความยาวของ substring ที่ยาวที่สุด
    return max_length
