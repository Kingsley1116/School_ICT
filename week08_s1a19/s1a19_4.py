print("s1a19 李景霖\n")

# 定義列表
numberList = []

# 將數字加入列表
for i in range(10):
    a = int(input(f"輸入第{i+1}項數字: "))
    numberList.append(a)

a = 0
for i in range(len(numberList)):
    a += numberList[i]

avg = a/len(numberList)

print("列表平均值: ",avg)
print("列表最大值: ",max(numberList))
