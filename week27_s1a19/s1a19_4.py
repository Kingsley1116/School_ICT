print("s1a19 李景霖\n")

def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        circumference = a + b + c
        return [True, circumference]
    else:
        return [False, None]
    
# 調用函數
ans = triangle(4,5,6)
if ans[0]:
    print(f"這是三角形!\n其周長為 {ans[1]}")
else:
    print("這不是三角形!")