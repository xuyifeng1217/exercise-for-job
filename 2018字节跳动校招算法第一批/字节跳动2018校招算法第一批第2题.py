# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:18:06 2019

@author: yifeng
"""

# 字节跳动2018校招算法第一批第2题
'''
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：

区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值: 
[6] = 6 * 6 = 36;

[2] = 2 * 2 = 4;

[1] = 1 * 1 = 1;

[6,2] = 2 * 8 = 16;

[2,1] = 1 * 3 = 3;

[6, 2, 1] = 1 * 9 = 9;

 
从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。

区间内的所有数字都在[0, 100]的范围内;
'''

##===========方法一==牛逼的解法===============

def main():
    n = int(input()) 
    arr = list(map(int,input().split()))
    stack = []  # 栈
    arr.append(0) #元素添加0
    result = 0 # 结果
    i = 0  #index
    presum = [] # 本轮第一个元素进栈时，presum.append上一轮元素出栈的和，之后都append 0
    tempsum = 0 # 本轮的累加
    while i<len(arr):
        if not stack or arr[i]>=stack[-1]: # 若栈为空，或arr[i]大于最后一个进栈的元素
            presum.append(tempsum) # 本轮第一个元素进栈时，presum.append上一轮元素出栈的和，之后都append 0
            tempsum = 0 
            stack.append(arr[i])
            i += 1
        else:
            temp = stack.pop(-1) # 出栈
            tempsum = tempsum + (temp+presum.pop(-1)) # 本轮的累加
            result = max(result,tempsum*temp)
    print(result)

main()

#====================方法二===================================================
# 最初的解法，复杂度过高
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


