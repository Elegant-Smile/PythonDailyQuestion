/*

基础题：20190627
	定义一个 fn(n)函数，其中 n 表示输入 n 行 n 列的矩阵(数的方阵)。
	在输出时，先输出 n 行 n 列的矩阵，再输出该矩阵的转置形式 。 例如，当参数为 3 时，先输出：
	1 2 3
	4 5 6
	7 8 9
	再输出：
	1 4 7
	2 5 8
	3 6 9


运行方式：如下所示
        gcc 程序.c/a.exe
		请输入行和列n:3
		输入矩阵元素:
		输入元素 a11: 1
		输入元素 a12: 2
		输入元素 a13: 3
		输入元素 a21: 4
		输入元素 a22: 5
		输入元素 a23: 6
		输入元素 a31: 7
		输入元素 a32: 8
		输入元素 a33: 9

*/

#include <stdio.h>

int fn(int n) {

	int a[10][10], transpose[10][10];

	// 存储矩阵的元素
	printf("\n输入矩阵元素:\n");
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf("输入元素 a%d%d: ", i + 1, j + 1);
			scanf("%d", &a[i][j]);
		}
	}


	// 显示矩阵 a[][] */
	printf("\n输入矩阵: \n");
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
		{
			printf("%d  ", a[i][j]);
			if (j == n - 1)
				printf("\n\n");
		}
	// 转换
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			transpose[j][i] = a[i][j];
		}
	}

	// 转化后的矩阵
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf("%d  ",transpose[i][j]);
			if (j==n-1)
			{
				printf("\n\n");
			}
		}
	}

	return 0;
}


// 主函数
void main() {

	int n;
	printf("请输入行和列n:");
	scanf("%d", &n);
	fn(n);



}