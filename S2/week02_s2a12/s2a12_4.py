import random

print("s2a12 李景霖")

print("請猜1-100中的隨機的年齡是多少，你共有5次機會! \n")

try:
    randomNumber: int = random.randint(1, 100)

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
    print("請輸入數字!")
