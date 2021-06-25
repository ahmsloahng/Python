# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:04:44 2021

@author: ORMAE
"""
nodes = 10
visited = [False]*nodes
previous = [0]*nodes
def dfs(G,v): #G: graph, nested dictionary with node as key the neighbours as a dictionary, v is the node we start with
    visited[v] = True
    for neighbour in v:
        if visited[neighbour] == False:
            previous[neighbour] = v
            dfs(G,neighbour)
    

