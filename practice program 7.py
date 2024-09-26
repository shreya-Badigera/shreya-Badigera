# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:58:20 2024

@author: shrey
"""

s=input()
v='aeiou'
d={}
mx=0
for i in s:
    if i in v:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if d[i]>mx:
            mx=d[i]
            ans=i
print(ans)