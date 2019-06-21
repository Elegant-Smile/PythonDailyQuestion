# 基础题： 
# 列表sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
# 编写代码实现以下功能：
# a.输出所有sh开头的单词
# b.输出所有长度超过4个字符的词
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
for i in sent:
    if i.startswith('sh'):
        print('a:',i)
    if len(i)>4:
        print('b:',i)

# 提高题：
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
# 那么对应的输出是第一个重复的数字2。
# n=eval(input('请输入N'))
# a=list(n)
# k=len(n)
# for i in range(k):
#     j=i+1
#     for j in range(k-i):
#         if a[i]==a[j]:
#             l=a[j]
#             print(l)
# 不会


