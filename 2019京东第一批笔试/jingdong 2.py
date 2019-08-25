# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:27:35 2019

@author: yifeng
"""

class Solution:
    def __init__(self):
#        self.total = total
        self.flag = False
#        self.result = None
    def maze(self):
        def get_matrix(m,n):
#            arr = ['...','###','#S#']
            arr = []
            for i in range(m):
                arr.append(input())
#            arr = ['S#','#.']
            mat = []
            for i in arr:
                tmp = []
                for j in i:
                    tmp.append(j)
                mat.append(tmp*3)
            for i in range(3):
                for j in range(m):
                    mat.append(mat[j])
            return mat
        
        
        def get_start(mat,m,n):
            for i in range(m,2*m):
                for j in range(n,2*n):
                    if mat[i][j]=='S':
                        return [i,j]
        
        
        def isValid(mat,x,y):
            if 0<=x<3*m and 0<=y<3*n and (mat[x][y]=='.' or mat[x][y]=='S'):
                return True
            else:
                return False
        
        def back(mat,x,y):
            if x==0 or x==3*m-1 or y==0 or y==3*n-1:
                self.flag = True

                return 
            walk_direction = [[1,0],[0,1],[-1,0],[0,-1]]
            for direction in walk_direction:
                next_x, next_y = x+direction[0], y+direction[1]
                if isValid(mat,next_x,next_y):
                    mat[next_x][next_y] = '#'
#                    self.result.append([next_x,next_y])
                    back(mat,next_x,next_y)
                    if self.flag:
                        return 
                    mat[next_x][next_y] = '.'
#                    self.result.remove([next_x,next_y])

        m,n = list(map(int,input().strip().split()))
#        self.result = []
        mat = get_matrix(m,n)
        start = get_start(mat,m,n)
        back(mat,start[0],start[1])
        return self.flag
            
total = int(input())
so = Solution()
for i in range(total):
    res = so.maze()
    print(res)