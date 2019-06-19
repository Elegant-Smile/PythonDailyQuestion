"""
 author:jjk
 datetime:2019/3/29
 coding:utf-8
 project name:Pycharm_workstation
 coding:utf-8
 Program function:
   20190606
   基础题：
      用户输入一个字符串和 一个子串，程序必须打印出给定子串在目标字符串中出现的次数 。字符串遍历将从左到右进行，而不是从右到左 。
      例如给定'ABCDCDC’和’CDC'，程序输出“ 2 ”。
"""

"""

"""

# def lens(element):
#     return len(element[1])
#
# languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'), (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]
# # 参数key用来指定一个函数，此函数在每次元素比较时被调用，
# # 此函数代表排序的规则，也就是你按照什么规则对你的序列进行排序；一般用lambda函数指定。
# languages.sort(key=lens,reverse=True) # 升序
# print(languages)


def calcu_sub_str_num(mom_str,sun_str):
    print('打印母字符串：', mom_str)  # 打印出母字符串
    print('打印子字符串：', sun_str)  # 打印出子字符串
    print('打印母字符串长度：', len(mom_str))  # 打印出母字符串长度
    print('打印子字符串长度：', len(sun_str))  # 打印出子字符串长度
    count = 0  # 定义计数器初始值
    # 使用循环遍历字符串
    # 第一次循环，通过切片获取下标从0开始与子字符串长度一致的字符串，并与字符串比较，如果等于子字符串count+1
    # 第二次循环，通过切片获取下标从1开始与子字符串长度一致的字符串，并与字符串比较，如果等于子字符串则count+1，以此类推直到遍历完成
    for i in range(len(mom_str) - 1):  # 因为i的下标从0开始，所以len（mom_str）-1
        if mom_str[i:i + len(sun_str)] == sun_str:
            count += 1
    return count

mom_str = input('please input mother string:') #使用input获取输入母字符串
sun_str = input('please input child string:') #使用input获取输入子字符串
print('子字符串在母字符串中出现的次数：%d'%calcu_sub_str_num(mom_str,sun_str))#%d为数字占位符
