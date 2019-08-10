# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:14:55 2019

@author: yifeng
"""

'''
链接：https://www.nowcoder.com/questionTerminal/f0ed5df0a373456a8c9b5a64e6374961?answerType=1&f=discussion
来源：牛客网

为了不断优化推荐效果，今日头条每天要存储和处理海量数据。假设有这样一种场景：我们对用户按照它们的
注册时间先后来标号，对于一类文章，每个用户都有不同的喜好值，我们会想知道某一段时间内注册的用户
（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。因为一些特殊的原因，不会出现一个查询的
用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。



输入描述:
输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度 
第3行为一个正整数q代表查询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，
即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。 数据范围n <= 300000,q<=300000 
k是整型


输出描述:
输出：一共q行，每行一个整数代表喜好值为k的用户的个数
'''

import bisect

n = int(input())
arr = list(map(int,input().strip().split()))
like_index =  {} 
#遍历arr喜好度，keys=喜好度,values=喜好度对应的index list
for i in range(n):
    if arr[i] not in like_index.keys():
        like_index[arr[i]] = []
    like_index[arr[i]].append(i+1)
   
q = int(input())
for i in range(q):
    [l,r,k] = list(map(int,input().strip().split()))
    # 若查询k在like_index keys中
    if k in like_index.keys():
        tmp = like_index[k]
        l = bisect.bisect_left(tmp,l) # 返回index使得tmp的前index的值都小于l
        r = bisect.bisect_right(tmp,r) # tmp得是递增的
        ans = r-l
        print(ans)
    else:
        print(0)

        
        