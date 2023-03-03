print("s1a19 李景霖\n")

def calTax(price, rate):
    total = price + (price * rate)
    return total

# 調用函數
myPrice = calTax(int(input("請輸入納稅額: ")), 0.06)
print(f"總價格是: {myPrice}")