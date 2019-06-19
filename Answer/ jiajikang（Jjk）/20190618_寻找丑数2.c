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

 想办法从上一个丑数推断出下一个丑数，而不需要从1开始遍历再判断。从1开始的10个丑数分别为1，2，3，4，5，6，8，9，10，12。
 可以发现除了1以外，丑数都是由某个丑数*2或者*3或者*5得到的。如2是丑数1*2得到的，3是丑数1*3得到的，4是丑数1*4得到的，5是丑数1*5得到的，6是丑数2*3得到的……

具体算法步骤：

（1）从第一个丑数1开始，求出1*2=2 ，1*3=3 ，1*5 = 5；

（2）取上面乘积中大于1的最小值2，作为第二个丑数（丑数是个递增序列，所以第i+1个丑数一定比第i个丑数）

（3）求丑数2之前的丑数与2、3、5的乘积：1*2=2 ，1*3=3 ，1*5 = 5； 2*2 = 4； 2*3 = 6； 2*5 =10；

（4）取上面乘积中大于2的最小值3，作为第三个丑数

       ……

       ……

（i）取出丑数i之前的丑数分别与2、3、5的乘积

（i+1）取乘积中大于i的最小值作为丑数

（i+2）重复(i)(i+1)的步骤直到计数器等于N
 
*/

#include <stdio.h>
#include <time.h>
#include <string.h>
#include <Windows.h>
#define MaxLen 99999

// 用于求出3个数的最小值
int compare(int chenTwo,int chenThree, int chenFive) {
	if (chenTwo<=chenThree)
	{
		if (chenTwo<=chenFive)
		{
			return chenTwo; // 返回最小值
		}
		else
		{
			return chenFive;
		}
	}
	else if (chenThree<=chenFive)
	{
		return chenThree;
	}
	else
	{
		return chenFive;
	}
	
}
 
// 找出第N个丑数
int findUgly(int N) {
	
	int ugly[MaxLen] = { 1 };// 用于保存丑数的数组
	int count = 1;// 数组中仅有丑数1，所以计数1


	while (1) // 进入到无线循环中
	{
		int chenTwo = 0;
		int chenThree = 0;
		int chenFive = 0;
		/*
			 ugly数组中最新的一个丑数为ugly[count-1]
			 ugly[count-1]之前的丑数与2相乘
			 求出第一个乘积大于ugly[count-1]的值保存在chenTwo中
		*/
		for (int i = 0; i < count; i++)
		{
			if (ugly[i]*2>ugly[count-1])
			{
				chenTwo = ugly[i] * 2;
				break;
			}
		}

		/*
			ugly数组中最新的一个丑数为ugly[count-1],
			ugly[count-1]之前的丑数与3相乘,
			求出第一个乘积大于ugly[count-1]的值保存在chenThree中
		*/
		for (int i = 0; i < count; i++)
		{
			if (ugly[i]*3 > ugly[count-1])
			{
				chenThree = ugly[i] * 3;
				break;
			}
		}

		/*
			ugly数组中最新的一个丑数为ugly[count-1],
			ugly[count-1]之前的丑数与5相乘,
			求出第一个乘积大于ugly[count-1]的值保存在chenFive中
        */
		for (int i = 0; i < count; i++)
		{
			if (ugly[i] * 5 > ugly[count - 1])
			{
				chenFive = ugly[i] * 5;
				break;
			}
		}

		//chenTwo，chenThree，chenFive的最小值为新的丑数，存入ugly数组中
		ugly[count] = compare(chenTwo,chenThree,chenFive);
		count++;
		if (count==N) // 第N个丑数
		{
			return ugly[count - 1];
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


 


 