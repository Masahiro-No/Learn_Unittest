def alternatingCharacters(s):
    num=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            num+=1
    return num

print(alternatingCharacters("AAAA")) # ควรได้ 3
print(alternatingCharacters("BBBBB")) # ควรได้ 4
print(alternatingCharacters("ABABABAB")) # ควรได้ 0
print(alternatingCharacters("AAABBB")) # ควรได้ 4
print(alternatingCharacters("AAABBBAABB")) # ควรได้ 6
print(alternatingCharacters("AABBAABB")) # ควรได้ 4
print(alternatingCharacters("ABABABAA")) # ควรได้ 1
print(alternatingCharacters("XYZXXQWE")) # ควรได้ 1
print(alternatingCharacters("A")) # ควรได้ 0
print(alternatingCharacters("")) # ควรได้ 0
print(alternatingCharacters("AB")) # ควรได้ 0
print(alternatingCharacters("AA")) # ควรได้ 1
print(alternatingCharacters("กกก")) # ควรได้ 2
print(alternatingCharacters(".,.,")) # ควรได้ 0
print(alternatingCharacters("       ")) # ควรได้ 6