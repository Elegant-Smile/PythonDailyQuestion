# -*- coding:utf-8 -*-
# Author: chengbin_luo


# import turtle
# from turtle import *
#
#
# def koch(size, n):  # n 代表雪花的级数，n越大，就越像雪花
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#             turtle.left(angle)
#             koch(size / 3, n - 1)
#
#
# def main():
#     turtle.setup(600, 600)
#     turtle.pen(speed=0, pencolor='blue')
#     turtle.penup()
#     turtle.goto(-200, 100)
#     turtle.pendown()
#     turtle.pensize(1)
#     level = 5  # 这里修改雪花的级数，级数越大，雪花越像
#     koch(400, level)
#     turtle.right(120)
#     koch(400, level)
#     turtle.right(120)
#     koch(400, level)
#     turtle.hideturtle()
#     done()
#
#
# if __name__ == '__main__':
#     main()


# import turtle as t
# t.setup(600, 400)  # 画布的大小 width=600 ,height=400
# t.pensize(5)  # 画笔的粗细
# # t.pencolor("red")
# t.speed(0)
# t.fillcolor("yellow")
# t.begin_fill()
# for i in range(4):
#     t.fd(150)  # 前进150像素
#     t.right(90)  # 画笔右转90度(顺时针)
#     t.circle(-150, 45)  # 圆的半径为 -150，意味着 顺时针绘制圆，夹角为 45度
#     t.goto(0, 0)  # 将画笔移动到坐标为(0,0)的位置
#     t.left(45)    # 画笔左转90度(逆时针)
#
# t.end_fill()
# t.done()


# import turtle as t
# import math as m
#
# t.pensize(4)  # 设置画笔的大小
# t.colormode(255)  # 设置GBK颜色范围为0-255
# t.color((0, 0, 255), "blue")  # 设置画笔颜色和填充颜色(pink)
# t.setup(800, 600)  # 设置主窗口的大小为840*500
# t.speed(10)  # 设置画笔速度为10
# # 头部
# t.hideturtle()
# t.pu()  # 提笔
# t.goto(-50, 0)  # 画笔前往坐标(0,0)
# t.seth(150)
# t.pd()  # 下笔
# t.begin_fill()
# t.color(0, 0, 255)
# for i in range(300):
#     t.rt(1)
#     t.forward(2 * m.pi * 100 / 360)
# t.seth(0)
# t.backward(10)
#
# t.seth(30)
# for i in range(300):
#     t.lt(1)
#     t.forward(2 * m.pi * 80 / 360)
# t.seth(0)
# t.backward(10)
# t.end_fill()
# # 眼睛
# t.pu()
# t.begin_fill()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(-15, 40 * m.sqrt(3) + 60)
# t.pd()
# t.circle(15)
# t.color(255, 255, 255)
# t.end_fill()
#
# t.pu()
# t.begin_fill()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(-15, 40 * m.sqrt(3) + 60)
# t.pd()
# t.circle(5)
# t.color(0, 0, 0)
# t.end_fill()
#
# t.pu()
# t.begin_fill()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(15, 40 * m.sqrt(3) + 60)
# t.pd()
# t.circle(15)
# t.color(255, 255, 255)
# t.end_fill()
#
# t.pu()
# t.begin_fill()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(15, 40 * m.sqrt(3) + 60)
# t.pd()
# t.circle(5)
# t.color(0, 0, 0)
# t.end_fill()
#
# # 鼻子
# t.pu()
# t.pensize(3)
# t.pencolor(255, 0, 0)
# t.goto(0, 40 * m.sqrt(3) + 40)
# t.pd()
# t.begin_fill()
# t.color(255, 0, 0)
# t.circle(10)
# t.end_fill()
# # 嘴巴
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(0, 40 * m.sqrt(3) + 40)
# t.pd()
# t.seth(-90)
# t.forward(50)
# t.pu()
# t.goto(-50, 90 - 10 * m.sqrt(3))
# t.seth(-30)
# t.pd()
# for i in range(60):
#     t.lt(1)
#     t.forward(2 * m.pi * 100 / 360)
#
# # 胡须
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(-30, 40 * m.sqrt(3) + 25)
# t.seth(0)
# t.pd()
# t.backward(40)
#
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(-30, 40 * m.sqrt(3) + 15)
# t.pd()
# t.seth(30)
# t.backward(40)
#
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(-30, 40 * m.sqrt(3) + 35)
# t.pd()
# t.seth(-30)
# t.backward(40)
#
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(30, 40 * m.sqrt(3) + 25)
# t.seth(0)
# t.pd()
# t.forward(40)
#
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(30, 40 * m.sqrt(3) + 35)
# t.pd()
# t.seth(30)
# t.forward(40)
#
# t.pu()
# t.pensize(3)
# t.pencolor(0, 0, 0)
# t.goto(30, 40 * m.sqrt(3) + 15)
# t.pd()
# t.seth(-30)
# t.forward(40)
#
# t.done()



import turtle as t
t.setup(600, 400)  # 画布的大小 width=600 ,height=400
t.pensize(5)  # 画笔的粗细
# t.pencolor("red")
t.speed(1)  # 画笔的移动速度
t.fillcolor("yellow")  # 填充颜色
t.begin_fill()  # 开始填充
for i in range(4):
    t.fd(150)  # 前进150像素
    t.right(90)  # 画笔右转90度(顺时针)
    t.circle(-150, 45)  # 圆的半径为 -150，意味着 顺时针绘制圆，夹角为 45度
    t.goto(0, 0)  # 将画笔移动到坐标为(0,0)的位置
    t.left(45)    # 画笔左转90度(逆时针)

t.end_fill()  # 结束填充
t.done()

