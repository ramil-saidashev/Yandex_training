#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:38:20 2021

@author: ramil_saidashev
"""
#1
st = input()
verdict = None
stack = []

for i in st:
    if i == '(':
        stack.append(i)
    elif i == ')':
        if stack:
            stack.pop()
        else:
            verdict = 1
            break

if verdict == None and stack == []:
    print('YES')
else:
    print('NO')

#2
def findT2(A, B, C, l1, l2, l3, n):
    
    res = [[1000000000, 1000000000, 1000000000]]
    d = {}
    
    for i in range(l1):
        if A[i] not in d:
            d[A[i]] = i
        else: 
            continue
        
    for i in range(l2):
        for j in range(l3):
            if n - B[i] - C[j] in d:
               x = n - B[i] - C[j]
               res[-1] = min(res[-1], [d[x], i, j])
    
    if res[-1] != [1000000000, 1000000000, 1000000000]:
        return res[-1]
    else:
        return -1

n = int(input())
A = list(map(int, input().split()))[1:]
B = list(map(int, input().split()))[1:]
C = list(map(int, input().split()))[1:]

l1 = len(A)
l2 = len(B)
l3 = len(C)

ans = findT2(A, B, C, l1, l2, l3, n)

print(*ans) if ans != -1 else print(-1)

#3

n = int(input())
l = list(map(int, input().split()))
s = l[0]
a = l[0]

for i in l[1:]:
    a = max(i, a + i)
    s = max(s, a)
    
print(s)

#4
def getsum(BITTree,i):
    s = 0 
    i = i+1
    
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

  
def construct(arr, n):
    BITTree = [0]*(n+1)
    for i in range(n):
        i += 1
        while i <= n:
            BITTree[i] += arr[i]
            i += i & (-i)
    return BITTree


def gt(BITTree, l, r):
    print(getsum(BITTree, r) - getsum(BITTree, l-1))


n, q = map(int, input().split())
a = list(map(int, input().split()))

b = construct(a, len(a))

for _ in range(q):
    l, r = map(int, input().split())
    gt(b, l-1, r-1)
    
    
#5
import bisect

n, m = map(int, input().split())    
x = list(map(int, input().split()))
y = list(map(int, input().split()))

c = 0
res = []
for i in range(len(y)):
    y[i] -= 1

for i in range(len(x)):
    t = bisect.bisect(y, x[i])   
    if y[t-1] >= x[i]:
        c += 1
        res.append(t)
        y[t-1] = y[t-1] - x[i]
        y.remove(t-1) if y[t-1] == 0 else bisect.insort(y, y.pop(t-1))
    elif y[t-1] < x[i] and y[t-1] != y[-1]:
         if y[t] >= x[i]:
             c += 1
             res.append(t+1)
             y[t] = y[t] - x[i]
             y.remove(t) if y[t] == 0 else bisect.insort(y, y.pop(t))
         elif y[t] < x[i]:
             res.append(0)
    else:
        res.append(0)
        


print(c)
print(*res)   
        
            

    
    

    



    
    

  
