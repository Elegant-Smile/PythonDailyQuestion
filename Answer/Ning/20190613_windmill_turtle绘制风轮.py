"""
使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
提示：turtle.goto(x,y)函数，能够将turtle画笔移动到坐标(x,y)
"""

import turtle

turtle.setup(600, 400)
turtle.pensize(5)

for i in range(4):
    turtle.forward(150)
    turtle.right(90)
    turtle.circle(-150, 45)
    turtle.goto(0, 0)
    turtle.left(45)

turtle.done()
