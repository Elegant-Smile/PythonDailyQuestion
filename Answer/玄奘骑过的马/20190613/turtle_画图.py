# _*_coding:utf-8 _*_
# Author:Oldyuan
# ChangeTime: 2019/6/13 11:03
# FileName: turtle_画图.py


import turtle as t

t.setup(600,400)
t.pensize(5)
for i in range(5):
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0, 0)
    t.left(45)
t.done()







