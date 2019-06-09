/*
 * @Author: jjk
 * @Date: 2019-06-07 23:26:07
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-07 23:47:07
 * 程序功能：请实现一个函数用来判断字符串是否表示数值(包括整数和小数)。
 * 例如，字符串"+100","5e2",-123","3.141 6"和"-1E-16"都表示数值。但是
 * "12e","1a3.14","1 .2.3","+-5"和"12e+4.3"都不是。
 */

/*

思路解析：
    1、e/E后面必须跟数字，且只能有一个e/E
    2、第一次出现的符号(+/-)要么开头，要么紧跟在e/E
    3、第二次出现的符号(+/-)只能紧接着e/E后面
    4、小数点只能出现一次，且只能出现在e/E前面
    5、不能出现除了0-9，+/-,e/E以外的字符
    前提条件：
        1 如果小数点前面没有数字自动补零。比如-.799相当于-0.799;
        2 如果符号后面没有数字自动补零。比如+e+相当于+0e+0;
由题目描述可知，
    一个数值字符串可能是常规的字符串，也可能是科学记数法表示的数值型字符串。
    就科学计数法表示可以发现，在字符‘E’、’e’的左侧表示的与常规数值型字符串一样，在字符‘E’、’e’的右侧，是整数。
    因而可以将数值型字符串按照科学计数法表示的分成两半分别检查即可。
*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 20

// 判断字符串是否包含某个字符
bool contains(char str[LENGTH], char ch)
{
  for (int i = 0; i < LENGTH; i++)
  {
    /* code */
    if (str[i] == ch)
    {
      /* code */
      return true;
    }
  }
  return false;
}

// 字符数组以字符ch开头
bool startWith(char str[], char ch)
{
  if (str[0] == ch)
  {
    /* code */
    return true;
  }

  return false;
}

// 判断是否是纯数字
bool isDigit(char num[])
{
  for (int i = 0; i < strlen(num); i++)
  {
    /* code */
    if (num[i] < '0' || num[i] > '9')
    {
      /* code */
      //printf("\n返回false");
      return false;
    }
  }

  return true;
}

// 判断是否是合法的数值(非科学计数法表示)
bool isDecimal(char str[])
{

  if (startWith(str, '-') || startWith(str, '+')) // 判断是否开头是：-/+
  {
    /* code */
    str = strncpy(str, str + 1, strlen(str)); // 复制除符号外字符串
    str[strlen(str)] = '\0';                  // 结束标识符
  }

  printf("\n打印左侧数据：\n"); // 除符号外字符串
  for (int i = 0; i < strlen(str); i++)
  {
    /* code */
    printf("%c\n", str[i]);
  }

  // printf("\n获取小数点的位置\n");
  if (contains(str, '.')) // 如果是小数点
  {
    /* code */
    int posE = -1;
    for (int i = 0; i < strlen(str); i++)
    {
      /* code */
      if (str[i] == '.')
      {
        /* code */
        posE = i;
        break;
      }
    }

    if (posE == 0 || posE == strlen(str) - 1)
    {
      /* code */
      return true;
    }
    // 小数点左边和右边
    char left[posE];
    char right[strlen(str) - posE - 1];
    strncpy(left, str, posE); //  复制除.外字符串:复制左边
    left[posE] = '\0';
    strncpy(right, str + posE + 1, strlen(str)); // 复制除符号外字符串：复制右边
    right[strlen(str) - posE - 1] = '\0';        // 结束标识符

    for (int i = 0; i < posE; i++)
    {
      /* code */
      printf("\n%c", left[i]);
    }

    printf("\n***********3333*********");
    
    for (int j = 0; j < strlen(str) - posE - 1; j++)
    {
      /* code */
      printf("\n%c", right[j]);
    }
    printf("\n是否是数值(1/0):");
    return isDigit(left) && isDigit(right); // 返回左边和右边的数值真假
  }
  else
  {
    // 如果不是小数
    /* code */
    // printf("%d",isDigit(str));
    printf("是否是数值(1/0):");
    return isDigit(str);
  }
}

int main(int argc, char const *argv[])
{
  /* code */
  // +100”,”5e2”,”-123”,”3.1416”和”-1E-16”都表示数值。
  // 但是”12e”,”1a3.14”,”1.2.3”,”+-5”和”12e+4.3”都不是。
  char str[] = "12.3E-124";
  printf("原字符串：");
  for (int i = 0; i < strlen(str); i++)
  {
    /* code */
    printf("%c",str[i]);
  }
  
  int posE = -1; // 位置标识符
  // 第一步：判断是否是使用科学计数法表示，将将数组分为两部分判断
  if (contains(str, 'E') || contains(str, 'e')) //
  {

    /* code */
    printf("\n包含字符e/E"); // 且获取字符e/E的位置
    for (int i = 0; i < strlen(str); i++)
    {
      /* code */
      if (str[i] == 'E' || str[i] == 'e')
      {
        /* code */
        posE = i;
        printf("\ni=%d", i);
        break; // 结束此次循环
      }
    }

    // 判断'E'||'e'在开始还是结尾的位置
    if (posE == 0 || posE == strlen(str) - 1)
    {
      /* code */

      return false;
    }

    // e/E左边和右边的计算
    char left[posE];
    char right[strlen(str) - posE - 1];
    printf("\n位置");
    // 以字符e/E为分割线，复制左边和右边的字符串
    strncpy(left, str, posE);                    // 复制除符号外字符串:复制左边
    left[posE] = '\0';                           // 结束标识符
    strncpy(right, str + posE + 1, strlen(str)); // 复制除符号外字符串：复制右边
    right[strlen(str) - posE - 1] = '\0';        // 结束标识符

    // 左边left判断和非科学计数法一样
    // 右边right判断必须为整数
    printf("\n*********left***********");
    for (int i = 0; i < posE; i++)
    {
      /* code */
      printf("\n%c", left[i]);
    }
    printf("\n*********right***********");
    for (int j = 0; j < strlen(str) - posE - 1; j++)
    {
      /* code */
      printf("\n%c", right[j]);
    }

    // 判断e/E右侧的字符串开头符号是否为-/+且复制除符号以外的字符
    if (startWith(right, '-') || startWith(right, '+'))
    {
      /* code */
      strncpy(right, right + 1, strlen(right)); // 复制除符号外字符串：复制右边
      right[strlen(str) - posE - 1] = '\0';     // 结束标识符
    }

    printf("\n*********right除去符号***********");
    for (int j = 0; j < strlen(str) - posE - 1; j++)
    {
      /* code */
      printf("\n%c", right[j]);
    }
    printf("\n*********判断是否符合***********");

    printf("%d", isDecimal(left) && isDigit(right)); // 右侧只能是数字
    //return isDecimal(left) && isDigit(right); // 这里处理了左侧，右侧：e/E且-/+后面的数据
  }
  else
  {
    /* code */
    printf("不包含字符e/E");
    // printf("\n%d",isDigit(str));
    printf("\n%d", isDecimal(str));
    //return isDigit(str);
  }

  return 0;
}