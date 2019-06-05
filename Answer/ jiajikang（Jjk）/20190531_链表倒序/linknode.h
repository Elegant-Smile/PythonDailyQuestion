
#include <stdio.h>
#include <stdlib.h>

struct student
{
	int num;// 编号
	float score; // 代表成绩
	struct  student *pNext; // 存储下一个节点的地址
};

typedef struct student ST;// 简写结构体声明

void add(ST **phead,int inum,float iscore);// 函数声明，传入头结点的地址，然后插入数据

void showall(ST *head);// 传递头结点，显示所有数据

ST *rev(ST *head);// 实现逆转
