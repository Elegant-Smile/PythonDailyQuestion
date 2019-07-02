/*

提高题：20190627
	创建一个定时器，实现以下功能：
		1.一秒钟之后，在屏幕打印一句话“Timer headle!”
		2.之后每隔一秒钟在屏幕打印一次“Timer headle!”
		3.在第2步加个限制，只允许持续10秒


运行方式：如下所示
F:\VS2017\VS2017_workstation\语法分析\语法分析>a.exe
	Today's date and time: Tue Jul 02 15:45:49 2019
	Timer headle!Timer headle!
	Timer headle!
	Timer headle!
	Timer headle!
	Timer headle!
	Timer headle!
	Timer headle!
	Timer headle!
	Timer headle!

*/

#include <stdio.h>
#include <time.h>
#include <Windows.h>

int main()
{

	//int i, j;
	//i = time((time_t*)NULL);
	//Sleep(2000); //延迟2s
	//j = time((time_t*)NULL);
	//printf("延时了%d秒", j - i);

	int i = 0;
	time_t t;
	time(&t);
	printf("Today's date and time: %s", ctime(&t));
	Sleep(1000); // 延迟两秒
	printf("Timer headle!");
	
	while (1)
	{

		printf("Timer headle!\n");
		Sleep(1000); // 延迟1秒
		i++;
		if (i==10)
		{
			break;
		}
	}

	return 0;
}