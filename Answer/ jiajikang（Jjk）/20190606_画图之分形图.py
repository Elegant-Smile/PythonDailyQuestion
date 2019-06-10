"""
 author:jjk
 datetime:2019/6/7
 coding:utf-8
 project name:Pycharm_workstation
 Program function:分形树（Fractal tree）

 1、树干初始长度为50
 2、每次绘制玩树枝时，画笔向右转20度
 3、绘制下一段树枝时，长度减少15.重复2-3操作直到终止
 4、终止条件：树枝长度小于5，此时为顶端树枝
 5、达到终止条件后，画笔左转40度，以当前长度减小15，绘制树枝
 6、右转20度，回到原来方向，退回上一个节点，直到操作完成。

"""
import turtle
def draw_bratch(branch_length):
    if branch_length > 5: # 树枝长度小于5，此时为顶端树枝
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print('向前：', branch_length)
        turtle.right(20)
        print('右转：', 20)
        draw_bratch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转：', 40)
        draw_bratch(branch_length - 15)
        # 返回上一节点
        turtle.right(20)
        print('右转:', 20)
        turtle.backward(branch_length)
        print('后退：', branch_length)

        if branch_length < 40:
            turtle.pencolor('green')
        else:
            turtle.pencolor('red')

def main():
    turtle.left(90) # 逆时针旋转
    turtle.penup() # 提起笔移动，不绘制图形，用于另起一个地方绘制 ，即抬起起笔移动，海龟飞行，不绘制图形
    turtle.backward(150)# 向当前画笔相反方向移动150像素长度
    turtle.pendown()# 即落下画笔，海龟在爬行

    draw_bratch(100) # 调用函数，树干初始化长度为:100
    turtle.exitonclick() # 鼠标点击，再执行退出



if __name__ == '__main__':
    main()



