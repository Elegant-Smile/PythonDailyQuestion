/*
 * @Author: jjk
 * @Date: 2019-06-11 17:12:31
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-11 17:56:17
 * 
 * 20190611
 * 1:基础概念实践题
     给定任意一个整数，打印出该整数的十进制、八进制、十六进制（大写）、二进制形式的字符串。
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 二进制
void decToBin(int num)
{
  if (num > 0)
  {
    decToBin(num / 2);
    printf("%d", num % 2);
  }
}


int main(int argc, char const *argv[])
{
  /* code */
  int number;
  printf("给定任意一个整数，打印出该整数的十进制、八进制、十六进制（大写）、二进制形式的字符串。");
  printf("\n请输入：");
  scanf("%d", &number);
  printf("十进制：%d\n", number);
  printf("八进制：%o\n", number);
  printf("十六进制：%X\n", number);
  printf("二进制：");
  decToBin(number);

      return 0;
}
