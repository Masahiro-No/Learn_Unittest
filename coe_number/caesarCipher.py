def caesarCipher(s, k):
    new=''
    for i in s:
        if i.isalpha(): # ถ้า i เป็นตัวอักษร
            if i.islower(): # ถ้า i เป็นตัวอักษรพิมพ์เล็ก
                new+=chr(((ord(i)-ord('a')+k)%26)+ord('a')) # ใช้ ord เพื่อเปลี่ยน i ให้เป็น ascii value เอามาคำนวณ แล้วเอามาเปลี่ยนกลับเป็นตัวอักษร
            elif i.isupper(): # ถ้า i เป็นตัวอักษรพิมพ์ใหญ่
                new+=chr(((ord(i)-ord('A')+k)%26)+ord('A')) # ใช้ ord เพื่อเปลี่ยน i ให้เป็น ascii value เอามาคำนวณ แล้วเอามาเปลี่ยนกลับเป็นตัวอักษร
            #  mod 26 เพราะมี 26 ตัวอักษร และ +ord('a') หรือ +ord('A') เพื่อเอาค่าที่คำนวณได้มาเปลี่ยนกลับให้อยู่ในช่วงตัวอักษรแบบเดิม
        else:
            new+=i # ถ้า i ไม่ใช่ตัวอักษร ให้เพิ่ม i ใน new โดยไม่เปลี่ยนแปลง
    return new

print(caesarCipher("middle-Outz", 2)) # ควรได้ okffng-Qwvb
print(caesarCipher("Hello_World!", 4)) # ควรได้ Lipps_Asvph!
print(caesarCipher("A", 1)) # ควรได้ B
print(caesarCipher("Z", 1)) # ควรได้ A
print(caesarCipher("a", 1)) # ควรได้ b
print(caesarCipher("z", 1)) # ควรได้ a
print(caesarCipher("AaZz", 1)) # ควรได้ BbAa
print(caesarCipher("A", -1)) # ควรได้ Z
print(caesarCipher("a", -1)) # ควรได้ z
print(caesarCipher("Z", -1)) # ควรได้ Y
print(caesarCipher("AaZz", 4)) # ควรได้ EeDd
print(caesarCipher("   ", 5)) # ควรได้
print(caesarCipher("1234567890", 6)) # ควรได้ 1234567890
print(caesarCipher("" , 7)) # ควรได้ ว่าง
print(caesarCipher("a", 0)) # ควรได้ a
print(caesarCipher("A", 0)) # ควรได้ A
print(caesarCipher(",c,c,vsdlss/xkf", 3)) # ควรได้ ,f,f,yvguv/vni
