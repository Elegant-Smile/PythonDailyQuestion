info_list = []
scores, subjects = 0, 0
while True:
    info = input("请输入小明成绩：（以空格分隔；回车结束录入）")
    if info == '':
        break
    else:
        info_list.append(info.split(' '))
        scores += eval(info.split(' ')[1])
        subjects += 1
info_list.sort(key=lambda x: x[1], reverse=True)
print("最高分课程是{}：{}，最低分课程是{}：{}，平均分是{:.1f}".format(info_list[0][0], info_list[0][1], info_list[-1][0], info_list[-1][1],
                                                  scores / subjects))
