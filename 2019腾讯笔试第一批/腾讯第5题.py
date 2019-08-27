# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:54:29 2019

@author: yifeng
"""
import numpy as np

class Solution:
    def __init__(self):
        self.max_sum = 0
        self.result = None
        
    def maze(self,arr):
        

        def isValid(x,y):
            if 0<=x<n and 0<=y<3:
                return True
            else:
                return False
        def back(x,y,sum_,flag):
            if x==n-1:
                if self.max_sum<sum_:
                    self.max_sum = sum_
#                    self.result = path
                return 
            walk_dir = [[1,-1],[1,0],[1,1]]
            for direction in walk_dir:
                next_x,next_y = x+direction[0], y+direction[1]
                if isValid(next_x,next_y):
                    num = arr[next_x][next_y]
                    flag_next = flag
                    if num==0:
                        flag_next = flag*(-1)
#                    path_next = path.copy()
#                    path_next.append([next_x,next_y])
                    sum_next = sum_ + num*flag_next
                    back(next_x,next_y,sum_next,flag_next)
                    
        arr.insert(0,[100,100,100])   
#        self.result = None
        n = len(arr)
        back(0,1,0,1)
        return self.max_sum
      
n = 10
np.random.seed(27)
arr = np.random.randint(-10,10,size=(n,3))
arr = arr.tolist()


so = Solution()
res = so.maze(arr)
print('{}:{}'.format(n,res))
