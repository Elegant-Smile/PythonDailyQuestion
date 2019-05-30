# 用原生函数实现
def convert_space_to_percent_sign(s):
    s = s.replace(' ', '%20')
    return s


print(convert_space_to_percent_sign('We Are Happy'))
