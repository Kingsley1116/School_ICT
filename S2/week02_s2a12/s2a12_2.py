print("s2a12 李景霖")

print("計算華氏(F)與攝氏(C)溫度的轉換")
print("C = (F - 32) / 1.8")
print("F = 1.8 * C + 32\n")

temp: str = input("輸入溫度值，例如30C 或 80F: ")

match temp[-1]:
    case n if n in ["C", "c"]:
        print(f"{temp} 轉換華氏溫度是: {1.8 * float(temp[:-1]) + 32}")

    case n if n in ["F", "f"]:
        print(f"{temp} 轉換攝氏溫度是: {(float(temp[:-1]) - 32) / 1.8}")

    case _:
        print("格式錯誤!")
