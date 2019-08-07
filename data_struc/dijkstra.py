# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:16:18 2019

@author: yifeng
"""

## 迪杰斯特拉最短路
'''
input: 
    graph:以字典形式存储节点和权重信息
    
关键中间量：costs:存储经过当前节点到其邻居邻居节点的最小开销

'''

def find_lowest_cost_node(costs,processed):
    cost = float('inf')
    node = None
    for n in costs.keys():
        if (costs[n]<cost) and (n not in processed):
            cost = costs[n]
            node = n
    return node

            
def dijkstra(graph,start,end):
    
    costs = {}
    for i in list('abcdef'):
        costs[i] = float('inf')
    costs[start] = 0
    
    processed = [] # 处理过的节点
    
    parents = {}
    
    node = find_lowest_cost_node(costs,processed)  # 在未处理节点中找到最低开销的节点
    while True:  #循环在所有节点都被处理后结束
        cost = costs[node] #记录起点到node的开销
        neighbors = graph[node] #node的邻居节点
        for n in neighbors.keys(): #遍历当前节点的所有邻居节点
            new_cost = cost+neighbors[n] #新的开销：经过当前节点到邻居节点n的开销
            if new_cost<costs[n]: #如果经当前节点往邻居更近，
                costs[n] = new_cost #更新该邻居的开销
                parents[n] = node #同时将该邻居的父节点设置为当前节点
        processed.append(node) #将当前节点标记为处理过
        node = find_lowest_cost_node(costs,processed) # 找出接下来要处理的节点，并循环
        if node == end: # 下一个要处理的节点是终点，结束循环
            break
    return costs,parents
    
def print_route(parents,start,end):
    ans = []
    while True:
        if end in parents.keys():
            tmp = parents[end]
            ans.append(end)
            end = tmp
        else:
            break
    ans.append(end)
    print(ans[::-1])
    
if __name__ == '__main__':
    graph = {'a':{'b':2,'c':5},
         'b':{'d':7,'c':8},
         'c':{'e':4,'d':2},
         'd':{'f':1},
         'e':{'d':6,'f':3}}
    start = 'a'
    end = 'f'
    c,p = dijkstra(graph,start,end)
    print_route(p,start,end)
    
