print("s1a19 李景霖\n")

def circumference(x, y):
    return (x + y) * 2

def area(x ,y):
    return x * y

x = int(input("請輸入長方形的長: "))
y = int(input("請輸入長方形的寬: "))
print("-----------")
print(f"長方形的同長是: {circumference(x, y)}")
print(f"長方形的面積是: {area(x, y)}")