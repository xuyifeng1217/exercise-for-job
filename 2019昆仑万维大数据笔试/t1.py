# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:43:47 2019

@author: S_mingtong
"""

n = int(input())
ugly_num = [1,2,3,4,5]
mul = [2,3,5]
ans = set()
while len(ans)<n:
    tmp = []
    for i in range(len(ugly_num)):
        for j in range(len(mul)):
            num = ugly_num[i]*mul[j]
            tmp.append(num)
            while num<ugly_num[-1]:
                num = num*mul[j]
                tmp.append(num)

    ugly_num.extend(tmp)
    ans = set(ugly_num)

ans = sorted(list(ans))
print(ans[n-1])
#