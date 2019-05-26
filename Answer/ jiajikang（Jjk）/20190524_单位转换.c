/*
 * @Author: jjk
 * @Date: 2019-05-24 09:14:30
 * @Last Modified by: jjk
 * @Last Modified time: 2019-05-24 09:55:54
 * coding：gbk
 * 程序功能：基础题1：设计一个重量转换器，输入以“g”为单位的数字后返回换算成“kg”的结果
 *          1000k = 1kg
 *
 */

#include <stdio.h>
// #include <string.h>
// #include <stdlib.h>
#define DFWW 0.001
#define DFWW2 1000

void trans(float sec)
{
    float g, kg;
    if (sec >= DFWW2)
    {
        kg = sec / DFWW2; //计算时 3600进制  计算千克，1000进制
        printf("以\"kg\"为单位:%.3f", kg);
    }
    else
    {
        kg = sec * DFWW;
        printf("以\"kg\"为单位:%.3f", kg);
    }
}

int main()
{
    float sec;
    printf("请输入以\"g\"为单位数值：\n");
    scanf("%f", &sec);
    trans(sec);
    return 0;
}