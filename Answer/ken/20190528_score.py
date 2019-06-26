# -*- coding:utf-8 -*-
# Author: chengbin_luo

# j = input('请输入课程和成绩').split()
# k = {}
# sum = 0
# for i in range(0, len(j), 2):
#     k[j[i]] = eval(j[i+1])
#     sum += eval(j[i+1])
# k1 = sorted(k.items(),key=lambda k : k[1])
# print('最高课和成绩：', k1[-1])
# print('最低课和成绩：', k1[0])
# print('均值：{:.2f}'.format(sum/(len(j)/2)))

# info_list = []
# scores, subjects = 0, 0
# while True:
#     info = input("请输入小明成绩：（以空格分隔；回车结束录入）")
#     if info == '':
#         break
#     else:
#         info_list.append(info.split(' '))
#         scores += eval(info.split(' ')[1])
#         subjects += 1
# info_list.sort(key=lambda x: x[1], reverse=True)
# print("最高分课程是{}：{}，最低分课程是{}：{}，平均分是{:.1f}".format(info_list[0][0], info_list[0][1], info_list[-1][0], info_list[-1][1],
#                                                   scores / subjects))



# from math import sqrt, pow
#
#
# def cal_distance(x1, y1, x2, y2):
#     return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
#
#
# if __name__ == '__main__':
#     x1, y1, x2, y2 = map(float, input("请输入坐标数字:").split())
#     print(cal_distance(x1, y1, x2, y2))


# class Student:
#     name = '姓名'
#     course = 'none'
#     course_score = -1
#
#     def theHighestScore(self, course_score_list):
#         return max(course_score_list)
#
#     def theLowestScore(self, course_score_list):
#         return min(course_score_list)
#
#     def theAverageScore(self, course_score_list):
#         sum = 0
#         for score in course_score_list:
#             sum += score
#
#         average_score = sum / len(course_score_list)
#         return average_score
#
#
# if __name__ == '__main__':
#     student = Student()
#     student.name = '小明'
#
#     course_score_dict = {}
#
#     student.course = list(map(str, input("请先输入课程名:").strip().split()))
#     student.course_score = list(map(float, input("然后请输入课程对应考试分数:").strip().split()))
#
#     course_score_dict = dict(zip(student.course, student.course_score))
#
#     print(course_score_dict)
#     theHighestScore = student.theHighestScore(student.course_score)
#     theLowestScore = student.theLowestScore(student.course_score)
#
#     print('最高分课程是%s %d' % (max(course_score_dict, key=course_score_dict.get), theHighestScore))
#     print('最低分课程是%s %d' % (min(course_score_dict, key=course_score_dict.get), theLowestScore))
#     print('平均分是', student.theAverageScore(student.course_score))

# c_s_list = {}  # class & score
# sum = 0			# 均值
# while True:
#     a = input('input your class && score:')
#
#     if a == 'esc':
#         for key, value in c_s_list.items():
#             print(key,value)
#             sum += int(value)  # 均值
#
#         max_min = sorted(c_s_list.items(), key=lambda s: s[1])
#
#         print('\n得分最高的课程名称:{}考试分数:{}'.format(max_min[-1][0], max_min[-1][1]))
#         print('得分最低的课程名称:{}考试分数:{}'.format(max_min[0][0], max_min[0][1]))
#         print('均值:%.1f' % (sum/len(c_s_list)))
#         break
#     else:
#         b = a.split()
#         c_s_list[b[0]] = b[1]

