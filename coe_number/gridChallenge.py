def gridChallenge(grid):
    for i in range(0,len(grid)): # วนลูปทุก row ใน grid
        grid[i]=''.join(sorted(grid[i])) # เรียงตัวอักษรในแต่ละ row แล้วเก็บใน grid ที่เป็น list ของ string
    
    for col in range(0,len(grid[0])): # วนลูปทุก col ใน grid
        anch=-999 # กำหนดค่าเริ่มต้นให้ anch ให้น้อยกว่า ord('a') ไว้เป็นตัวเช็คว่าตัวอักษรตัวถัดไปใน col มีค่ามากกว่าตัวก่อนหน้าหรือไม่
        for row in range(0,len(grid)): # วนลูปทุก row ใน grid
            if anch> ord(grid[row][col]) : # เช็คว่า ord ของตัวอักษรใน col ตำแหน่งที่ row มีค่ามากกว่า ord ของตัวอักษรใน col ตำแหน่งที่ row ก่อนหน้าหรือไม่
                return "NO" # ถ้ามีให้ return NO
            anch=ord(grid[row][col]) # ถ้าไม่มีให้กำหนดค่า anch เป็น ord ของตัวอักษรใน col ตำแหน่งที่ row
    
    return "YES" # ถ้าไม่มีให้ return YES

print(gridChallenge([',', '.', '/'])) # YES