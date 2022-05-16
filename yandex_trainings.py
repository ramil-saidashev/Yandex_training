#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:04:09 2021

@author: ramil_saidashev
"""
#1
a = 0
count = 1

for i in range(10001):
      i = int(input())
      if i != 0:
         if i > a:
            a = i
            count = 1
         elif i == a:
            count += 1
      else: break

print(count)

#2
import random

def qsort(a):
    g, e, l = [], [], []
    if len(a) > 1:
        pivot = random.choice(a)
        for x in a:
            if x < pivot:
                g.append(x)
            elif x  > pivot:
                l.append(x)
            elif x == pivot:
                e.append(x)
        return qsort(l) + e + qsort(g)
    else:
        return a
    

res = 0
n = int(input())
cases = list(map(int, input().split()))

if len(cases) > 1:  
   a = qsort(cases)
   while len(a) > 1:
       res += a.pop()

print(res)

#3
cost = 0
st = [i for i in input()]
while len(st) > 1:
    if st[0] != st[-1]:
        cost += 1
    del st[0]
    del st[-1]

print(cost)

#4

a = list(map(int, input().split()))
mags = []
houses = []
for i in range(len(a)):
    if a[i] == 1:
        houses.append(i)
    elif a[i] == 2:
        mags.append(i)

def binary(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] >x:
            r = m -1 
        else:
            l = m +1
    return l
res = []
for i in houses:
    x = binary(mags, i)
    if x >= len(mags):
        res.append(i - mags[-1])
    elif x == 0:
        res.append(mags[x]-i)
    else:
        res.append(min(mags[x] - i, i - mags[x-1])) 
  
print(max(res))

#5

def binary(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] >x:
            r = m -1 
        else:
            l = m +1
    return l

n, k = map(int, input().split())
a = list(map(int, input().split()))
a2 = [0] * n
for i in a:
    a2[i] = i


mid = n//2 
x = binary(a, mid)

if n % 2 != 0 and a2[mid] != 0:
    print(a2[mid])
    
else:
   print(a[x-1], a[x])
       
#6
x, y, z = map(int, input().split())
if y > 12 or x > 12 or y == x:
   print('1')
else:
    print('0')

#7
r = int(input())
i = int(input()) 
c = int(input())
x = i

if i == 0:
    if r != 0:
        x = 3
    else:
        x = c

elif i == 1:
    x = c

elif i == 4:
    if r != 0:
        x = 3
    else:
        x = 4

elif i == 6:
    x = 0

elif i == 7:
    x = 1

print(x)

#8
n, i, j = map(int, input().split())

if i > j:
    i, j = j, i

print(min(n - j + i - 1, j - i - 1))

#9 
n = int(input())
a = list(map(int, input().split()))
print(a[n//2])

#10
import math
d = int(input())
x, y = map(int, input().split())

x1 = 0
y1 = 0
x2 = d
y2 = 0
x3 = 0
y3 = d
v1 = (x1-x)*(y2-y1) - (x2-x1)*(y1-y)
v2 = (x2-x)*(y3-y2) - (x3-x2)*(y2-y)
v3 = (x3-x)*(y1-y3) - (x1-x3)*(y3-y)
if v1 >= 0 and v2 >= 0 and v3 >= 0:
    print(0)
else:
    da = math.sqrt(pow(x - x1, 2) + pow(y - y1, 2))
    ba = math.sqrt(pow(x - x2, 2) + pow(y - y2, 2))
    ca = math.sqrt(pow(x - x3, 2) + pow(y - y3, 2))
    m = min(da, min(ba, ca))
    if m == da:
        print(1)
    elif m == ba:
        print(2)
    else:
        print(3)

#11
import random

def qsort(a):
    g, e, l = [], [], []
    if len(a) > 1:
        pivot = random.choice(a)[0]
        for x in a:
            if x[0] < pivot:
                g.append(x)
            elif x[0]  > pivot:
                l.append(x)
            elif x[0] == pivot:
                e.append(x)
        return qsort(g) + e + qsort(l)
    else:
        return a



n = int(input())
a = []
d = None
z = 0

for _ in range(n):
    key, val = map(int, input().split())
    a.append([key, val])

x = qsort(a)
d = (x[0][0])


for i in range(len(x)):
    if x[i][0] == d:
        z += x[i][1]
    elif x[i][0] != d:
        print(d, z)
        z = 0
        d = (x[i][0])
        z += x[i][1]

print(d, z)


    

        
    
        
        
    
    
    
    