# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:35:35 2019

@author: yifeng
"""
# 腾讯第二题
class Solution:
    def __init__(self):
        self.result = None
        self.flag = None
        
    def maze(self,board):
        def isValid(board,x,y):
            if 0<=x<m and 0<=y<n and board[x][y]>0:
                return True
            else:
                return False
        
        def back(board,path,x,y):
            if x==m-1 and y==n-1  and board[x][y]==0:
                self.flag = True
                self.result.append(path)
                return 
            walk_dir = [[1,0],[0,1],[-1,0],[0,-1]]
            for direction in walk_dir:
                next_x = x + direction[0]
                next_y = y + direction[1]
                if isValid(board,next_x,next_y):
                    board[next_x][next_y] -= 1
                    path_copy = path.copy()
                    path_copy.append([next_x,next_y])
                    back(board,path_copy,next_x,next_y)
#                    if not self.flag:
                    board[next_x][next_y] += 1
        m = len(board)
        n = len(board[0])
        self.flag = False
        self.result = []
#        end = [3,3]
        for i in range(m):
            for j in range(n):
                num = board[i][j]
                if num=='X':
                    board[i][j] = 1
                elif num=='.':
                    board[i][j] = 2
        path = []
        path.append([0,0])
        board[0][0] -= 1
#        start = [0,0]
        back(board,path,0,0)
        return self.result,self.flag

board = [['X','X','.'],['X','X','.']]    
so = Solution()
so.maze(board)        