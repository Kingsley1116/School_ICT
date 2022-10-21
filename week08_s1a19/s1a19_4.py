print("s1a19 李景霖\n")

# 定義列表
numberList = []

# 將數字加入列表
for i in range(10):
    i = int(input("輸入任意數字: "))
    numberList.append(i)

for i in range(len(numberList)):
    a = 0
    a += numberList[i]

avg = a/len(numberList)+1

print("列表平均值: ",avg)
print("列表最大值: ",max(numberList))