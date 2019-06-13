#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Abner Han 
# time:2019/6/13
"""
    手机品牌存放在一个列表中 brandlist = ['华为','苹果','一加','OPPO','小米']，
    请实现以下功能：随机选择一个手机品牌屏幕输出
"""

import random

brandlist = ['华为','苹果','一加','OPPO','小米']
i = random.randint(0,5)
print(brandlist[i])
