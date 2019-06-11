#字符输入星期
str=input("请输入一个字符:\n")

if str is 'm' or str is 'M':
    print("Monday")
elif str is 'T' or str is 't':
    str1=input("请继续输入第二个字符:\n")
    if str1 is 'u' or str1 is 'U':
        print("Tuesday")
    elif str1 is 'h' or str1 is 'H':
        print("Thursday")
elif str is 'W' or str is 'w':
    print("Wednesday")
elif str is 'f' or str is 'F':
    print("Friday")
elif str is 's' or str is 'S':
    str2=input("请继续输入第二个字符")
    if str2 is 'A' or str2 is 'a':
        print("Saturday")
    elif str2 is 'u' or str2 is 'U':
        print("Sunday")
