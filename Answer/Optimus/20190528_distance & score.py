# 基础题：从键盘输入4个数字，各数字采用空格分隔，对应为变量x0,y0,x1,y1。计算(x0，y0)和(x1,y1)两点之间的距离，
# 输出结果保留1位小数。比如，键盘输入：0 1 3 5，屏幕输出：5.0
i=input('输入坐标').split()
x1,x2,x3,x4=eval(i[0]),eval(i[1]),eval(i[2]),eval(i[3])
dis=pow((pow(x3-x1,2)+pow(x4-x2,2)),0.5)
print(dis)


# 提高题：键盘输入小明学习的课程以及考试分数信息，信息之间采用空格分隔，每个课程一行，空格回车结束录入，示例格式如下：
# 数学 90
# 语文 95
# 英语 86
# 物理 84
# 生物 87
# 输出得分最高和最低的课程名称、考试分数，以及所有课程的平均分(保留2位小数)
# 格式如下：
# 最高分课程是语文 95，最低分课程是物理 84，平均分是88.4
j=input('请输入课程和成绩').split()
k={}
sum=0
for i in range(0,len(j),2):
    k[j[i]]=eval(j[i+1])
    sum+=eval(j[i+1])
k1=sorted(k.items(),key=lambda k:k[1])
print('最高课和成绩：',k1[-1])
print('最低课和成绩：',k1[0])
print('均值：{:.2f}'.format(sum/(len(j)/2)))


