# 引入 random 模組
import random

print("s2a12 李景霖")

print("請猜1-100中的隨機的年齡是多少，你共有5次機會! \n")

try:
    # 生成隨機數
    # 兩個 argument 必須為 int(整數)
    # randint: 返回一個於範圍 [a, b] 的整數類隨機數
    randomNumber: int = random.randint(1, 100)

    # 五次機會，所以重覆五次
    i:int = 1
    while i <= 5:
        guess: int = int(input("請輸入你猜測的年齡: "))

        if guess == randomNumber:
            print("你猜對了!")
            break

        elif guess < randomNumber:
            print("你猜小了!")

        elif guess > randomNumber:
            print("你猜大了!")
        
        i += 1
    
    print(f"隨機的年齡為: {randomNumber}")

except ValueError:
    # 類型錯誤
    print("請輸入數字!")