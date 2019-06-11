/*
 * @Author: jjk
 * @Date: 2019-06-10 16:11:49
 * @Last Modified by: jjk
 * @Last Modified time: 2019-06-11 18:59:24
 *
 *
 * 20190611:
 * 1:基础概念实践题
     给定任意一个整数，打印出该整数的十进制、八进
制、十六进制（大写）、二进制形式的字符串。
   
   3：提高题：
      一只青蛙一次可以跳上1级台阶，也可以跳上2级。
      求该青蛙跳上一个n级的台阶总共有多少种跳法
      注：先后次序不同 算作是不同的结果
   

思路：
    说明：?

1）这里的f(n) 代表的是n个台阶有一次1,2,...n阶的 跳法数。
2）n = 1时，只有1种跳法，f(1) = 1
3) n = 2时，会有两个跳得方式，一次1阶或者2阶，这回归到了问题（1） ，f(2) = f(2-1) + f(2-2)?
4) n = 3时，会有三种跳得方式，1阶、2阶、3阶，那么就是第一次跳出1阶后面剩下：f(3-1);第一次跳出2阶，剩下f(3-2)；第一次3阶，那么剩下f(3-3)
   因此结论是f(3) = f(3-1)+f(3-2)+f(3-3)
5) n = n时，会有n中跳的方式，1阶、2阶...n阶，得出结论：f(n) = f(n-1)+f(n-2)+...+f(n-(n-1)) + f(n-n) => f(0) + f(1) + f(2) + f(3) + ... + f(n-1)
6) 由以上已经是一种结论，但是为了简单，我们可以继续简化：
   f(n-1) = f(0) + f(1)+f(2)+f(3) + ... + f((n-1)-1) = f(0) + f(1) + f(2) + f(3) + ... + f(n-2)
   f(n) = f(0) + f(1) + f(2) + f(3) + ... + f(n-2) + f(n-1) = f(n-1) + f(n-1)
   可以得出：
???f(n) = 2*f(n-1)
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int jumpFloor(int number)
{

   if (!number)
   {
      /* code */
      return 0;
   }

   return (number == 1) ? 1 : 2 * jumpFloor(number - 1);
}

int main()
{
  int number;
  while (1)
  {
     /* code */
     printf("请输入台阶数：");
     scanf("%d", &number);
     printf("一共跳：%d层台阶\n", jumpFloor(number));
     if (number == 0)
     {
        /* code */
        break;
     }
     
  }
  
   return 0;
}
