#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:28:16 2021

@author: ramil_saidashev
"""

#1
import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    x = bisect.bisect_left(a, i)
    if x < len(a) and a[x] == i:
        print('YES')
    else:
        print('NO')

#2
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    x = bisect.bisect_left(a, i)
    if x >= len(a):
        print(a[-1])
    else:
        if abs(a[x]-i) < abs(a[x-1]-i):
            print(a[x])
        elif abs(a[x]-i) > abs(a[x-1]-i):
            print(a[x-1])
        else:
            print(min(a[x], a[x-1]))
#3
w, h, n = map(int, input().split())

l = 0
r = max(w, h) * n

while l < r:
    mid = (l+r)//2
    f = mid // w
    s = mid // h
    if n <= (f * s):
        r = mid
    else:
        l = mid + 1

print(l)

#4
n, a, b, w, h = map(int, input().split())

l = 0
r = 10**18
while r - l > 1:
    m = (l+r) // 2
    if max(((w//(a + 2 * m)) * (h//(b + 2* m))), ((h//(a + 2 * m)) * (w//(b + 2* m))))  >= n:
        l = m
    else:
        r = m

print(l)

#5
a = int(input())
b = int(input())
c = int(input())

s = a * 2 + b * 3 + c * 4
d = a + b + c

l = 0
r = a+b+c+1
while l < r:
    m = (r+l) // 2
    if 10 * (s + 5 * m) < 35 * (d + m):
       l = m + 1
    else:
        r = m

print(l)

#6
N, x, y = map(int, input().split())

l = 0
r = (N-1)*max(x, y)
while r-l>1:
    m = (r+l)//2
    if m//x + m//y < N-1:
        l = m
    else:
        r = m

print(r + min(x, y))

#7
n = int(input())
m = int(input())
t = int(input())

s = n * m











        







    



