# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:50:26 2021

@author: Amlan Ghosh
"""
'''Given an array of size N and a number K. 
You need to partition the array into K non-empty partitions such that the sum of (max-min) in each partition is maximised.'''

n,k = map(int, input().split())
a = list(map(int, input().split()))
def f(n,k,a):
    if k == 1:
        return max(a) - min(a)
    else:
        return max([(max(a[:i+1]) - min(a[:i+1]) + f(n-i-1,k-1,a[i+1:])) for i in range(n-k+1)])
p = f(n,k,a)
print (p)