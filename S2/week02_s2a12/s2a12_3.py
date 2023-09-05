import turtle as t

print("s2a12 李景霖")

def forward(distance: float):
    t.pensize(5)
    t.pencolor("#80409c")
    t.forward(distance)

def right(angle: float):
    t.right(angle)

for i in range(4):
    forward(100)
    right(90)
t.done()
