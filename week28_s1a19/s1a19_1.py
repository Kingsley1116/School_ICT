print("s1a19 李景霖\n")

def guessTheHeight(sex, father, mother):
    if sex.lower() == "m":
        return (father + mother) * 1.08 / 2
    else:
        return (father * 0.923 + mother) / 2
    
print("小孩的預測身高是:",
    guessTheHeight(
        sex = input("請輸入預測小孩的性別(M/F): "),
        father = float(input("請輸入爸爸的身高: ")),
        mother = float(input("請輸入媽媽的身高: "))
    )
)