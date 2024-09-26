# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:09:42 2024

@author: shrey
"""

import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Input reading
a, b = map(int, input().split())

# Calculate GCD and LCM
gcd_value = gcd(a, b)
lcm_value = lcm(a, b)

print(gcd_value)
print(lcm_value)