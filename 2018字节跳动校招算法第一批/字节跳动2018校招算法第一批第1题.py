# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:01:18 2019

@author: yifeng
"""

##字节跳动2018算法第一批第一题
'''链接：https://www.nowcoder.com/questionTerminal/f652bf7904bf4905804fa3bc347fdd2a
来源：牛客网

P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内
（横纵坐标都大于x），则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标
都不重复, 坐标轴范围在[0, 1e9) 内）'''

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

#============第2种写法=================
# 将点集对y值进行降序排序，遍历，若该点的x值比上一个‘最大点’的x值大，则记录该x值。
# ‘最大点’就是其右上方无点，
def main():
    n = int(input())
    p = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        p.append(tmp)
        
    p = sorted(p,key=lambda x:x[1], reverse=True) #根据y值进行降序排序
    t = -1
    for i in p:#遍历p
        if i[0]>t:
            print('{} {}'.format(i[0],i[1]))
            t = i[1] # 记录上一个点的y value
main()
