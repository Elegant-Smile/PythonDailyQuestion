"""
 author:jjk
 datetime:2019/3/29
 coding:utf-8
 project name:Pycharm_workstation
 coding:utf-8
 Program function:
       列表中有一个数字出现的次数超过列表长度的一半，请找出这个数字。
       例如，输入一个长度为 9 的列表[1, 2, 3, 2, 2, 2, 5, 4, 2]。数字2出现了5次，超过列表长度的一半，因此输出2。
       如果不存在则输出0。
"""

# 方法一：
import collections
def Number(numbers):
    tmp = collections.Counter(numbers) # 统计列表元素出现的次数 返回是一个字典：键值
    x = len(numbers)/2
    for k,v in tmp.items(): # 列表返回可遍历的(键, 值) 元组数组。
        if v>x:
            return k
    return  0

# if __name__ == '__main__':
#     le = [1, 2, 3, 2, 2, 2, 5, 4, 2]
#     print(Number(le))


#方法二： 时间复杂度为O(NlogN)
"""
  思路：数组排序后，如果符合条件的数存在，
  则一定是数组中间那个数。（比如：1，2，2，2，3；或2，2，2，3，4；或2，3，4，4，4等等），
  这种方法虽然容易理解，但由于涉及到快排sort，其时间复杂度为O(NlogN)并非最优。

"""

def morethathalfNum_Solution(numbers):
    len1 = len(numbers) # 列表的长度
    if len1 == 0:
        return 0
    numbers.sort() # 排序
    middle = numbers[len1//2] # 排序后的中位数 整除//

    # 判断出现次数是否大于数组长度的一半
    counts = 0
    for j in range(len1): # 遍历数组的长度
        if numbers[j] == middle:
            counts += 1 # 出现重复的个数
    if counts>len1//2: #整除
        return middle
    else:
        return 0


if __name__ == '__main__':
    try:
        while True:
            arr = [int(i) for i in input().split()] # 循环输入int型数值
            print(morethathalfNum_Solution(arr))
    except:
        pass


