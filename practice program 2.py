# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:33:23 2024

@author: shrey
"""

N=int(input())
A=int(input())
sum=0
count=0
for pos in A:
    sum += pos
    if sum == 0:
        count+=1
print(count)