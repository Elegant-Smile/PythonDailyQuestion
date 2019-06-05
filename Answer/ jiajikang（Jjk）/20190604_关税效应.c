/*
 * @Author: jjk
 * @Date: 2019-05-31 16:42:45
 * @Last Modified by: jjk
 * @Last Modified time: 2019-05-31 19:04:45
 * @encoding：gbk
 * @程序功能：
        #关税效应#
		已知A国对进口棉花要征收关税，棉花价格为100元，原棉(纯棉)价格为60元，有如下的方案：
		1.对棉花征收10%的关税，对原棉征收10%的关税。
		2.对棉花征收10%的关税，对原棉征收20%的关税。
		3.对棉花征收20%的关税，对原棉征收10%的关税。
		设计一个函数来表达三个方案的有效保护率。
		有效保护率＝（国内加工增长值－国外加工增长值）/国外加工增长值×100%


 */


#include<stdlib.h>
#include <stdlib.h>
#include <string.h>
#include "linknode.h"


void main()
{
	// 已知A国对进口棉花要征收关税，棉花价格为100元，原棉(纯棉)价格为60元，有如下的方案：
	// 1.对棉花征收10%的关税，对原棉征收10%的关税。
	double a = 100.0,b = 60.0;
	double ERP = 0.0;
	double gn;
	double gw;
	
	// ERP＝（V'－V）/V×100%
	printf("请输入国内加工增值：");
	scanf("%lf",&gn);
	printf("请输入国内加工增值：");
	scanf("%lf",&gw);

	// VV = 100* (1+10%) - 60*(1+5%)
	ERP = (a*(1 + gn) - b*(1+gw)) / (a - b);
	printf("有效保护率：%.2lf\n",ERP);

	system("pause");







}