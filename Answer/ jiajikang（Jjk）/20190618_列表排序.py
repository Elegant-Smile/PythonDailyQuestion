"""
 author:jjk
 datetime:2019/3/29
 coding:utf-8
 project name:Pycharm_workstation
 coding:utf-8
 Program function:
   20190606
   基础题：
      列表 languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'), (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]，
      请进行排序，实现效果：[(4, 'Erlang'), (5, 'Kotlin'), (6, 'Python'), (3, 'Swift'), (2, 'Ruby'), (1, 'Go')]
"""

"""

"""

def lens(element):
    return len(element[1])

languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'), (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]
# 参数key用来指定一个函数，此函数在每次元素比较时被调用，
# 此函数代表排序的规则，也就是你按照什么规则对你的序列进行排序；一般用lambda函数指定。
languages.sort(key=lens,reverse=True) # 升序
print(languages)