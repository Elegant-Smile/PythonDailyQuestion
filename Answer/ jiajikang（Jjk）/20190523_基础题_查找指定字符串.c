/*
 * @Author: jjk
 * @Date: 2019-05-23 15:12:18
 * @Last Modified by: jjk
 * @Last Modified time: 2019-05-23 15:43:33
 * 程序功能：
 *         基础题：
 *               手机品牌存放在一个列表中 brandlist =['华为','苹果','一加','OPPO','小米']，
 *               请实现以下功能：随机选择一个手机品牌屏幕输出
 */
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{

    char name1[][10] = {"华为", "苹果", "一加", "OPPO", "小米"}; // 创建二位数组
    char *name2[] = {"华为", "苹果", "一加", "OPPO", "小米"};// 创世一维数组
    printf("--------二维字符串数组的存储方式-------\n");
    for (int i = 0; i <= 4; i++)
    {
        printf("name[%d] = \"%s\"\t", i, name1[i]);
        printf("所占地址：%p\n", name1[i]);
    }

    printf("--------一维指针数组的存储方式--------\n");
    for (int i = 0; i <= 4; i++)
    {
        if (strcmp(argv[1],name2[i])==0)
        {
            printf("name[%d] = %s\t", i, name2[i]);
        }

        // printf("name[%d] = \"%s\"\t", i, name2[i]);
        // printf("所占地址：%p\n", name2[i]);
    }
    
    // printf("argv=%s\n", argv[1]);

    return 0;
}