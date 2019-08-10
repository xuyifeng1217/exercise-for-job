# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:21:42 2019

@author: yifeng
"""

'''
链接：https://www.nowcoder.com/questionTerminal/f73e780af8f0425b98dfaf7cdd9389dc?f=discussion
来源：牛客网

作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，
要么涂了若干种颜色。为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种
颜色（不包含无色），在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。
手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色
分别有哪些。请你判断该手串上有多少种颜色不符合要求。即询问有多少种颜色在任意连续m个
串珠中出现了至少两次。


输入描述:
第一行输入n，m，c三个数，用空格隔开。(1 <= n <= 10000, 1 <= m <= 1000, 1 <= c <= 50)
 接下来n行每行的第一个数num_i(0 <= num_i <= c)表示第i颗珠子有多少种颜色。接下来依次读入
 num_i个数字，每个数字x表示第i颗柱子上包含第x种颜色(1 <= x <= c)
 
 输出描述:
一个非负整数，表示该手链上有多少种颜色不符需求。

例子：
    输入
    5 2 3
    3 1 2 3
    0
    2 2 3
    1 2
    1 3
    输出
    2

说明：

第一种颜色出现在第1颗串珠，与规则无冲突。
第二种颜色分别出现在第 1，3，4颗串珠，第3颗与第4颗串珠相邻，所以不合要求。
第三种颜色分别出现在第1，3，5颗串珠，第5颗串珠的下一个是第1颗，所以不合要求。
总计有2种颜色的分布是有问题的。 
这里第2颗串珠是透明的。
'''
#=====================================================
[n,m,c] = list(map(int,input().strip().split()))
color_index = {} #keys=color, values=颜色对应的index
for i in range(n):
    zhuzi = list(map(int,input().strip().split()))
    for j in range(1,len(zhuzi)):
        if zhuzi[j] not in color_index.keys():
            color_index[zhuzi[j]] = []
        color_index[zhuzi[j]].append(i)
count = 0
for i in color_index.keys():
    tmp = color_index[i]
    for j in range(1,len(tmp)):
        if tmp[j]-tmp[j-1]<m or (n+tmp[0]-tmp[j])<m:
            count += 1
            break
print(count)
