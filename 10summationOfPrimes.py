# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:53:39 2018

@author: mathewspmani
"""
import math
def isprime2(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    limit = math.floor(math.sqrt(num))
    for i in range(5,limit+1,2):
        if num % i == 0:
            return False
    return True

answer = 5
limit = 2000000
for i in range(5, limit, 2):
    if isprime2(i):
        answer += i
print(answer)