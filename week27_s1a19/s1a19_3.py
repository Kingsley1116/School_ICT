print("s1a19 李景霖\n")

def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
# 調用函數
ans = triangle(4,5,6)
if ans:
    print("這是三角形")
else:
    print("這不是三角形")