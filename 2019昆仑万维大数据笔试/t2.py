# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:22:39 2019

@author: S_mingtong
"""

n = int(input())
def jump(n):
    if n<=2:
        return n
    
    dp = [1]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = sum(dp[:i])
    return dp[-1]

ans = jump(n)
print(ans)