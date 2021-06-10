# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:32:10 2021

@author: Amlan Ghosh
"""

'''Djikstra's Shortest Path'''
def djikstra(dist_mat, nodes): #dist_mat: dictionary {node1: {node2: 2, node3: 4}, node2: {node1: 2}}
    opt_dist = [10**5]*nodes
    opt_dist[0] = 0
    not_visited = list(i for i in range(25))
    for i in range(nodes):
        not_visited.sort(key = lambda x: opt_dist[x])
        node = not_visited[0]
        for neighbour in dist_mat[node]:
            opt_dist[neighbour] = min(opt_dist[neighbour], opt_dist[node] + dist_mat[node][neighbour])
        del not_visited[0]
    print (opt_dist)    