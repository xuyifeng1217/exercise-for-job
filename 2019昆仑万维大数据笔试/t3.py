# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:48:05 2019

@author: S_mingtong
"""

num = int(input())

def isZhishu(num):
    if num==2:
        return True
    
    for i in range(3,num//2+1):
        if num%i==0:
            return False
    else:
        return True
def get_zhishus(num):
    res = []
    for i in range(2,num+1):
        if isZhishu(i):
            res.append(i)
    return res

zhishu_list = get_zhishus(num)
last = num
ans = []
while last != 1:
    for i in zhishu_list:
        if last%i == 0:
            ans.append(i)
            break
    last = last/i
ans = sorted(ans)
res = []
if len(ans)==1:
    print(str(ans[0]))
else:
    for i in ans:
        res.append(str(i))
        
res = '*'.join(res)
print(res)
        