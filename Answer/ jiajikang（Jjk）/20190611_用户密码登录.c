/*
 * @Author: jjk
 * @Date: 2019-06-11 16:37:56
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-11 18:29:33
 *
 * 2：基础题
     2：基础题
      给用户三次输入用户名和密码的机会，要求如下：????????????????????????????????????????????????
      1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；????????????????????????????????????????????????

      2）当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。
 */

#include <stdio.h>
//#include <stdlib.h>
#include <string.h>
#define LENGTH 20

int main()
{
  int n = 0;
  char name[LENGTH];
  char password[LENGTH];
  while (1) // 死循环
  {
    printf("请输入用户名：");
    scanf("%s", &name);
    printf("请输入密码：");
    scanf("%s", &password);

    if (strcmp(name, "Kate") == 0)
    {
      /* code */
      if (strcmp(password, "666666") == 0)
      {
        /* code */
        printf("登录成功");
        break;
      }
    }

    n++;
    if (n == 3)
    {
      /* code */
      return 0;
    }
    printf("密码或用户名错误，请重新输入\n");

    /* code */
  }

  return 0;
}