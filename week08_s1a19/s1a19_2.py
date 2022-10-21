print("s1a19 李景霖\n")
# Python 列表(List)認識

alist = [10, 20, 30, "bob", "alice", [1,2,3]]
print("列表是: ",alist)
print("列表的長度: ",len(alist)) # 列表的長度
print("取出最後一項",alist[-1]) # 取出最後一項
print("取出最後一項的列表最後一項: ",alist[-1][-1])
# 因為最後一項是列表，列表還可以繼續取下標
print("取出最後一項的列表最後一項: ",[1,2,3][-1])
# [1,2,3]是列表，[-1]表示列表最後一項
print("取出倒數第2項是字符串，再取出字符下標為的字符: ",alist[-2][2])
# 取出倒數第2項是字符串，再取出字符下標為的字符
print("取出列表4-5項: ",alist[3:5])
# ["bob", "alice"]
print("10是否在列表中: ",10 in alist) # True
print("o是否在列表中: ","o" in alist)
print("100不在列表中: ",100 not in alist) # True