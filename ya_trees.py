#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:40:47 2021

@author: ramil_saidashev
"""

#1 basic BST 
class Node:
    def __init__(self, key, parent = None):
        self.parent = parent
        self.left = None
        self.right = None
        self.val = key
        self.height = self.parent.height + 1 if self.parent else 0
      
    
def insert(root, key, parent = None):
    if root is None:
       root = Node(key, parent = parent )
       print ('DONE')
       return root
    else:
       if root.val == key:
          print('ALREADY')
          return root
       elif root.val > key:
            root.left = insert(root.left, key, parent = root)
       else:
           root.right = insert(root.right, key, parent = root)     
    return root

def search(root, key):
    if root is None:
        return False
    if root.val == key:
        return True
    elif root.val > key:
        return search(root.left, key)
    elif root.val < key:
        return search(root.right, key)
    return False
                         
def get(root):
    if root.left:
       get(root.left)
    if root.height > 0:
       for i in range(root.height):
           print('.', end = '')
    print(root.val)    
    if root.right:
       get(root.right)

r = None
             
while True:
    try:
      line = input()
      line = line.split()
      if len(line) > 1:
          x = int(line[1])
          if line[0] == 'ADD':
             r = insert(r, x)
          if line[0] == "SEARCH":
           if search(r, x) == False:
                print('NO')
           else:
                print('YES')
      else:
            get(r)
    except EOFError:
             break
    
#2 is ancestor?
def find(a, i, k):
    new = a[i]
    if new == k:
        return True
    elif new == -1:
        return False
    else:
        return find(a, new, k)
    return False

file = open('input.txt')
lines = file.readlines()
file.close()

n = int(lines[0])
d, c, a = {}, 0, []
res = []

for line in lines[1:n]:
    k, p = line.split()
    if k not in d:
       a.append(None)
       d[k] = c
       c += 1
    if p not in d:
        a.append(None)
        d[p] = c 
        c += 1
    a[d[k]] = d[p]
    if a[d[p]] == None:
        a[d[p]] = -1
        
for line in lines[n:]:
        x, y = line.split()
        x, y = d[x], d[y]
        if find(a, x, y):
            res.append(2)
        elif find(a, y, x):
            res.append(1)
        else:
            res.append(0)

print(*res)

#3 LCA
def lca(a, j, k):
    visited = [False for i in range(len(a))]
    visited[j] = True
    while a[j][0] != -1:
        visited[j] = True
        j = a[j][0]
    visited[j] = True
    while visited[k] == False:
        k = a[k][0]
    return k 
       
file = open('input.txt')
lines = file.readlines()
file.close()

n = int(lines[0])
d, c, a = {}, 0, [] 

for line in lines[1:n]:
    k, p = line.split()
    if k not in d:
       a.append(None)
       d[k] = c
       c += 1
    if p not in d:
        a.append(None)
        d[p] = c 
        c += 1
    a[d[k]] = [d[p], k]
    if a[d[p]] == None:
        a[d[p]] = [-1, p]
      
for line in lines[n:]:
    x, y = line.split()
    x, y = d[x], d[y]
    print(a[lca(a, x, y)][1])

#4 huffman
n = int(input())
for _ in range(n):
    line = input()
    cell = ''
    ans = []
    
    for j in line:
        if j == 'D':
            cell += '0'
        else:
            ans.append([cell])
            i = -1
            
            while cell[i] == '1':
                i -= 1
           
            if i < -1:
                cell = cell[:i+1]
            
            cell = cell[:-1] + '1'
            print(cell)
    ans.append([cell])
        
    print(len(ans))
    for el in ans:
        print(el)

#5 diameter of a tree
#this one fails 
def make(a, b, arr):
    arr[a].append(b)
    arr[b].append(a)

def DFS(node, d):
    global vis, arr, mxD, mxN
    vis[node] = 1
    d += 1
    for i in arr[node]:
        if vis[i] == 0:
           if d > mxD:
              mxN = i
              mxD = d
           DFS(i, d)

def dffs(node, n):
    d = 0
    for i in range(n+1):
        vis[i] = 0
    DFS(node, d +1)

def diameter(n):
    global arr, mxD
    dffs(start, n)
    dffs(mxN, n)
    return mxD
    
n = int(input())
arr, vis = [[] for i in range(n+1)], [0 for i in range(n+1)]
mxD, mxN = -1, -1
start = 0
for i in range(n-1):
    a, b = map(int, input().split())
    if i == 0:
        start = min(a, b)
    make(a, b, arr)

diameter(n)

# this one does not
from collections import deque
class Graph:
    def __init__(self, node):
        self.node = node
        self.arr = {i:[] for i in range(self.node)}
    
    def add(self, a, b):
        self.arr[a].append(b)
        self.arr[b].append(a)
    
    def BFS(self, u):
        vis = [False for i in range(self.node + 1)]
        distance = [-1 for i in range(self.node + 1)]
        distance[u]= 0
        q = deque()
        q.append(u)
        vis[u] = True
        while q:
            front = q.popleft()
            for i in self.arr[front]:
                if not vis[i]:
                    vis[i] = True
                    distance[i] = distance[front] +1
                    q.append(i)
        mxD = 0
        mxN = -1
        for i in range(self.node):
            if distance[i] > mxD:
                mxD = distance[i]
                mxN = i
        return mxN, mxD
    def diameter(self, start):
        node, dis = self.BFS(start)
        node2, dia = self.BFS(node)
        print(dia+1)
    
n = int(input())
G = Graph(n+1)
start = 10**19
for i in range(n-1):
    a, b = map(int, input().split())
    start = min(a, b, start)
    G.add(a, b)

G.diameter(start)



        


    
        
    
        




    

    

       

        
    
            