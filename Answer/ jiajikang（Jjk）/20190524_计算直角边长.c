/*
 * @Author: jjk 
 * @Date: 2019-05-24 09:56:11 
 * @Last Modified by: jjk
 * @Last Modified time: 2019-05-24 10:09:06
 */

#include <stdio.h>
#include <math.h>
// #include <string.h>
// #include <stdlib.h>

void trans(double num1, double num2)
{

    double result = 0.0, pow1, pow2;
    pow1 = pow(num1, 2);
    pow2 = pow(num2, 2);
    result = sqrt(pow1 + pow2);

    printf("The right triangle third side's length is %.1lf", result);
}

int main()
{

    double num1, num2;
    printf("\nPlease enter the side length 1：");
    scanf("%lf", &num1);
    printf("\nPlease enter the side length 2：");
    scanf("%lf", &num2);

    trans(num1,num2); // 调用计算斜边长函数

    return 0;
}