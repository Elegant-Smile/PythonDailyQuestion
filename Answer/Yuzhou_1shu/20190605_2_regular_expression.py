'''
请实现一个函数用来匹配包括.和'*'的正则表达式。
模式中的字符 '.' 表示任意一个字符，而 '*' 表示它前面的字符可以出现任意次(包含0次)。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
'''


def match(s, pattern):
    if s == pattern:
        return True
    if not pattern:
        return False
    if len(pattern) > 1 and pattern[1] == '*':
        if (s and s[0] == pattern[0]) or (s and pattern[0] == '.'):
            return match(s, pattern[2:]) \
                   or match(s[1:], pattern) \
                   or match(s[1:], pattern[2:])
        else:
            return match(s, pattern[2:])
    elif s and (s[0] == pattern[0] or pattern[0] == '.'):
        return match(s[1:], pattern[1:])
    return False


print(match('aaa', 'a.a'))
print(match('aaa', 'ab*ac*a'))
print(match('aaa', 'aa.a'))
print(match('aaa', 'ab*a'))
