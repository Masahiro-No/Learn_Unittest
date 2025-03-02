def funnyString(s):
    s = [ord(letter) for letter in s] # เปลี่ยน s เป็น ascii value ด้วย ord แล้วเก็บใน list
    reverse = list(reversed(s))  # ใช้ reversed() ได้เลย เพราะ s เป็น list ของตัวเลขแล้ว
    r = [abs(reverse[i] - reverse[i + 1]) for i in range(len(reverse) - 1)] # เช็คความแตกต่างของ ascii ของ reverse ตำแหน่งที่ i กับ i+1 ใน list
    s = [abs(s[i] - s[i + 1]) for i in range(len(reverse) - 1)] # เช็คความแตกต่างของ ascii ของ s ตำแหน่งที่ i กับ i+1 ใน list
    if r == s: # เช็คว่า list r และ s มีค่าเท่ากันหรือไม่
        return "Funny" # ถ้าเท่ากัน return Funny
    return "Not Funny" # ถ้าไม่เท่ากัน return Not Funny
    

print(funnyString("acxz")) # ควรได้ Funny
print(funnyString("zxc")) # ควรได้ Not Funny
print(funnyString("lmnop")) # ควรได้ Funny
print(funnyString("123456789")) # ควรได้ Funny
print(funnyString("247")) # ควรได้ Not Funny
print(funnyString(".:/")) # ควรได้ Not Funny
print(funnyString("")) # ควรได้ Funny
print(funnyString("กขฃ")) # ควรได้ Funny
print(funnyString("๑๒๓๔๕๖๗๘๙")) # ควรได้ Funny
print(funnyString("กขคง")) # ควรได้ Not Funny
print(funnyString("๑๒๓๔๕๖๗๘๙๐๑")) # ควรได้ Not Funny