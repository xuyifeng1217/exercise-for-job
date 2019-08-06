# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:18:06 2019

@author: yifeng
"""

# 字节跳动2018校招算法第一批第2题
import sys

def main():
    n = sys.stdin.readline().strip().split()
    n = int(n[0])
    arr = sys.stdin.readline().strip().split()
    arr = list(map(int,arr))
    max_m = (max(arr))**2 # 区间为1时
    min_n = min(arr) # 区间为n时
    max_n_sum = sum(arr)
    max_n = min_n*max_n_sum
    if max_m<max_n:
        max_m = max_n
    for i in range(2,n): #遍历不同长度的区间
        ar = arr[:i]
        ar_min = min(ar)
        ar_sum = sum(ar)
        ar_m = ar_min*ar_sum
        for j in range(i,n): #对区间末端的遍历
            ar_sum = ar_sum + arr[j] - arr[j-i]
            if ar_min==arr[j-i]:
                ar_min = min(arr[j-i+1:j+1])
            else:
                ar_min = min(ar_min,arr[j])
            ar_mul = ar_min*ar_sum
            if ar_m<ar_mul:
                ar_m = ar_mul
        if max_m<ar_m:
            max_m = ar_m
    print(max_m)
    
main()
    
