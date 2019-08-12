# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 19:43:48 2019

@author: yifeng
"""
##题目与leetcode的分发糖果类似

n = 4
year = [3,9,2,7]

ans = [100]*n
for i in range(1,n):
    if year[i]>year[i-1]:
        ans[i] = ans[i-1]+100
sum_ = ans[-1]
for i in range(n-2,-1,-1):
    if year[i]>year[i+1]:
        ans[i] = max(ans[i],ans[i-1]+100)
    sum_ += ans[i]
print(sum_)