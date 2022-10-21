print("s1a19 李景霖\n")
# Python 列表(List)小遊戲

# 輸入十個整數、存入一個名為people清單中（表示我們的宴客人數）：
people = []
for i in range(10):
    i = int(input("輸入數字(1-10): "))
    people.append(i)
print(f"列表順序是: {people}")
print(end="\n")

# 之後會有五次詢問
# 每次會輸入清單開始和結束的位置，再輸出從開始到結束位置的總和
for questions in range(5):
    a = int(input("開頭在哪裡(1-10): "))
    b = int(input("結尾在哪裡(1-10): "))
    print("列表順序是: ",people[a-1:b])
    print("數字總和是: ",sum(people[a-1:b]))
    print(end="\n")