print("s1a19 李景霖\n")

def function1(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total

def function2(number):
    total = 0
    i = 1
    while i < number + 1:
        if i % 2 == 0:
            total += i
        i += 1
    return total

print("\"利用for循環計算1+2+3...+n的值\"")
n = int(input("請輸入n的值: "))
print(f"1+2+3...+n的總和是: {function1(n)}")

print("\"利用while循環計算1~n的值\"")
n = int(input("請輸入n的值: "))
print(f"1~n以內所有偶數的總和是: {function2(n)}")