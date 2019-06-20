'''
提高题：
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy
则经过替换之后的字符串为We%20Are%20Happy。
'''
# 1.
print('We Are Happy'.replace(' ','%20'))

# 2.
import re
print(re.sub(r' ','%20','We Are Happy'))