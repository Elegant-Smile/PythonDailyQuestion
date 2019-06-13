"""
  一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
  编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
  然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Abner Han 
# time:2019/6/13

time = 0
person = 0
while time < 3:
    age = int(input("Please age:"))
    gender = input("Please gender:(f or m)")
    time += 1
    if age >= 10 and age <=12 and gender == "f":
        person += 1
    else:
        person = 0

print("Number is {0}".format(person))
