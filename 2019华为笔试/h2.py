# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:37:59 2019

@author: yifeng
"""

def isZhishu(num):
    if num>2:
        for i in range(2,num//2+1):
            if (num % i) == 0:
                return False
                break
        return True
    return True

def get_num(num):
    num = str(num)
    a10 = num[-2]
    a1 = num[-1]
    return a10,a1


[low,high] = list(map(int,input().strip().split()))
res = []
for i in range(low,high):
    if isZhishu(i):
        res.append(i)
ans1 = []
ans10 = []
for num in res:
    if num < 10:
        ans1.append(num)
        ans10.append(0)
    else:
        a10,a1 = get_num(num)
        ans1.append(a1)
        ans10.append(a10)
ans1 = [int(x) for x in ans1]
ans10 = [int(x) for x in ans10]
    
result = min(sum(ans1),sum(ans10))
print(result)
        