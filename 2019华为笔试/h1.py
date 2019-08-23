# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:04:40 2019

@author: yifeng
"""

arr = input().strip().split()
res = []
for i in range(len(arr)):
    if i==0:
        continue
    if 'A' in arr[i]:
        for j in range(len(arr[i])):
            if arr[i][j]=='A':
                tmp = arr[i][:j]+'12 34'+arr[i][j+1:]
                tmp = tmp.split(' ')
                res.extend(tmp)
    elif 'B' in arr[i]:
        for j in range(len(arr[i])):
            if arr[i][j]=='B':
                tmp = arr[i][:j]+'AB CD'+arr[i][j+1:]
                tmp = tmp.split(' ')
                res.extend(tmp)
    else:
        res.append(arr[i].upper())
length = len(res)
res = [str(length+1)]+res
print(' '.join(res))


a = '1A'
'A' in a

for i in a:
    if i=='A'
        
a.replace('A',['12','34'])
