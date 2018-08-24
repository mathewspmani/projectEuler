# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:22:29 2018

@author: mathewspmani
"""

import math 

def even_fib_sum(n):
    sum2 = 0
    
    fibfor = [1,1,2]
    while len(fibfor) <= 3*(int(math.log(n))):
        fibfor.append(fibfor[-1]+ fibfor[-2])
#    print(fibfor)
    loc=2
    for i in range(1, int(math.log(n))+1):
        op = fibfor[loc]
#        print(f"{i} and {op}")
        loc = loc + 3
        if op < n:
            sum2 = sum2 + op
        else:
            break
    
    return sum2

even_fib_sum(4000000)