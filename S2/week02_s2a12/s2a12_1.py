print("s2a12 李景霖")

# 寫出公式
print("計算梯形的面積(公式: 上底加下底乘高除二)\n")

try:
    # 用戶輸入
    upperb: int = int(input("輸入梯形中上底(upperb)的長度(cm): "))      # 上底
    underb: int = int(input("輸入梯形中下底(underb)的長度(cm): "))      # 下底
    height: int = int(input("輸入梯形中高(height)的長度(cm): "))        # 高

    # 計算梯形面積
    trapezoid: float = ((upperb + underb) * height) / 2

    # 輸出結果
    print(f"梯形的面積是: {trapezoid}")

except ValueError:
    # 處理類型錯誤
    # 當用戶輸入文字時，會在轉換為int時報出ValueError
    # 因而使用ValueError，而不是TypeError
    print("請輸入數字!")