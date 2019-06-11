#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int FirstNotRepeatingChar(string str)
{
  int strSize = str.size();
  //处理错误输入
  if (strSize <= 0)
    return -1;
  //处理特殊输入
  if (strSize == 1)
    return 0;

  //使用vector做一个哈希表，记录每个字符出现的次数，全部初始化为0
  vector<int> hashTable(256, 0);
  //范围for循环对输入字符串进行第一次遍历，统计每一种字符出现的次数
  for (auto s : str)
  {
    hashTable[s]++;
  }

  //对输入字符串进行第二次遍历:
  for (int i = 0; i != strSize; i++)
  {
    if (hashTable[str[i]] == 1)
    {
      //cout <<  str[i] << endl;
      return i;
    }
  }

  return -1;
}



// 主函数
int main()
{
  cout << "Please enter a string:" << endl;
  string test;
  while (cin >> test)
  {
    cout << FirstNotRepeatingChar(test) << endl;
  }

  return 0;
}