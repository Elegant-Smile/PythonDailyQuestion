#include "linknode.h"

void add(ST **phead, int inum, float iscore) {

	if (*phead ==NULL) // 判断链表是否为空
	{
		ST *newnode = (ST *)malloc(sizeof(ST));// 分配内存
		 
		newnode->num = inum; // 节点初始化
		newnode->score = iscore;
		newnode->pNext = NULL;
		*phead = newnode;// 让头指针指向这个节点
	}
	else
	{
		// 尾部插入的方式
		// 链表不为空
		ST *p = *phead;// 指向头结点
		// p存储最后一个节点的地址
		while (p->pNext!= NULL) // 循环到最后一个节点的地址
		{
			p = p->pNext;// 不断循环向前
		}
		//p = p->PNext == null 循环终止

		ST *newnode = (ST *)malloc(sizeof(ST));// 分配内存
		newnode->num = inum; // 节点初始化
		newnode->score = iscore;
		newnode->pNext = NULL;
		p->pNext = newnode;// 链接上
	}


}

// 显示所有数据
void showall(ST *head) { // 传递头结点，显示所有数
	// 遍历所有的节点
	while (head!=NULL)
	{
		printf("\nnum=%d,score=%f",head->num,head->score);
		printf(" %p,%p",head,head->pNext); // 打印两个节点的地址
		head = head->pNext;// 指针不断向前循环
	}
}


ST *rev(ST *head) {


	ST *p1, *p2, *p3;
	p1 = p2 = p3 = NULL;

	if (head ==NULL || head->pNext==NULL) // 如果只有一个节点，或者链表为空
	{
		return head;// 返回头节点
	}
	p1 = head;
	p2 = head->pNext;
	while (p2!=NULL) // 从第二个到最后一个节点开始循环
	{
		p3 = p2->pNext;// 布局三个节点
		p2->pNext = p1;// 指向前面一个节点
		p1 = p2;// 指针向前移动，从第二个到最后一个节点全部指向前面的节点
		p2 = p3;

	}
	head->pNext = NULL; // 代表链表的结束，设置第一个节点指向为空
	head = p1;// 指向最后一个节点

	return head;// 副本机制，改变的head，并不会生效，需要返回值赋值生效



}