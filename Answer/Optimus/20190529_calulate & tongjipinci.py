# 请解释Python中 copy, deepcopy 的区别及原因。
# 复制就是deepcopy，即将被复制对象完全再复制一遍作为独立的新个体单独存在。
# 所以改变原有被复制对象不会对已经复制出来的新对象产生影响。
# —–而copy并不会产生一个独立的对象单独存在，他只是将原有的数据块打上一个新标签，
# 所以当其中一个标签被改变的时候，数据块就会发生变化，另一个标签也会随之改变。
import copy
origin = [1, 2, [3, 4]]
#origin 里边有三个元素：1， 2，[3, 4]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
print(cop1 == cop2)
# True
print(cop1 is cop2)
# False
#cop1 和 cop2 看上去相同，但已不再是同一个object
origin[2][0] = "hey!"
print(origin)
# [1, 2, ['hey!', 4]] 
print(cop1)
# [1, 2, ['hey!', 4]]
print(cop2)
# [1, 2, [3, 4]]
#把origin内的子list [3, 4] 改掉了一个元素，观察 cop1 和 cop2


# 基础题：809*x=800*x+9*x+1 其中 x 代表的两位数, 8*x 的结果为两位数，
# 9*x 的结果为 3 位数。求 x ，及计算 809*x 的结果。
for x in range(10,100):
    if (10<=8*x<+100) and (100<=9*x<=1000):
        print(809*x)

# 提高题：
# 对文件"命运.txt"进行字符频次统计，并将所有字符按照频次高低排序，将排序后的字符及其频次输出到文件"命运-频次排序.txt"
# 字符包括中文、英文、标点等，但不包括空格和回车
# 输出格式要求：
# (1)字符与频次之间采用冒号 ：分隔
# (2)一个字符一行，比如
# 理:224
# 斯:120
# 卫:100
txt=open('F:\\mingyun.txt','r',encoding='utf-8').read()
txt = txt.replace('\n','')
count={}
for word in txt:
    count[word] = count.get(word, 0) + 1
counts=sorted(count.items(),key=lambda x:x[1],reverse=True)
for word,cnt in counts:
    print(f'{word} : {cnt}')
    file = open('F:\\mingyuncounts.txt', 'a+', encoding='utf-8')
    file.write(f'{word} : {cnt}' + '\n')
