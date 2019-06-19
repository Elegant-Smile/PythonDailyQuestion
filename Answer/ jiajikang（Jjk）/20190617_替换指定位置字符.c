/*

20190617
基础题：
		用户输入一个字符串，修改该字符串中哪个位置的字符，程序就会输出修改后的结果。
		比如用户输入 ：
		字符串>> fkjava.org
		字符位置>> 6
		替换字符>> -
		程序将会输出：
		替换后的字符串>> fkjava-org
  
*/


#include <stdio.h>
#include <time.h>
#include <string.h>
#include <Windows.h>
#define MaxLen 100
 
 
void tihuan(char str[],char substr,int number) {
	for (int i = 0; i < strlen(str); i++)
	{

		if (i == number)
		{
			str[i] = substr;
		}
	}

	for (int i = 0; i < strlen(str); i++)
	{
		printf("%c",str[i]);
	}
}


void main() {
	 
	char str[MaxLen];
	char substr;
	int number = 0;
	printf("字符串>>");
	scanf("%s",&str);

	printf("字符位置>>");
	scanf("%d",&number);

	printf("替换字符>>");
	scanf(" %c",&substr);

	tihuan(str,substr,number);

	/*clock_t start = clock(); 
	clock_t stop = clock();
	printf("耗时：%lf\n",(double)(stop-start)/CLOCKS_PER_SEC);*/
	// system("pause");

}


 


 