# 问题：输入年月份，判断该天使该年的第几天

# 解法一
# #输入年月日，输出第几天
# # def Leap(year):#判断闰年的函数
# #     if year%400==0 or (year%100!=0 and year%4==0):
# #         days[1]=29
# #         return days[1]
# #     else:
# #         return year
# #
# # days=[31,28,31,30,31,30,31,31,30,31,30,31]
# # year,month,day= map(int,input().split())
# # Leap(year)
# #
# # numDay=0
# # for i in range(0,month-1):
# #     numDay+=days[i]
# #
# # print("{}年 {}月 {}日 是{}年的第{}天".format(year,month,day,year,numDay+day))

# 解法二
import datetime
def getDay_Num():
    print("请输入年月份，中间空格间隔开")
    year, month, day = map (int, input().split())
    date1=datetime.date(year=int(year),month=int(month),day=int(day))
    date2=datetime.date(year=int(year),month=1,day=1)
    return ((date1-date2).days+1)

if __name__ == '__main__':
    print(getDay_Num())
