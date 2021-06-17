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

'''You are given a string S of length N. The string S consists of digits from 1-9. 
Consider the string indexing to be 1-based. You need to divide the string into blocks such that 
each block contains X consecutive elements while the last block can have less than X elements 
since N% X==0 might not be true always. 
A number is valid if it is formed by choosing exactly one digit from each block 
and placing the digits in the order of their block number.
For example:
If the given string is '123456789' and X-3, the blocks formed are [123], [456], [789]. 
Few valid numbers are 147,159,348 etc., but 124 and 396 are invalid.
Given K, a number find the Kth highest number from the valid numbers.'''

N,X,K = map(int, input().split())
s = str(input())
h = []
i = 0
while i<= N-1:
    if i+X > N:
        h.append(s[i:])
    else:
        h.append(s[i:i+X])
    i += X
K -= 1
q = [0]*len(h)
e = [0]*len(h)
q[-1] = (K%len(h[-1]))
e[-1] = K//len(h[-1])
for i in range(2,len(h)+1):
    q[-i] = (e[-i+1]%len(h[-i]))
    e[-i] = (e[-i+1]//len(h[-i]))
st = ''
for j in range(len(q)):
    st += sorted(h[j])[q[j]]
print (st)

'''Given a dictionary of N words. Given a query string S. Count the number of ways in which the query string can be constructed as a concatenation of two different words chosen from the dictionary. (here different means choosing different indices of the words).
Note - Two indices can have the same word in the dictionary. (i.j) and (j,i) are treated in separate ways.'''

n = int(input())
k = {}
for i in range(n):
    o = str(input())
    if len(o) in k:
        k[len(o)].append(o)
    else:
        k[len(o)] = [o]
q = str(input())
count = 0
for i in k:
    if len(q)-i in k and i != len(q)-i:
        for a in k[i]:
            for b in k[len(q)-i]:
                if a + b == q:
                    count += 2
if len(q)%2 == 0:
    if len(q)/2 in k:
        for i in range((len(q)/2)-1):
            for j in range(i+1,len(q)/2):
                if k[len(q)/2][i] + k[len(q)/2][j] == q:
                    count += 2
print (count)