print("s1a19 李景霖\n")

List = []
i = 1

while True:
    print(f"第 {i} 場")
    name = input("請輸入物品名稱: ")

    if name.lower() == "stop":
        break

    cost = int(input("請輸入物品價格: "))
    List.extend([name, cost])
    i += 1

print(f"拍賣列表是: {List}")
print(f"拍賣物品有: {List[::2]}")