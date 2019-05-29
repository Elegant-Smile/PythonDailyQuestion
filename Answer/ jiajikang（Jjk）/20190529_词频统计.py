"""
 author:jjk
 datetime:2019/5/29
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 词频统计
 思路： 
      1、以一行作为一个词
	  2、先分词
	  3、存储的新的文本文件
	  4、统计新的文本文件中的词频
 执行方式：
           后台执行：python 20190528_词频统计.py result.txt
"""


import jieba
import jieba.posseg as pseg
import re
from sys import argv # 后台参数


def fenci():
    fileneedCut = 'test.txt' 
    filename = 'result.txt'
    fn = open(fileneedCut, "r", encoding='utf-8')
    f=open(filename,"w+",encoding='utf-8')
    for line in fn.readlines():
        # words=pseg.cut(line)
        line = line.strip('\n')
        words = jieba.cut(line)
        for word in words:
            f.write(word)
            f.write('\n')
            #print(word)
    fn.close()
    #return word


# 读文件到缓冲区
def process_file(file):     # 读文件到缓冲区
    try:     # 打开文件
        f = open(file, 'r',encoding="utf-8")
    except IOError as s:
        print(s)
        return None
    try:     # 读文件到缓冲区
        bvffer = f.read()
    except:
        print("Read File Error!")
        return None
    f.close()
    return bvffer

# 处理缓冲区
def process_buffer(bvffer):
    if bvffer:
        word_freq = {}
        # 下面添加处理缓冲区 bvffer代码，统计每个单词的频率，存放在字典word_freq
        # bvffer = bvffer.lower()
        #for ch in '“‘!;,.?”':
        #    bvffer = bvffer.replace(ch, " ")  #将所有字母转换成小写，便于统计
        words = bvffer.strip().split()         #strip消除空白符，split以空格作为单词分界
        for word in words:
            word_freq[word] = word_freq.get(word, 0)+1  #读取到的单词存放到字典
        return word_freq


def output_result(word_freq):
    if word_freq:
        sorted_word_freq = sorted(word_freq.items(), key=lambda v: v[1], reverse=True)
        #for item in sorted_word_freq[:10]:  # 输出 Top 10 的单词
        for item in sorted_word_freq: 
            print(item[0], item[1])


if __name__ == "__main__":
    fenci()
    canshu = len(argv)
    if canshu != 2:
        print("后台输入参数不合法")
        exit(1)
    else:
        file = argv[1]  # 第二个参数：文本文件名字
        bvffer = process_file(file)  # 调用读取文件函数
        word_freq = process_buffer(bvffer)  # 调用处理缓冲区函数
        output_result(word_freq)  # 调用输出结果函数



