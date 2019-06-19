/*

20190614
基础题：
       读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
       第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。。

思路：
     等差数列公式：a = 1+2(n-1) = 2*n-1
*/


#include <stdio.h>
#include <malloc.h>
#include <string.h>
#define MAX 10000


void main() {
	int n;
	int arr1[] = { 1,2,3,4,5,6,7};
	int len = sizeof(arr1) / sizeof(arr1[0]);
	// printf("%d",len);
	//printf("请输入一个奇数：");
	scanf("%d",&n);
	for (int i = 1; i < n; i++) //控制行数的第一层循环
	{
		for (int j = 1; j <= n-i; j++) // 添加空格为了好看
		{
			printf("  ");
		}

		for (int k = 0; k < 2*i-1; k++) // 打印星号
		{
			printf("* ");
		}
		printf("\n");

	}

	// system("pause");

}


 


 