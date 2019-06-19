'''
基础题：
列表sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']。
编写代码执行以下任务：
a. 输出所有 sh 开头的单词
b. 输出所有长度超过 4 个字符的词
'''
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print([s for s in sent if s.startswith('sh') and len(s)>4])
