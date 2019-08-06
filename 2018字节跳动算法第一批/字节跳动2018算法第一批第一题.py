# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:01:18 2019

@author: yifeng
"""

##字节跳动2018算法第一批第一题

import sys

def readline(n):
    l = []
    for _ in range(n):
        line = sys.stdin.readline().strip().split()
        line = list(map(int,line))
        l.append(line)
    return l
def get_max_points(l):
    sets = sorted(l,key=lambda x:x[0],reverse=True)
    p = sets[0]
    for point in sets[1:]:
        if point[1]>p[1]:
            p = point
        else:
            sets.remove(point)
    return sets
def main():
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    a = int(n/2)
    nn = [a,n-a]
    ans = []
    for i in nn:
        points = readline(i)
        sets = get_max_points(points)
        ans.extend(sets)
    ans = get_max_points(ans)
    ans.sort(key=lambda x:x[0])
    for i in ans:
        print(i[0],i[1])
main()

l = [[1, 2],
[5, 3],
[4, 6],
[7, 5],
[9, 0]]
ll = get_max_points(l)
