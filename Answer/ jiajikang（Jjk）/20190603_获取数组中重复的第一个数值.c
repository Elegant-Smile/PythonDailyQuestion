#include<stdlib.h>
#include <stdio.h>
#include <string.h>

/**
   
	在一个长度为n的数组里的所有数字都在0到n-1的范围内。
	数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
	请找出数组中任意一个重复的数字。
	例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
	那么对应的输出是第一个重复的数字2。


*/

void main() {

	int a[] = {2,3,1,0,2,5,3};
	int iTemp;
	printf("输出原数组\n");
	for (int i = 0; i < 7; i++)
	{
		printf("%d\t",a[i]);
		if (i==3)
		{
			//printf("\n");

		}

	}

	/*从小到大冒泡排序*/
	for (int i = 0; i < 7; i++)/*外层循环元素下标为1-9*/
	{
		for (int j = 6; j >=i; j--)/*内层循环元素下标为i-9*/
		{
			if (a[j]<a[j-1]) /*如果前一个数比后一个数大*/
			{
				/*交换两个数组元素的值*/
				iTemp = a[j - 1];
				a[j - 1] = a[j];
				a[j] = iTemp;

			}

		}

	}
	/*输出数组*/
	printf("\n输出排序后的数组\n");
	for (int i = 0; i < 7; i++)
	{
		printf("%d\t",a[i]);
		if (i==3)
		{
			//printf("\n");

		}

	}


	/*遍历输出第一个重复的数值*/
	printf("\n输出重复的数值\n");
	for (int i = 0; i < 7; i++)
	{
		//printf("%d\t", a[i]);
		if (a[i] == a[i+1])
		{
			printf("%d",a[i]);
			break;

		}

	}


	 

}