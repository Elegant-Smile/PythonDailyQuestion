/*
 * @Author: jjk
 * @Date: 2019-05-24 10:09:14
 * @Last Modified by: jjk
 * @Last Modified time: 2019-05-24 10:59:54
 * 程序功能：
 *        提高题：打印出杨辉三角形（实现根据键盘输入数字打印出相应数量的行，比如，输入10，则打印出10行）
 */

/*

思路：
    定义一个二维数组，所有元素先初始化为0；
    给数组的第1列和对角线元素赋值为 1； 其余元素a[i][j] = a[i - 1][j - 1] + a[i - 1][j] ；
    输出这个二维数组的下三角。

*/

#include <stdio.h>
#include <stdlib.h>
#define N 14

int main(int argc, char *argv[])
{
    int n = 0;
    
    while (n<=0||n>=13)
    {
        printf("请输入行数：");
        scanf("%d",&n);
    }
    
    int a[N][N] = {0}; // 初始化二维数组a，所有的元素为0
    // 初始化二维数组
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++) // j<=i,第i行，只有i+1个
        {
            if (j == 0 || i == j) // 如果是第一列，全为1
            {
                a[i][j] = 1;
            }
            else
            {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            }
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++)
    {
        printf("%*d", 30 - i * 2, a[i][0]); // 第一列
        for (int j = 0; j < i; j++)
        {
            printf("%4d", a[i][j]);
        }
        printf("\n");
    }

    return 0;
}
