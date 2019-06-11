/*
 * @Author: jjk
 * @Date: 2019-06-10 16:11:49
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-11 16:57:08
 *
 * 请实现一个函数用来找出字符串中第1个只出现1次的字符。
      例如，
      当从字符串中只读出前两个字符"go"时，第1个只出现次的字符是"g"。
      当从该字符串中读出前六个字符"google"时，第1个只出现1次的字符是“l”。


   1、针对一个字符串，获取遍历前n个字符
   2、针对前n个字符，实现查找：只出现1次的字符并输出
   输入描述：输入一个非空字符串
   输出描述：输出第一个只出现一次的字符，如果不存在输出-1
   示例：go g；google l

   1、没有抽烟黑历史
   2、三观必须合得来
   3、勤快上进
   4、感情态度：专一（认认真真，都是很负责，都是奔着结婚的心态，每一段感情都专注的，不能脚踏两条船，并且如果不爱了，及时说明）
   5、家教：善良，有礼貌（我理解：至少要会来事呀，嘴巴甜呀，见了长辈最起码要留个好印象呀）
   5、性格：脾气好，能包容(能包容对方的一些毛病呀等等），活泼！开朗！外向
   6、家庭背景：无要求
   
   备注：不接受异地恋、网恋
   
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LENGTH 30
const int Tabsize = 256;
int hashtab[256]; // int型全局变量

int main()
{
   char str[LENGTH] = "0";

   while (scanf("%s", &str))
   {
      /* code */
      bool flg = false;
      for (int i = 0; i < Tabsize; i++)
      {
         /* code */
         hashtab[i] = 0;
      }
      for (int i = 0; i < strlen(str); i++)
      {
         /* code */
         hashtab[str[i]]++;
      }

      for (int i = 0; !flg && i < strlen(str); ++i)
      {
         /* code */
         if (hashtab[str[i]] == 1)
         {
            /* code */
            printf("%c\n", str[i]);
            flg = true;
            break;
         }
      }

      if (!flg)
      {
         /* code */
         printf("-1");
      }
   }

   return 0;
}
