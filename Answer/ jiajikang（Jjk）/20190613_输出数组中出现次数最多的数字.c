/*

20190616
提高题：
    列表中有一个数字出现的次数超过列表长度的一半，请找出这个数字。
    例如，输入一个长度为 9 的列表[1, 2, 3, 2, 2, 2, 5, 4, 2]。数字 2 出现了5次，超过列表长度的一半，因此输出2。如果不存在则输出0。



思路：
    1、找出次数超过数组一半的数字，也就说，它出现的次数比其他所有数字出现次数的和还要多，即：数字出现最多且大于数组长度的一半
	2、设置两个变量：a:保存数字，b:保存次数，开始：保存数组的第一个元素，次数设置为：1
	3、遍历数组：
	   a：如果下一个数字和当前保存的数字相同，则次数count递增1
	   b: 如果下一个数字和当前保存的数字不同，则次数count递减1
	   c：如果次数为0；需要保存下一个数字且设置次数count为1
	   d: 由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，所以要找的数字是：最后一次把次数设为1时对应的数字(返回遍历完之后的数字，最后保存的数字)。
	   e: 判断该数字的出现次数是否超过了数组长度的一半，因为可能数组中并不包含这样的数字。
 时间复杂度：O(n)
 
 解析：1, 2, 3, 2, 2, 2, 5, 4, 2
 第一次：a[0] == a[1]      N
         count--   count = 0
 第二次：cur移位下一个
         cur=a[1]
		 count = 1
 第三次：a[1] == a[2]       N
         count--   count = 0
 第四次：cur移位下一个
         cur=a[2]
		 count = 1
 第五次：a[2] == a[3]       N
         count--   count = 0
 第六次：cur移位下一个
         cur=a[3]
		 count = 1
 第七次:a[3] == a[4]        Y
        count++    count = 2
 第八次:a[3] == a[5]        Y
         count++    count = 3
 第九次:a[3] == a[6]        N
         count--   count = 2
 第十次:a[3] == a[7]       N
         count--   count = 1
		 
 第十一次：a[3] == a[8]    Y
         count++    count = 2
		 printf("a[%d]=%d",a[i]) // 即a[8] = 2
		 
           

*/

#include <stdlib.h>
#include <stdio.h>
// #include <stdbool.h> 
int MorethatHalf(int a[], int size) {

	int cur = a[0];// 数组第一个元素的值：数字
	int count = 1; // 
	int i = 0;
	for (i = 0; i < size; ++i) // 遍历数组 ++i：先改变i的值即+1之后在使用i的值
	{
		if (count == 0)
		{
			cur = a[i]; // 循环数组中：当前的数字
			count=1;
		}
		else if (cur == a[i])
		{
			count++;// 当前数字和下一个数字相同，统计个数
		}
		else
		{
			count--; // 当前数字和下一个数字不相同，count--
		}
		 
	}
	
	 printf("count=%d\n",count);
	 
	 return cur;

}




void main() {
	
	int a[] = {1, 2, 3, 2, 2, 2, 5, 4, 2};
	int len = sizeof(a) / sizeof(a[0]);// 数组长度
	printf("len =%d\n",len); // 打印数组长度
	printf("%d\n", MorethatHalf(a,len));// 打印输出结果
	system("pause");


	 
}
 