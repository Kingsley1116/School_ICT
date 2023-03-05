print("s1a19 李景霖\n")

name = "root"
passwd = "3322"

def login(userName, password):
    if userName == name and password == passwd:
        exit("登錄成功!")
    else:
        print("登錄失敗!")

if __name__ == "__main__":
    for i in range(3):
        login(
            userName = input("用戶名: "),
            password = input("密碼: ")
        )
    print("失敗超過3次, 請稍後再試!")