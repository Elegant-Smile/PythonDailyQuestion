# _*_coding:utf-8 _*_
# Author:Oldyuan
# ChangeTime: 2019/6/18 8:55
# FileName: dogfile.py

class Dog ():
    def __init__(self, name ,age):
        self.Name = name
        self.Age = age

    def sit(self):
        print('set')
    def rill_over(self):
        print('rill_over')


my_dog = Dog('1',6)

print(my_dog.Name.title())
print(my_dog.Age)
print(my_dog.rill_over())
