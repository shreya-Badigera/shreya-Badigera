# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:10:52 2024

@author: shrey
"""

N=int(input())
P=int(input())
time=240-P
timeleft=time
i=1
while i <= N and 5+i <= timeleft:
    timeleft-= 5*i
    i +=1
print(i-1)