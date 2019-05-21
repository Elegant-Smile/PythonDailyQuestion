n = 0
for _ in range(10):
	age=input("请输入你的年龄：")
	gender=input("请输入你的性别：(男性输入m 女性输入f)")
	if 10<=eval(age)<=12 and gender=="f":
		print("恭喜你被录取！")
		n+=1
	else:
		print("抱歉，你没有被录取。")
print("共有{}人被录取!".format(n))
