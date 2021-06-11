# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:14:28 2021

@author: Amlan Ghosh
"""

'''There are N file extensions in a system with Q1 files of extension 1, 
   Q2 files of extension 2 and till QN files of extension N. 
   But the problem with them is that if one deletes one file of some extension, 
   then all the other files of that same extension vanishes. 
   There is also a special file extension 0, with Q0 quantity of files, 
   if one deletes one file of that extension 0, then all the files of all the extensions vanish. 
   What is the expected number of files one will delete till all the files of all the extensions vanishes? 
   Your answer would be considered correct if it has a precision of exactly 6 decimal places.'''

q = {}
n,q[0] = map(float, input().split())
n = int(n)
print (n)
for i in range(1,n+1):
    q[i] = float(input())
superset = [[0]]
for i in range(1,n+1):
    k = []
    for j in superset:
        k.append(j + [i])
    superset = superset + k
u = 0
l = 0
for i in superset:
    m = 1
    for j in i:
        m = m*q[j]
    u += len(i)*m
    l += m
print (round(u/l,6))