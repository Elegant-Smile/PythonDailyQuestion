/*
 * @Author: jjk 
 * @Date: 2019-05-29 19:32:05 
 * @Last Modified by:   jjk 
 * @Last Modified time: 2019-05-29 19:32:05 
 * 基础题：
        设计一个复利计算函数invest（），
        它包含三个参数：amount（资金），rate（年利率），time（投资时间）。
        键盘输入每个参数后，输出结果：返回每一年的资金总额
        比如，amount = 10000 , rate = 8% ,time = 5
 */

#include <stdio.h>
double invest(double amount, double rate, int time)
{
    double sum_zijin = 0.0;
    sum_zijin = amount + amount * rate * time;
    printf("%.2lf", sum_zijin);
    return 0;
}

int main(int argc, char const *argv[])
{
    /* code */
    double amount;
    double rate;
    int time;
    printf("请输入总金额、利率、时间：");
    scanf("%lf%lf%d", &amount, &rate, &time);
    invest(amount, rate, time);
    return 0;
}
