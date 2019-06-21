# 用Python Turtle 模块，画出分形树（Fractal tree），
# 科赫雪花曲线（Koch snowflake）和龙形曲线（Dragon curve）。



import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle
main()




# 请实现一个函数用来判断字符串是否表示数值(包括整数和小数)。例如，字符
# 串"+100","5e2",-123","3.141 6"和"-1E-16"都表示数值。但
# 是"12e","1a3.14","1 .2.3","+-5"和"12e+4.3"都不是。



def is_Number(s):
    try:
        num = float(s)
        return True
    except:
        return False


if __name__ == '__main__':
    s = input("请输入一个字符串：")
    print(is_Number(s))