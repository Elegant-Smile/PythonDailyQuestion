"""
 author:jjk
 datetime:2019/5/2
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 
"""
# !/usr/bin/env python
# coding:UTF-8



'''
矩阵转置
将[[1,2,3],[4,5,6],[7,8,9]]
转换为[[1,4,7],[2,5,8],[3,6,9]]
'''

#方法一：默认列表值均初始为0，防止换为位置时，坐标越界
list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        list2[j][i] = list1[i][j]
print(list2)

print("*"*50,"1")
#方法二：互换位置，空列表插入值
list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = [[],[],[]]
for i in range(3):
    for j in range(3):
        list2[j].insert(i,list1[i][j])
print(list2)
print("*"*50,"2")


#方法三：行列互换
list1 = [[1,2,3],[4,5,6],[7,8,9]]
print([[list1[i][j] for i in range(3)] for j in range(3)])
print("*"*50,"3")

# 方法四:取每行的第i列，即列转换为行
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([[row[i] for row in list1] for i in range(3)])