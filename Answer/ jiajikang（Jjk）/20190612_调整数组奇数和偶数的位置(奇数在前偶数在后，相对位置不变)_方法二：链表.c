/*

20190612
提高题：
       输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
	   使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
     
*/

#define use _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <memory.h>
#include <malloc.h>
#define MAX 10000
 
// 方法二
/*

 (1） 先构建两个单链表,一个用来存放数组中奇数，一个用来存放数组中的偶数；
（2） 然后先将所有奇数拷回到原数组中，再将所有偶数拷回到原数组中。
（3） 运行输入方式：
                  1：数组长度
				  2：数组元素
  时间复杂度：O(n)

*/

// 创建链表节点
typedef struct LNode {

	int data; // 数据域
	struct LNode * next;// 指针域

}Linklist;

/*

number[] 调整好奇偶顺序后的数组
n 数组的长度

*/
void printResult(int number[],int n) {

	int i;
	for ( i = 0; i < n-1; i++)
	{
		printf("%d ",number[i]);

	}
	printf("%d\n",number[i]); // 最后一个字符
}

/*

 调整数组中数字的奇偶顺序
 number[] 待调整奇偶顺序的数组
 n 数组的长度

*/

void adjustOddEven(int number[],int n) {

	int i;
	Linklist *s = NULL;// s指向新构造的节点
	Linklist *oddNumber = (Linklist *)malloc(sizeof(Linklist)); // 用于存放奇数的链表
	Linklist *evenNumber = (Linklist *)malloc(sizeof(Linklist)); // 用于存放偶数的链表

	oddNumber->next = NULL;
	evenNumber->next = NULL;

	Linklist *p1 = oddNumber;// p1始终指向奇数链表的最后一个节点
	Linklist *p2 = evenNumber;// p2始终指向偶数链表的最后一个节点
	
	
	for ( i = 0; i < n; i++)
	{
		s = (Linklist *)malloc(sizeof(Linklist));
		scanf("%d",&number[i]);
		if ((number[i]&1)==1) // 如果输入的数据是奇数，则插入到奇数链表的末尾
		{
			s->data = number[i];
			s->next = p1->next;
			p1->next = s;
			p1 = s;
		}
		else //  如果输入的数据是偶数，则插入到偶数链表的末尾
		{
			s->data = number[i];
			s->next = p2->next;
			p2->next = s;
			p2 = s;
		}
	}

	// 先将奇数链表中的元素全部放入到数组中，再将偶数链表中的元素全部放入数组中
	i = 0;
	p1 = oddNumber->next;
	p2 = evenNumber->next;
	while (p1!=NULL)
	{
		number[i] = p1->data;
		p1 = p1->next;
		i++;
	}

	while (p2!=NULL)
	{
		number[i] = p2->data;
		p2 = p2->next;
		i++;
	}

	// 调用打印函数
	printResult(number,n);

}


void main() {
	
	int n;
	int arr1[] = { 1,2,3,2,1,1,1,1 };
	int len = sizeof(arr1) / sizeof(arr1[0]);
	// printf("%d",len);

	int number[MAX];
	scanf("%d",&n);
	adjustOddEven(number,n);
	
	// system("pause");

}