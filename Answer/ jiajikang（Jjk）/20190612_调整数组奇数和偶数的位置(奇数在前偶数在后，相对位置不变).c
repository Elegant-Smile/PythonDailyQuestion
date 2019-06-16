/*

20190612
提高题：
       输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
	   使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
     
方法一：
       时间复杂度为O(n),但是空间复杂度较高的。 
　　   1、申请另外两个数组，每次输入数据时，直接比对是奇数还是偶数，顺序存放在两个数组中，并记录下标的变化。
	   2、最后两个数组顺序输出就行了



*/

#define use _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <memory.h>
#include <malloc.h>
#define N 100000
#define MAX 10000
int arr[N];
int arr1[N];
int arr2[N];
// 方法1：
int main(void) {
	
	int n, i, num_arr1, num_arr2;
	printf("请输入数组长度：");
	while (scanf("%d", &n) != EOF && n > 0) {
		num_arr1 = num_arr2 = 0;
		memset(&arr, 0, sizeof(int)*N);
		memset(&arr1, 0, sizeof(int)*N);
		memset(&arr2, 0, sizeof(int)*N);
		
		printf("请输入测试数据：\n");
		for (i = 0; i < n; i++) {
			
			scanf("%d", &arr[i]);
			if (arr[i] % 2 == 1) {
				arr1[num_arr1++] = arr[i];
			}
			else {
				arr2[num_arr2++] = arr[i];
			}
		}

		// 打印奇数
		for (i = 0; i < num_arr1; i++) {
			printf("%d ", arr1[i]);
		}
		// 打印偶数
		for (i = 0; i < num_arr2; i++) {
			printf("%d ", arr2[i]);
		}
		printf("\n");
		//printf("%d\n", arr2[num_arr2 - 1]);
	}
	return 0;
}

 