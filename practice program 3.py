# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:46:33 2024

@author: shrey
"""

N=int(input())
chocolates=list(map(int,input().strip().split()))
total=0
for jar in chocolates:
    if jar%3!=0:
        total+=jar//3+1
    else:
        total+=jar//3
print(total)