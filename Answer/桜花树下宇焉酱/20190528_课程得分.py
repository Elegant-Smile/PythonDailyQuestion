'''
提高题：键盘输入小明学习的课程以及考试分数信息，信息之间采用空格分隔，每个课程一行，空格回车结束录入，示例格式如下：
数学 90
语文 95
英语 86
物理 84
生物 87
输出得分最高和最低的课程名称、考试分数，以及所有课程的平均分(保留2位小数)
格式如下：
最高分课程是语文 95，最低分课程是物理 84，平均分是88.4
'''
c_s_list = {}	# class & score
sum = 0			# 均值
while True:
	a = input('input your class && score:')

	if a == 'esc':
		for key,value in c_s_list.items():
			print(key,value)
			sum += int(value)	# 均值

		max_min = sorted(c_s_list.items(),key=lambda s:s[1])

		print('\n得分最高的课程名称:{}考试分数:{}'.format(max_min[-1][0],max_min[-1][1]))
		print('得分最低的课程名称:{}考试分数:{}'.format(max_min[0][0],max_min[0][1]))
		print('均值:%.1f'%(sum/len(c_s_list)))
		break
	else:
		b = a.split()
		c_s_list[b[0]] = b[1]
