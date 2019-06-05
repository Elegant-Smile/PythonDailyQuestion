"""
 author:jjk
 datetime:2018/11/5
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 20190603
    基础题：
        列表 sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
        编写代码实现以下功能：
        a. 输出所有 sh 开头的单词
        b. 输出所有长度超过 4 个字符的词

"""

sent = ['she','sells','sea','shells','by','the','sea','shore']

for x in sent:
    if x.startswith('sh'):
        print('a:',x)
    elif len(x)>4:
        print('b:',x)
    else:
        pass


