#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:06:44 2021

@author: ramil_saidashev
"""

#1 bisect count intervals
import random
import bisect

def sort(a):
    l =[]
    e = []
    g = []
    if len(a) > 1:
        pivot = random.choice(a)
        for x in a:
            if x < pivot:
                l.append(x)
            elif x == pivot:
                e.append(x)
            elif x > pivot:
                g.append(x)
        return sort(l) + e + sort(g)
    else:
        return a

n = int(input())
a = list(map(int, input().split()))
res = []
a = sort(a)
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    res.append(bisect.bisect_right(a, r) - bisect.bisect_left(a, l))

print(*res)

#2 left/right entry
import bisect
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

d = {}

for i in b:
    l = bisect.bisect_left(a, i)
    r = bisect.bisect_right(a, i)
    if i not in d:
        if r-l == 0:
            d[i] = [0, 0]
        else:
            d[i] = [l+1, r]
        print(d[i][0], d[i][1])
    else:
        print(d[i][0], d[i][1])

#3 cubic equation
a, b, c, d = map(float, input().split())
e = 0.00000001
if a <0:
   a, b, c, d = -a, -b, -c, -d

def f(x):
    return a * x**3 + b * x**2 + c*x +d

def root():
    l = -1500
    r = 1500
    while r - l >= e:
        m = (r+l)/2
        if f(m) <= 0:
            l = m
        else:
            r = m
    return (l + r) / 2

print(root())

#4 deforestation
a, k, b, m, x = map(int, input().split())

def howm(lu, rs, x):
    return (x-x//rs) * lu

def binary():
    l = 0
    r = 2 * x//(a+b) + 1
    while r - l > 1:
        days = (l + r)//2
        p1 = howm(a, k, days)
        p2 = howm(b, m, days)
        if p1 + p2 >= x:
            r = days
        else:
            l = days
    return r

print(binary())

#5 find the length of k-segments to cover n dots
n, k = map(int, input().split())
a = list(map(int, input().split()))

def search(a, k):
    l = 0
    r = a[len(a)-1] - a[0]
    while l < r:
        m = (l + r) // 2
        if r == m:
            return r
        if islen(a, k, m):
            r = m
        else:
            l = m + 1
    return r
 

def islen(a, k, m):
    end = 100000000000000
    for i in range(len(a)-1, -1, -1):
           if end > a[i] and k != 0:
              k -=1
              end = a[i] - m  
    if end > a[0]:
       return False
    else:
        return True

a = sort(a)
print(search(a, k))


    
    
        
        
        
    
