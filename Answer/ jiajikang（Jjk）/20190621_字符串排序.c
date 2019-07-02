/*

提高题：20190621
	输入一个字符串按字典序打印出该字符串中字符的所有排列。
    例如，输入字符串abc，则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
    要求：
        ①字符串长度不超过9(可能有字符重复)
        ②字符只包括大小写字母
备注：剑指offer
运行方式：如下所示
*/


/*

分析：
	这是一道很好的考查对递归理解的编程题。
	我们以三个字符abc为例来分析一下求字符串排列的过程。
	1、 固定第一个字符a，求后面两个字符bc的排列(bc,cb)。当两个字符bc的排列求好之后，我们把第一个字符a和后面的b交换，得到bac，
	2、 固定第一个字符b，求后面两个字符ac的排列(ac,ca)。
	3、 固定第一个字符c, 求后面两个字符ab的排列(ab,ba)。
	    记住前面我们已经把原先的第一个字符a和后面的b做了交换，
		A:为了保证这次c仍然是和原先处在第一位置的a交换，我们在拿c和第一个字符交换之前，先要把b和a交换回来。
		B:在交换b和a之后，再拿c和处在第一位置的a进行交换，得到cba。我们再次固定第一个字符c，求后面两个字符b、a的排列。

	既然我们已经知道怎么求三个字符的排列，那么固定第一个字符之后求后面两个字符的排列，就是典型的递归思路了。

 */
#include <stdio.h>
#include <time.h>
#include <Windows.h>
#include <stdlib.h>



void swap(char* s, int i, int j)
{
	/*字符交换*/
	char temp; // 创建一个char型字符变量
	temp = s[j];
	s[j] = s[i];
	s[i] = temp;
	// return ; 
}

void permutate(char *s, const int beg, int end)
{
	/*begingging: beg =0 ，end=strlen(s)-1; if end!= this worong*/
	int i;
	if (beg == end)
	{
		printf("%s\n", s);
	}
	else {

		for (i = beg; i < end; i++)
			//不能是i=beg+1 
		{
			swap(s, beg, i);// 字符串交换
			permutate(s, beg + 1, end);// 再次调用：递归
			swap(s, beg, i);
		}
	}
}


int main()
{
	char s[] = "abc";
	permutate(s, 0, strlen(s));
	system("pause");
	return 0;
}
 
