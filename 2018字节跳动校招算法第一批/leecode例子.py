# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:52:48 2019

@author: yifeng
"""

# 题目详解参考
# https://blog.csdn.net/weixin_42001089/article/details/84203651

class Solution:
    def largestRectangleArea(self,heights):
        heights.append(0)
        stack = []
        i = 0
        result = 0
        while i<len(heights):
            if not stack or heights[stack[-1]]<heights[i]:
                stack.append(i)
                i += 1      
            else:
                num = stack.pop(-1)
                result = max(result,heights[num]*((i-num) if stack else i))
            
        return result
    
t = [2,1,5,6,2,3]
so = Solution()
so.largestRectangleArea(t)
