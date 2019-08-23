# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:49:16 2019

@author: yifeng
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:04:40 2019

@author: yifeng
"""

arr = [8,1,2,3,5,6,'B','A']
for i in range(len(arr)):
    arr[i] = str(arr[i])

def func(arr):
    res = []
    for i in range(len(arr)):
        if i==0:
            continue
        if arr[i]=='A':
            res.extend(['12','34'])
                    
        elif arr[i]=='B':
            res.extend(['AB','CD'])
        else:
            res.append(arr[i].upper())
    return res

def func2(arr):
    res = []
    for i in range(len(arr)):
        if 'A' in arr[i]:
            for j in range(len(arr[i])):
                if arr[i][j]=='A':
    #                tmp = arr[i][:j]+'12 34'+arr[i][j+1:]
    #                tmp = tmp.split(' ')
                    if arr[i][:j] != '':
                        res.append(arr[i][:j])
                    
                    res.extend(['12','34'])
                    if arr[i][j+1:] != '':
                        res.append(arr[i][j+1:])
                
        elif 'B' in arr[i]:
            for j in range(len(arr[i])):
                if arr[i][j]=='B':
                    if arr[i][:j] != '':
                        res.append(arr[i][:j])
                    res.extend(['AB','CD'])
                    if arr[i][j+1:] != '':
                        res.append(arr[i][j+1:])
        else:
            res.append(arr[i].upper())
    return res

res = func(arr)
while True:
    res = func2(res)
    if ('A' not in res) and ('B' not in res):
        break

length = len(res)
res = [str(length+1)]+res
print(' '.join(res))
