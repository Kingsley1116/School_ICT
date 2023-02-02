print("s1a19 李景霖\n")

# 可以用eval()替代int()
number = int(input("輸入循環次數: "))

for i in range(1, number + 1, 1):
    if i % 3 != 0:
        print(f"choikou {i}")