/*
 * @Author: jjk 
 * @Date: 2019-05-20 16:26:06 
 * @Last Modified by:   jjk 
 * @Last Modified time: 2019-05-20 16:26:06 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int num2 = 0;
int number(int num)
{
    int i = 0;
    do
    {
        num = num / 10;
        i++;
    } while (num != 0);
    //printf("一共%d位\n", i);
    num2 = i;
}

void fun(int num)
{
    int x = 0, flag = 0, number = 1;

    if (num <= 0)
    {
        //num = -num;
        //printf("-");
        printf("I'am so sorry, %d is not a positive integer", num);
        exit(-1);
    }
    while (num > 10)
    {
        x = num % 10; // 求余
        num /= 10;    // 求整
        number++;

        if (x == 0 && (!flag)) //
            continue;
        else
            printf("%d", x);
        flag = x; //标志位
    }
    printf("%d\n", num);
    //printf("\nnumber=%d", number);
}

int main()
{
    int num;
    printf("请输入正整数(小于5位):");
    scanf("%d", &num);
    printf("%d\n", num);
    number(num); // 调用位数函数
    if (num2 >= 5)
    {
        printf("\nPlease enter a positive integer less than five digits\n");
        exit(0);
    }
    else
    {
        fun(num); // 调用倒序函数
    }

    system("\npause");
}
