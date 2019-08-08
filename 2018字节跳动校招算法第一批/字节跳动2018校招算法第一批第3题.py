# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:40:42 2019

@author: yifeng
"""

'''
产品经理(PM)有很多好的idea，而这些idea需要程序员实现。现在有N个PM，在某个时间会想出一个 idea，
每个 idea 有提出时间、所需时间和优先等级。对于一个PM来说，最想实现的idea首先考虑优先等级高的，
相同的情况下优先所需时间最小的，还相同的情况下选择最早想出的，没有PM会在同一时刻提出两个 idea。

同时有M个程序员，每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的一个idea,
然后从中挑选出所需时间最小的一个idea独立实现，如果所需时间相同则选择PM序号最小的。
直到完成了idea才会重复上述操作。如果有多个同时处于空闲状态的程序员，那么他们会依次
进行查看idea的操作。

求每个idea实现的时间。

输入第一行三个数N、M、P，分别表示有N个PM，M个程序员，P个idea。随后有P行，每行有4个数字，
分别是PM序号、提出时间、优先等级和所需时间。输出P行，分别表示每个idea实现的时间点。
'''

#=================================================================
# 解题思路
# time_ideas,key=time,values=[#0:pm序号,1:提出时间,2:优先等级,3:所需时间,4:任务序号]
# zhixing_ideas:正在执行的ideas，finish_ideas:完成的ideas,
# pm_idea_dict:key=pm,values=ideas,时刻t，pm提出的尚未被执行的ideas
# while True
#   对正在执行的idea,所需时间-1，若执行一步后完成，从执行idea中删除，n_chengxuyuan+1，加至finish_idea
#   若 正在执行idea为空， 且n_diea==0，结束
#   当前时刻，pm提出来的idea,加到pm_idea_dict
#   while 还有程序员  and 现有任务>0:
#       pm_want_idea,pm最想落实的idea
#       if pm_want_idea 不为空:
#           程序员执行pm_want_idea中最优先的idea,
#           pm_idea_dict[idea[0]].remove(idea),
#           将idea从pm_idea_dict删除，加到xingzhi_idea中
#           n_idea -= 1, n_weizhixing_idea -= 1, n_chengxuyuan -= 1
    
def find_finish_time(time_ideas,n_chengxuyuan,n_idea):
    time = 0
    zhixing_ideas = []
    finish_ideas = []
    pm_idea_dict = {}
    n_weizhixing_idea = 0
    
    while True:
        time += 1
        # 对正在执行idea,所需时间-1
        if zhixing_ideas: # zhixing_ideas != []
            deleted_ideas = []
            for i in zhixing_ideas:
                i[3] -= 1
                if i[3] == 0:
                    deleted_ideas.append(i)
            for i in deleted_ideas:
                zhixing_ideas.remove(i)
                n_chengxuyuan += 1
                i.append(time) # 5:执行完成时间
                finish_ideas.append(i)
                
        # 若无正在执行idea 且 剩余idea数为0， 结束循环
        if not zhixing_ideas and n_idea==0:
            break
        # 时刻t，更新pm提出的idea
        for t in time_ideas.keys():
            if t==time:
                for i in time_ideas[t]:
                    if i[0] not in pm_idea_dict:
                        pm_idea_dict[i[0]] = []
                    pm_idea_dict[i[0]].append(i)
                    n_weizhixing_idea += 1
                break
        # 若还有程序员 且 还有现有任务，
        # 找出每个pm最想落实的idea,判断实现哪个idea,加入执行队列，并从未执行队列中删除
        while n_chengxuyuan > 0 and n_weizhixing_idea > 0:
            pm_want_idea = []
            for i in pm_idea_dict.keys():
                if pm_idea_dict[i] != []:
                    pm_want_idea.append(min(pm_idea_dict[i], \
                                            key=lambda x:(-x[2],x[3],x[1]))) 
            if pm_want_idea != []:
                want_idea = min(pm_want_idea, key=lambda x:(x[3],x[0]))
                zhixing_ideas.append(want_idea)
                pm_idea_dict[want_idea[0]].remove(want_idea)
                n_idea -= 1
                n_weizhixing_idea -= 1
                n_chengxuyuan -= 1
                
    finish_ideas = sorted(finish_ideas,key=lambda x:x[4])
    for i in finish_ideas:
        print(i[5])

[n_pm,n_chengxuyuan,n_idea] = list(map(int,input().strip().split()))
time_ideas = {}
for i in range(n_idea):
    #0:pm序号,1:提出时间,2:优先等级,3:所需时间,4:任务序号
    idea = list(map(int,input().strip().split()))
    idea.append(i)
    if idea[1] not in time_ideas.keys():
        time_ideas[idea[1]] = []
    time_ideas[idea[1]].append(idea)
            
#=====================================================
# """
# 解题思路：
# time_ideas字典
# while Ture:
#     time += 1
#     更新执行队列任务剩余时间
#     删除执行完的idea，更新程序员数量，记录完成时间
#     if 执行队列为空 and 所有idea = 0:
#         break
#     更新每个pm现有的idea
#     pm_ideas字典
#     while 还有程序员 并且 现有任务数 > 0：
#         找出每个pm现有的最想实现的idea
#         判断实现哪个idea，并加入执行队列,并从待执行队列中删除
#         任务数p -= 1
#         程序员数m -= 1
#
# """

            