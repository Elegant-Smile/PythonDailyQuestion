/*
 * @Author: jjk
 * @Date: 2019-06-11 16:37:56
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-11 16:46:16
 *  请实现一个函数用来找出字符串中第1个只出现1次的字符。
      例如，
      当从字符串中只读出前两个字符"go"时，第1个只出现次的字符是"g"。
      当从该字符串中读出前六个字符"google"时，第1个只出现1次的字符是“l”。


   1、针对一个字符串，获取遍历前n个字符
   2、针对前n个字符，实现查找：只出现1次的字符并输出
   输入描述：输入一个非空字符串
   输出描述：输出第一个只出现一次的字符，如果不存在输出-1
   示例：go g；google l


   即我们只遍历一次字符串，然后下来记录每个字符出现的次数。
   对于字符串来讲，一般采用哈希表，然后对哈希表进行查询即可。如果只针对字符串为小写字母形式，则简单的采用int hashtable[26] = {0};来做存储。
 
 */

#include <iostream>
#include <string>

using namespace std;
const int Tabsize = 256;
int hashtab[Tabsize]; // int型全局变量

int main()
{
  string str;
  while (cin >> str) // 输入字符串
  {
    bool flg = false;
    for (int i = 0; i < Tabsize; ++i) 
    {
      hashtab[i] = 0; 
    }
    //范围for循环对输入字符串进行第一次遍历，统计每一种字符出现的次数
    for (int i = 0; i < str.size(); ++i)
    {
      hashtab[str[i]]++;
    }
    //对输入字符串进行第二次遍历: 输出符合要求的字符
    for (int i = 0; !flg && i < str.size(); ++i)
    {
      if (hashtab[str[i]] == 1)
      {
        cout << str[i] << endl;
        flg = true;
        break;
      }
    }
    
    if (!flg)
      cout << "-1" << endl;
  }
  return 0;
}