# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:32:09 2019

@author: yifeng
"""
'''
字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字
母进行交换。询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？

链接：https://www.nowcoder.com/questionTerminal/8da0ea4b4853464795f5c32634a1b06f?f=discussion
来源：牛客网

输入描述:
第一行为一个字符串S与一个非负整数m。(1 <= |S| <= 1000, 1 <= m <= 1000000)


输出描述:
一个非负整数，表示操作之后，连续最长的相同字母数量。
示例1
输入
abcbaa 2
输出
2
说明
使2个字母a连续出现，至少需要3次操作。即把第1个位置上的a移动到第4个位置。
所以在至多操作2次的情况下，最多只能使2个b或2个a连续出现。
'''
    

#====================================
[string,m] = list(input().strip().split())
m = int(m)
n = len(string)
# char_v 
char_v = {} #keys=字母，values=[字母所对应的index]
for i in range(n):
    if string[i] not in char_v.keys():
        char_v[string[i]] = []
    char_v[string[i]].append(i)
    
#dp[i][j]表示v中第i个位置到第j个都移动到一起，需要的步数
#对任意一个字母
ans = 0
for i in char_v.keys():
    v = char_v[i]
    k = len(v)
    dp = [[0]*k for _ in range(k)]
    #若i+1 == j,即v的两个index相邻元素，移动到一起需v[j]-v[i]-1步
    for j in range(k-1):
        dp[j][j+1] = v[j+1]-v[j]-1
    #间隔为t(2<=t<n),dp[i][j]=dp[i+1][j-1]+v[j]-v[i]-1-(j-1-(i+1)+1)
    for interval in range(2,k):
        for j in range(k-interval):
            left,right = j,j+interval
            dp[left][right] = dp[left+1][right-1]+v[right]-v[left]-1-(right-1-(left+1)+1)
            
    for j1 in range(k):
        for j2 in range(j1,k):
            if dp[j1][j2]<=m:
                ans = max(ans,j2-j1+1)
print(ans)
    

        