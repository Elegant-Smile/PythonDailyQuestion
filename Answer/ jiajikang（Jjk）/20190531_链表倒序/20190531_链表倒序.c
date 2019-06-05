
#include<stdlib.h>
#include <stdlib.h>
#include "linknode.h"
/*

 * @程序功能：
 *         输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
 * @思路：
 *      所谓链表的逆置，是指“头变尾，尾变头”，将原来的“A B C D……”变成“……D C B A”，
 *      先从单链表模型来看

*/

void main() 
{
	struct student *head = NULL;// 头节点指针
	add(&head,1,70);
	add(&head,2,80);
	add(&head,3,90);
	add(&head,4,91);
	add(&head,5,72);

	//printf("%d,%f", head->num, head->score);// 打印数据
	//printf("%d,%f", head->pNext->num, head->pNext->score); // 打印数据
	//printf("%d,%f", head->pNext->pNext->num, head->pNext->pNext->score); // 打印数据
	showall(head); // 显示所有数据
 
	head = rev(head); // 逆转链表
	showall(head);

	system("pause");



}