# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:32:10 2021

@author: Amlan Ghosh
"""

'''Djikstra's Shortest Path'''
def djikstra(dist_mat, nodes): #dist_mat: dictionary {node1: {node2: 2, node3: 4}, node2: {node1: 2}}
    opt_dist = [10**5]*nodes
    opt_dist[0] = 0
    computed = [0]
    visited = [False]*nodes
    for i in computed:
        if visited[i] == False:
            for neighbour in dist_mat[i]:
                opt_dist[neighbour] = min(opt_dist[neighbour], opt_dist[i] + dist_mat[i][neighbour])
                if visited[neighbour] == False:
                    computed.append(neighbour)
            visited[i] = True
    print (opt_dist)    