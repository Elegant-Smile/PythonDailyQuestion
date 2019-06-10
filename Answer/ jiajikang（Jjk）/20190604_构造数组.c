/*

提高题：
		给定一个长度为n的列表 A ，请构建一个长度为n的列表 B ，
		其中B中的元素:
		B[i]=A[0] A[1] ...  A[i-1] A[i+1]... A[n-1]。
		要求不能使用除法。
		比如，给定一个长度为5的列表 A=[1, 2, 3, 4, 5]
思路：
	   B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
	   第一步：计算A[0]*A[1]*...A[i]
	   第二步：载乘以A[i-1]*A[i+1]*...*A[n-1]
参考链接：https://blog.csdn.net/Rebirth_Love/article/details/51612096

*/
#include<stdlib.h>
#include <stdio.h>
#include <string.h>
#define LENGTH 5
//#define LEN(x) sizeof(x) / sizeof(x[0]) // 计算数组长度


void main() {

	int a[] = { 1, 2, 3, 4, 5 };
	//int length = sizeof(a) / sizeof(int);
	//printf("%d",length);
	 

	int d[LENGTH];
	int c[LENGTH];
	int b[LENGTH];

	d[0] = 1; // 计算d
	for (int i = 1; i < LENGTH; i++)
	{
		d[i] = d[i - 1] * a[i - 1];
	}

	c[5 - 1] = 1;// 计算c
	for (int j = LENGTH - 1; j > 0; j--)
	{
		c[j - 1] = c[j] * a[j];
	}


	// 计算b
	for (int i = 0; i < LENGTH - 1; i++)
	{
		b[i] = d[i] * c[i];
	}

	for (int i = 1; i < LENGTH; i++)
	{ 
		printf("%d",b[i]);
	}
 

}
