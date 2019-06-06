import turtle
from turtle import *
def koch(size, n):#n 代表雪花的级数，n越大，就越像雪花
     if n == 0:
         turtle.fd(size)
     else:
         for angle in [0, 60, -120, 60]:
             turtle.left(angle)
             koch(size / 3, n - 1)
def main():
    turtle.setup(600,600)
    turtle.pen(speed = 0, pencolor = 'blue')
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(1)
    level = 5 #这里修改雪花的级数，级数越大，雪花越像
    koch(400,level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    done()

if __name__ == '__main__':
    main()
