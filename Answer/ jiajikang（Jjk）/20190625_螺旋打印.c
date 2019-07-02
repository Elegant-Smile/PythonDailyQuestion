/*

提高题：20190625
	给定 4 ， 应该输出如下形式的数据。
	01 12 11 10
	02 13 16 09
	03 14 15 08
	04 05 06 07

	给定 5 ， 应该输出如下形式的数据 。
	01 16 15 14 13
	02 17 24 23 12
	03 18 25 22 11
	04 19 20 21 10
	05 06 07 08 09


运行方式：如下所示


*/

#include <stdio.h>
#include <time.h>
#include <Windows.h>
#include <stdlib.h>
#define NMAX 100

int n;
//N阶螺旋矩阵
void getluoxuan1(int arrays[NMAX][NMAX])
{
	//核心算法：
	printf("从外到内螺旋，且数字从小到大，从矩阵的左上角开始从数字1开始螺旋\n");
	int c = 0, i, j;
	int z = n*n;
	int ou = 1;
	while (ou <= z)
	{
		i = 0;
		j = 0;
		for (i += c, j += c; j < n - c; j++)// 从左到右
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		for (j--, i++; i < n - c; i++) // 从上到下
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		for (i--, j--; j >= c; j--)//从右到左
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		for (j++, i--; i >= c + 1; i--)//从下到上
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		c++;

	}
}

void getluoxuan11(int arrays[NMAX][NMAX])
{
	printf("从矩阵的左上角开始从数字的最大值开始螺旋\n");
	int c = 0, i, j;
	int z = n * n;
	int ou = z;
	while (ou >= 1)
	{


		i = 0;
		j = 0;
		for (i += c, j += c; j < n - c; j++)//从左到右
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		for (j--, i++; i < n - c; i++) // 从上到下
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		for (i--, j--; j >= c; j--)//从右到左
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		for (j++, i--; i >= c + 1; i--)//从下到上
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		c++;
	}
}


void getluoxuan2(int arrays[NMAX][NMAX])
{
	printf("从矩阵的右上角开始从数字1开始螺旋\n");
	int c = 0, i, j;
	int z = n * n;
	int ou = 1;
	while (ou <= z)
	{


		i = 0;
		j = 0;
		for (i = c, j = n - c - 1; j >= c; j--)//从右到左
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		for (j++, i++; i < n - c; i++) // 从上到下
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		for (i--, j++; j < n - c; j++)//从左到右
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		for (j--, i--; i >= c + 1; i--)//从下到上
		{
			if (ou > z) break;
			arrays[i][j] = ou++;
		}
		c++;


	}
}

void getluoxuan22(int arrays[NMAX][NMAX])
{
	printf("从矩阵的右上角开始从矩阵的最大值开始螺旋\n");
	int c = 0, i, j;
	int z = n * n;
	int ou = z;
	while (ou >= 1)
	{
		i = 0;
		j = 0;
		for (i = c, j = n - c - 1; j >= c; j--)//从右到左
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		for (j++, i++; i < n - c; i++) // 从上到下
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		for (i--, j++; j < n - c; j++)//从左到右
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		for (j--, i--; i >= c + 1; i--)//从下到上
		{
			if (ou > z) break;
			arrays[i][j] = ou--;
		}
		c++;

	}
}


// 打印二维数组结果
void display(int arrays[NMAX][NMAX]) {

	int i, j;
	for ( i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			printf("%5d",arrays[i][j]);
		}
		printf("\n");
	}

}

int main()
{
	int arrays[NMAX][NMAX];
	printf("输入：");
	scanf("%d", &n);

	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			arrays[i][j] = 0;
		}
	}
	printf("从外到内螺旋，且数字从小到大，从矩阵的左上角开始从数字1开始螺旋\n");
	getluoxuan1(arrays);
	display(arrays);

	return 0;

}
