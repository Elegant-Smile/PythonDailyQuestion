"""
 author:jjk
 datetime:2019/3/29
 coding:utf-8
 project name:Pycharm_workstation
 coding:utf-8
 Program function:
       20190612
       提高题：
          输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
	      使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

def reOrderArray(array):
    odd, even = [], []
    for i in array:
        odd.append(i) if i % 2 == 1 else even.append(i)
    return odd + even

# 方式二
def reOrderArray2(array):
    i = 0
    odd = []
    even = []
    while len(array)>i:
        if array[i] %2 == 1: # 奇数
            odd.append(array[i])
        else:
            even.append(array[i])
        i += 1
    return odd + even

# 方式三：转型方式一
def reOrderArray3(array):
    odd,enven =[],[] # 创建两个列表
    for i in array:
        if i %2 ==1:# 奇数
            odd.append(i)
        else:
            enven.append(i)
    return odd+enven



if __name__ == '__main__':
    length = [1,3,4,6,7,9,10,11,12,14]
    print(reOrderArray3(length))