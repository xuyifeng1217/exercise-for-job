# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:49:59 2019

@author: S_mingtong
"""

import sys
arr = eval(input())
points = eval(input())

def isValid(x,y):
# 确定（x,y）是否有效
    if 0<=x<4 and 0<=y<4:
        return True
    else:
        return False

walk_direction = [[1,0],[0,1],[-1,0],[0,-1]]

for p in points:
    for direction in walk_direction:
        next_x,next_y = p[0]-1+direction[0], p[1]-1+direction[1]
        if isValid(next_x,next_y):
            arr[next_x][next_y] = 1-arr[next_x][next_y]
arr = str(arr)
sys.stdout.write(arr)