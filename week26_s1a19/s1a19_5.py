print("s1a19 李景霖\n")

List = []
try:
    times = int(input("請輸入次數: "))

    for i in range(times):
        try:
            number = eval(input("請輸入數字: "))
            List.append(number)
        except:
            exit("請輸入數字!")

    print(f"平均值是: {sum(List) / len(List)}")
    print(f"最大值是: {max(List)}")
except:
    exit("請輸入整數!")