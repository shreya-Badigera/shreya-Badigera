# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:11:50 2024

@author: shrey
"""

def min_key_presses(s):
    target = int(s)
    presses = 0
    
    while target > 0:
        if target % 100 == 0:
            target //= 100
        else:
            target //= 10
        presses += 1
    
    return presses

# Example usage:
s = input().strip()  
print(min_key_presses(s))