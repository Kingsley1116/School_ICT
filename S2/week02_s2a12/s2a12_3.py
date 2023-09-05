# 引入 turtle(海龜) 模組並創建別稱 t
import turtle as t

print("s2a12 李景霖")

# 自定義函數
def forward(distance: float):
    # 向前 distance 距離
    t.pensize(5)            # 設置畫筆大小為5
    t.pencolor("#80409c")   # 紫色 (上網查hex color picker以更換為其他顏色)
    t.forward(distance)

def right(angle: float):
    # 轉右 angle 度
    t.right(angle)

# 調用函數
# 重覆四次畫一個正方形
for i in range(4):
    forward(100)
    right(90)

# 程式完結並保持窗口開啟
t.done()