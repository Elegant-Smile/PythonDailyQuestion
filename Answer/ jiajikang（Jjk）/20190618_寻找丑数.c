/*

20190614
  提高题：
    把只含有质因子2、3、5的数称为丑数。
    例如6、8都是丑数，但14不是，  因为它包含质因子7。习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数，N由键盘输入。
  
  因子的概念：
      整数m除以n，得到无余数的商，则称n是m的一个因子。
	  如8的因子有1、2、4、8。而丑数要求的因子只包含2、3、5。所以丑数中的因子应理解为质因子。
	  即因子为质数，质数又称素数，指一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数。与质数相对应的数称为合数。

  思路：
     
     某个丑数肯定是前面丑数的2,3,5倍数。只需要从前往后生成即可。1,2,3,4,5,6,8,9,10,12,15，。。。。。。。

*/

/*

判断是否是丑数的算法：
   设待判断整数位M，M循环除以2直到不能整除，此时接着循环除以3直到不能整除，接着循环除以5直到商为1或者不能整除为止。
   商为1且余数为0则为丑数，否则为非丑数。
   如：丑数12

	12/2 = 6

	6/2 = 3;

	3/2 不能整除

	3/3 = 1; 结束，12是丑数

	非丑数26

	26/2 = 13

	13/2 不能整除

	13/3 不能整除

	13/5 不能整除

	结束，26不是整数

寻找丑数算法1：
（1）设置一个计数器用来统计出现的丑数的个数
（2）从1开始遍历每一个整数，判断是否是丑数，如果是丑数则计数器加1，否则遍历下一个整数。
（3）当计数器的值=N时，停止遍历，输出丑数。

*/








#include <stdio.h>
#include <time.h>
#include <string.h>
#include <Windows.h>

// 判断number是否是丑数
int isUgly(int number) { 
	while (number%2==0) // 能否被2整除
	{
		number = number / 2;
	}
	while (number%3==0) // 能否被3整除
	{
		number = number / 3;
	}
	while (number%5==0) // 能否被5整除
	{
		number = number / 5;
	}

	if (number == 1)
	{
		return 1;
	}
	else
	{
		return 0;
	}

}

// 寻找从1开始的第N个丑数
int findUgly(int N) { 
	int count = 0; // 计数
	int number = 1;// 从1开始遍历
	while (1)
	{
		if (isUgly(number)) // 如果number是丑数计数器+1
		{
			count++;
		}

		if (count == N) // 找到第N个丑数，返回丑数
		{
			// printf("count=%d\n", count);
			return number;
		}
		else
		{
			number++;
		}
	}
	
}
 

void main() {
	 
	int N = 0;
	scanf("%d",&N);

	clock_t start = clock();
	printf("%d\n",findUgly(N));
	clock_t stop = clock();
	printf("耗时：%lf\n",(double)(stop-start)/CLOCKS_PER_SEC);
	// system("pause");

}


 


 