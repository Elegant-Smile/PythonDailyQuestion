"""
 author:jjk
 datetime:2019/6/6
 coding:utf-8
 project name:Pycharm_workstation
 Program function:  用Python Turtle 模块，画出分形树（Fractal tree），科赫雪花曲线（Koch snowflake）和龙形曲线（Dragon curve）。

"""
"""
 科赫雪花曲线（Koch snowflake）

    瑞典人科赫于1904年提出了著名的“雪花”曲线，这种曲线的作法是，从一个正三角形开始，把每条边分成三等份，然后以各边的中间长度为底边。分别向外作正三角形，再把“底边”线段抹掉，这样就得到一个六角形，它共有12条边。再把每条边三等份，以各中间部分的长度为底边，向外作正三角形后，抹掉底边线段。反复进行这一过程，就会得到一个“雪花”样子的曲线。这曲线叫做科赫曲线或雪花曲线。
反复进行这一作图过程，得到的曲线越来越精细。
    科赫曲线有着极不寻常的特性，不但它的周长为无限大，而且曲线上任两点之间的距离也是无限大。该曲线长度无限，却包围着有限的面积。
    很神奇的一个曲线，他说明了一个悖论：“无限长度包围着有限面积。”

思路：
   设想一个边长为1的等边三角形，取每边中间的三分之一，接上去一个形状完全相似的但边长为其三分之一的三角形，结果是一个六角形。
   现在取六角形的每个边做同样的变换，即在中间三分之一接上更小的三角形，以此重复，直至无穷。外界的变得原来越细微曲折，形状接近理想化的雪花。
"""

import turtle

# 抽象步骤，如果是0阶，只需前行；如果是一阶，需要前行，转向，前行，转向，前行，转向，前行，
# 共有的是前行，阶数需要控制转向的次数，所以边界是0阶，只需前行
#科克曲线

"""
# 科赫曲线

turtle.pensize(4)
turtle.pencolor('green')
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
def kehe_line(n=1,len=120): # 通过修改n来实现科赫曲线的节数
    if n==0:
        turtle.fd(len)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            kehe_line(n-1,len/3)

kehe_line() # 调用函数

turtle.hideturtle() # 隐藏画笔的turtle形状，说白了也就是箭头
turtle.done()

"""


def kehe(len,n):
    if n==0:
        turtle.fd(len) # 前进
    else:
        for i in [0,60,-120,60]:
            turtle.left(i) # 逆时针移动
            kehe(len/3,n-1)

lenth = 500
level = 3 # 阶数
du = 120

def main():
    turtle.penup() # 提起笔移动，不绘制图形，用于另起一个地方绘制
    turtle.goto(-100,100) # 将画笔移动到坐标为x,y的位置
    turtle.pensize(2)# 设置画笔的宽度
    turtle.color('green') # 设置图片的颜色
    turtle.pendown() # 移动时绘制图形，缺省时也为绘制


    kehe(lenth,level)
    turtle.right(du) # 顺时针移动
    kehe(lenth,level)
    turtle.right(du)
    kehe(lenth,level)
    turtle.right(du)


    turtle.hideturtle() # 隐藏画笔的turtle形状，说白了也就是箭头
    turtle.done() # 用来停止画笔绘制，但绘图窗体不关闭

main() # 调用函数

















