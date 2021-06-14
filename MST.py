# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:09:41 2021

@author: Amlan Ghosh
"""

'''Prim's Algo'''
'''Example: Complete graph with 0-1 edges'''
N,M = map(int, input().split())
G = {}
for i in range(N):
    G[i] = {}
    for j in range(N):
        G[i][j] = 0
for i in range(M):
    u,v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1
mst = [0]
mst_t = [i for i in range(1,N)]
weight = 0
for _ in range(N-1):
    
    big = {}
    big_list = {}
    
    for i in mst: #searching the minimum edge for each node in mst
        m = G[i][mst_t[0]]
        for j in mst_t:
            if G[i][j] <= m:
                m = G[i][j]
                ind = j
        big[ind] = m
        big_list[i] = ind
    
    q = big_list[0]
    f = big[big_list[0]]
    for i in big_list: #searching the minimum among the minimum edge obtained from the nodes in mst
        if big[big_list[i]] <= f:
            f = big[big_list[i]]
            q = big_list[i]
            track = i
            
    mst.append(q)
    mst_t.remove(q)
    weight += G[track][q]
print (weight)
