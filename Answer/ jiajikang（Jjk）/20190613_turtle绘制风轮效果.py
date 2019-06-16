"""
 author:jjk
 datetime:2019/3/29
 coding:utf-8
 project name:Pycharm_workstation
 coding:utf-8
 Program function:

使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
            turtle.goto(x,y)函数，能够将turtle画笔移动到坐标(x,y)

"""


import turtle as t
t.setup(600,400) # 设置窗体大小及位置
t.pensize(1) # 都可以用来设置画笔尺寸 也就是线的粗细
for i in range(4):
    t.fd(150) # forward(150)前进
    t.right(90)
    t.circle(-150,45) # 边长150像素，内角：45度
    t.goto(0,0) # turtle.goto(x,y)函数，能够将turtle画笔移动到坐标(x,y)‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬
    t.left(45)
t.done()# 绘制完成，图片不关闭



