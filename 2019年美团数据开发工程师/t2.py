# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:14:33 2019

@author: S_mingtong
"""
import sys

line = list(map(int,input().strip().split()))
month = line[0]
year = line[1]
j_1 = year%4
j_2 = year%100
j_3 = year%400

big_month = set([1,3,5,7,8,10,12])
small_month = set([4,6,9,11])


if month in big_month:
    days = 31
elif month in small_month:
    days = 30
else:
    if (j_3==0) or (j_1==0 and j_2 != 0):
        days = 29
    else:
        days = 28
sys.stdout.write(str(days))