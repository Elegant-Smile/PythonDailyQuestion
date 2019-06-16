/*

20190612
提高题：
       输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
	   使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
*/


// 方法三
/*
思路：
    实现了奇数在前，偶数在后（相对位置未能考虑）
    1、创建两个指针：第一个指针：指向数组的第一个数字，第二个指针：指向数组的最后一个数组
    2、两个指针相对移动，如果第一个指针指向的数字是偶数且第二个指针指向的数字是奇数，就交换这两个数字
    时间复杂度：O(n)

*/

#include <stdio.h>
#include <memory.h>
#include <malloc.h>
#include <string.h>
#define MAX 10000

int reorderOddEven (int array[],int len) {

	if (array ==NULL ||len == 0)
	{
		return 0;
	}
	
	int pBegin = 0;// 头指针
	int end = len - 1;// 尾指针
	while (pBegin<end)
	{
		while (pBegin<end && (array[pBegin]%2 !=0)) // 头指针移动，直到遇到偶数
		{
			pBegin++;
		}
		while (pBegin < end && (array[end] % 2 == 0)) // 将尾指针前移，直到为奇数
		{
			end--;
		}
		if (pBegin<end)
		{
			int temp = array[pBegin];
			array[pBegin] = array[end];
			array[end] = temp;
		}
	}

	// 循环打印
	for (int i = 0; i < len; i++)
	{
		printf("%d ",array[i]);
	}

	return 0;
}
 

void main() {
	int n;
	int arr1[] = { 1,2,3,4,5,6,7};
	int len = sizeof(arr1) / sizeof(arr1[0]);
	// printf("%d",len);

	reorderOddEven(arr1,len);
	
	// system("pause");

}