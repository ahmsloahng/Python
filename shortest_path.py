# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:32:10 2021

@author: Amlan Ghosh
"""

'''Djikstra's Shortest Path'''
def djikstra(dist_mat, nodes): #dist_mat: dictionary {node1: {node2: 2, node3: 4}, node2: {node1: 2}}
    opt_dist = [10**5]*nodes
    opt_dist[0] = 0
    not_visited = list(i for i in range(nodes))
    for i in range(nodes):
        node = not_visited[0]
        dist = opt_dist[node]
        for j in not_visited:
            if opt_dist[j] < dist:
                node = j
                dist = opt_dist[j]
        for neighbour in dist_mat[node]:
            opt_dist[neighbour] = min(opt_dist[neighbour], opt_dist[node] + dist_mat[node][neighbour])
        not_visited.remove(node)
    print (opt_dist)    

'''Djikstra's Shortest Path using Priority Queue (heapq library in python)'''
import heapq
def djikstra_priorityqueue(dist_mat, nodes):
    opt_dist = [10**5]*nodes
    opt_dist[0] = 0
    not_visited_nodes = [i for i in range(1,nodes)]
    for neighbour in dist_mat[0]:
        opt_dist[neighbour] = min(opt_dist[neighbour], opt_dist[0] + dist_mat[0][neighbour])
    not_visited = [(opt_dist[i], i) for i in not_visited_nodes]
    heapq.heapify(not_visited)
    for i in range(nodes-1):
        node = heapq.heappop(not_visited)
        not_visited_nodes.remove(node[1])
        for neighbour in dist_mat[node[1]]:
            opt_dist[neighbour] = min(opt_dist[neighbour], opt_dist[node[1]] + dist_mat[node[1]][neighbour])
        not_visited = [(opt_dist[i],i) for i in not_visited_nodes]
        heapq.heapify(not_visited)
    print (opt_dist)

            