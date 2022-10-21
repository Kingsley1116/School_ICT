print("s1a19 李景霖\n")
# Python 字串(String)認識

# 串接字串
str1 = "01234"
str2 = "56789"
str3 = str1 + str2
print(str3)

# 複製字串
str1 = "Oh~"
str2 = "蔡"
str3 = "高"
str4 = str1 * 5 + str2 + str3 * 2
print(str4)
str5 = str3.replace("高","老師")
str4 = str1 * 10 + str2 + str5
print(str4)

# 取出字串元素
str1 = "聖公會(澳門)蔡高中學"
print(str1[0])
print(str1[1])
print(str1[-1])
print(str1[-2])

# 切割字串
str1 = "聖公會(澳門)蔡高中學"
print(f"str1 = {str1} s[:] = {str1[:]}")
print(f"str1 = {str1} s[5:] = {str1[5:]}")
print(f"str1 = {str1} s[-2:] = {str1[-2:]}")
print(f"str1 = {str1} s[:5] = {str1[:5]}")
print(f"str1 = {str1} s[:-2] = {str1[:-2]}")
print(f"str1 = {str1} s[::-1] = {str1[::-1]}")