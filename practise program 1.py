# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:44:54 2024

@author: shrey
"""

goals=int(input())
size=int(input())
l=list(map(int,input().split()))
max=0
for i in range(0,len(l)):
    sub=l[i:i+size]
    k=1
    s=0
    for j in sub:
        s+=(j*k)
        k+=1
        if  s>max:
            max=s
print(max)