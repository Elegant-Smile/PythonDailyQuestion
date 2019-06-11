/*
 * @Author: jjk
 * @Date: 2019-06-03 21:31:04
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-10 16:05:42
 * 程序功能：
*       字符串的加密和解密:
*       恺撒密码是古罗马恺撒大帝用来对军事情报进行加解密的算法，
        它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，
*       即，字母表的对应关系如下：
         原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
         密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
         对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26
         上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26
         假设用户可能使用的输入包含大小写字母a~zA~Z、空格和特殊符号，
         请编写一个程序，对输入字符串进行恺撒密码加密，直接输出结果，其中空格不用进行加密处理。使用input()获得输入。
 *
 * 思路：
    1、while无线循环，声明两个字符数组：保存明文和密文
    2、首次用户输入字符串，进行明文加密成密文操作
    3、之后用户输入命令字符实现判断：输入：“1”加密新的明文，输入：“2”对“明文”反向解密，输入：“3” 退出
 *
 *
 *
 *
 *
 */
#include <stdio.h>


// A=65,Z=90,a=97,z=122
// 加密
void CaesarEncrypt(char *pstrBff, int nKey) // nKry：偏移量
{
  int count;
  for (count = 0; pstrBff[count] != '\0'; count++)
  {
    if ((pstrBff[count] >= 'A' && pstrBff[count] <= 'Z') || (pstrBff[count] >= 'a' && pstrBff[count] <= 'z'))
    {
      pstrBff[count] += nKey;
      if (pstrBff[count] > 'Z' && pstrBff[count] < 'a')
        pstrBff[count] -= 26; // -26
      else if (pstrBff[count] > 'z')
        pstrBff[count] -= 26;
    }
  }
}

// 解密
void CaesarDecrypt(char *pstrBff, int nKey)
{
  int count;
  for (count = 0; pstrBff[count] != '\0'; count++)
  {
    if ((pstrBff[count] >= 'A' && pstrBff[count] <= 'Z') || (pstrBff[count] >= 'a' && pstrBff[count] <= 'z'))
    {
      pstrBff[count] -= nKey;
      if (pstrBff[count] < 'A')
        pstrBff[count] += 26;
      else if (pstrBff[count] > 'Z' && pstrBff[count] < 'a')
        pstrBff[count] += 26;
    }
  }
}



int main(void)
{

  char strBff[100]; // 原文
  int bExit = 0;    // 标识符
  unsigned int nSel, nKey = 0;
  printf("“1”加密新的明文，输入：“2”对刚加密的密文进行解密，输入：“3”退出");

  while (!bExit)
  {
    printf("\n**************************\n");
    printf("请输入指令：");
    scanf("%d", &nSel);
    while (getchar() != '\n')
      ;
    switch (nSel)
    {
    case 1:
      printf("请输入要加密的明文：");
      gets(strBff);
      printf("请输入偏移量：");
      scanf("%d", &nKey);  // 偏移量
      while (getchar() != '\n')
        ;
      CaesarEncrypt(strBff, nKey); // 加密
      printf("加密后的密文是: %s\n", strBff);
      break;
    case 2:
      printf("请输入需要解密的明文：");
      gets(strBff);
      printf("请输入偏移量：");
      scanf("%d", &nKey); // 偏移量
      while (getchar() != '\n')
        ;
      CaesarDecrypt(strBff, nKey);  //解码
      printf("解码后的明文：%s\n", strBff);
      break;
    case 3:
      return 1;
    default:
      printf(".\n");
    }
  }
  return 0;
}
