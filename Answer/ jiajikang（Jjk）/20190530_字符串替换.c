/*
 * @Author: jjk
 * @Date: 2019-05-30 13:14:46
 * @Last Modified by: jjk
 * @Last Modified time: 2019-05-30 15:06:02
 * 提高题：
   请实现一个函数，将一个字符串中的每个空格替换成“%20”。
   例如，当字符串为We Are Happy，则经过替换之后的字符串为We%20Are%20Happy。
 */

#include <stdio.h>
#include <string.h>

/* 功  能：将str字符串中的oldstr字符串替换为newstr字符串
 * 参  数：str：操作目标 oldstr：被替换者 newstr：替换者
 * 返回值：返回替换之后的字符串
 */
char *strrpc(char *str, char *oldstr, char *newstr)
{
    char bstr[strlen(str)]; //转换缓冲区
    memset(bstr, 0, sizeof(bstr));

    for (int i = 0; i < strlen(str); i++) // 遍历原字符串长度
    {
        if (!strncmp(str + i, oldstr, strlen(oldstr))) // oldstr:查找要替换的字符串
        // 比较两个字符串，相同返回0，若s1大于s2，则返回大于0的值；若s1小于s2，则返回小于0的值。
        {                         //查找目标字符串
            strcat(bstr, newstr); // newstr追加到bstr后面
            i += strlen(oldstr) - 1;
        }
        else
        {
            strncat(bstr, str + i, 1); //保存一字节进缓冲区
        }
    }

    strcpy(str, bstr); // bstr复制到str中
    return str;
}

int main(void)
{

    char str[] = "We Are Happy";
    printf("origin：%s", str); // 替换前

    strrpc(str, " ", "%20");   // 调用函数
    printf("\nafter:%s", str); // 替换后
    return 0;
}