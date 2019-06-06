/*


请实现一个函数用来匹配包括.和' '的正则表达式。
模式中的字符 '.' 表示任意一个字符，而 ' ' 表示它前面的字符可以出现任意次(包含0次)。
在本题中，匹配是指字符串的所有字符匹配整个模式。 
例如，字符串"aaa"与模式"a.a"和"ab ac a"匹配，但是与"aa.a"和"ab*a"均不匹配。

思路解析：
       1、两个字符串都为空，返回true
	   2、当第一个字符串不为空，第二个为空，返回false
	      【因为这样，就无法匹配成功了,而如果第一个字符串空了，第二个字符串非空，还是可能匹配成功的，
	        比如第二个字符串是“a*a*a*a*”,由于‘*’之前的元素可以出现0次，所以有可能匹配成功】
	   3、之后就开始匹配第一个字符，这里有两种可能：匹配成功或匹配失败。但考虑到pattern下一个字符可能是‘*’， 这里我们分两种情况讨论：
	      pattern下一个字符为‘*’或不为‘*’：
          3.1>pattern下一个字符不为‘*’：这种情况比较简单，直接匹配当前字符。如果匹配成功，继续匹配下一个；如果匹配失败，直接返回false。注意这里的
            “匹配成功”，除了两个字符相同的情况外，还有一种情况，就是pattern的
              当前字符为‘.’,同时str的当前字符不为‘\0’。
          3.2>pattern下一个字符为‘*’时，稍微复杂一些，因为‘*’可以代表0个或多个。
               这里把这些情况都考虑到：
               a>当‘*’匹配0个字符时，str当前字符不变，pattern当前字符后移两位，
                跳过这个‘*’符号；
               b>当‘*’匹配1个或多个时，str当前字符移向下一个，pattern当前字符不变。（这里匹配1个或多个可以看成一种情况，因为：当匹配一个时，
                  由于str移到了下一个字符，而pattern字符不变，就回到了上边的情况a；当匹配多于一个字符时，相当于从str的下一个字符继续开始匹配）
 
  
*/

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>



//bool math(char *str,char *pattern) {
//
//	if (str==NULL || pattern == NULL)
//	{
//		return false;
//	}
//}



bool myMatch(char *str,char *pattern) {


	if (str == NULL || pattern == NULL)
	{
		return false;
	}


	if (*str=='\0'&& *pattern =='\0')
	{
		return true;
	}
	if (*str!='\0'&& *pattern=='\0')
	{
		return false;
	}
	 
	if (*(pattern + 1) == '*') {
		if (*str == *pattern || (*pattern == '.' && *str != '\0'))
			//myMatch(str,pattern+2):模式串未匹配
			//myMatch(str+1,pattern):模式串已经匹配成功，尝试匹配下一个字符串
			return myMatch(str + 1, pattern) || myMatch(str, pattern + 2);
		else
			return myMatch(str, pattern + 2);
	}

	if (*str == *pattern || (*pattern == '.' && *str != '\0'))
		return myMatch(str + 1, pattern + 1);
	return false;

}


void main() {
	
	char *s1 = "aaa";
	char* pattern1 = "ab*a*c*a";
	char* pattern2 = "a.a";
	char* pattern3 = "ab*a";
	char* pattern4 = "aa.a";
	char* pattern5 = "bbbba";
	char* pattern6 = ".*a*a";

	printf("%d\n", myMatch(s1, pattern1));
	printf("%d\n", myMatch(s1, pattern2));
	printf("%d\n", myMatch(s1, pattern3));












}
 