/*

20190617
提高题：
	求出任意非负整数区间中1出现的次数，比如，1~13中包含1的数字有1、10、11、12、13，1~13的整数中1出现的次数是6次。那100~1300的整数中1出现的次数是多少呢？

思路：
两种方法，一种是从1到n遍历，每次通过对10求余数判断整数的个位数字是不是1，大于10的除以10之后再判断。
           我们对每个数字都要做除法和求余运算以求出该数字中1出现的次数。
            如果输入数字n，n有O(logn)位，我们需要判断每一位是不是1，那么时间复杂度为O(n*logn)。
          
		  第二种方法是数学之美上面提出的方法，设定整数点（如1、10、100等等）作为位置点i（对应n的各位、十位、百位等等），
		   分别对每个数位上有多少包含1的点进行分析。

根据设定的整数位置，对n进行分割，分为两部分，高位n/i，低位n%i
当i表示百位，且百位对应的数>=2,如n=31456,i=100，则a=314,b=56，此时百位为1的次数有a/10+1=32（最高两位0~31），每一次都包含100个连续的点，
             即共有(a/10+1)*100个点的百位为1

当i表示百位，且百位对应的数为1，如n=31156,i=100，则a=311,b=56，此时百位对应的就是1，则共有a/10(最高两位0-30)次是包含100个连续点，
             当最高两位为31（即a=311），本次只对应局部点00~56，共b+1次，所有点加起来共有（a/10*100）+(b+1)，这些点百位对应为1

当i表示百位，且百位对应的数为0,如n=31056,i=100，则a=310,b=56，此时百位为1的次数有a/10=31（最高两位0~30）

综合以上三种情况，当百位对应0或>=2时，有(a+8)/10次包含所有100个点，还有当百位为1(a%10==1)，需要增加局部点b+1
             之所以补8，是因为当百位为0，则a/10==(a+8)/10，当百位>=2，补8会产生进位位，效果等同于(a/10+1)
 
*/


#include <stdio.h>
#include <time.h>
#include <string.h>
#include <Windows.h>


int NumberOf1Between1AndN_Solution1(int n)
{
	int count = 0;
	for (int i = 0; i <= n; ++i)
	{
		int temp = i;
		while (temp)
		{
			if (temp % 10 == 1) {
				++count;
			}

			temp =temp / 10;
		}
	}
	return count;
}
 

int NumberOf1Between1AndN_Solution(int n)
{
	int count = 0;
	long long i = 100;
	for (i = 1; i <= n; i *= 10)
	{
		//i表示当前分析的是哪一个数位
		int a = n / i, b = n % i;
		count = count + (a + 8) / 10 * i + (a % 10 == 1) * (b + 1);
	}
	return count;
}


void main() {
    
	printf("%d", NumberOf1Between1AndN_Solution1(13));

}

 


 


 