# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:23:30 2018

@author: mathewspmani
"""

a = list(range(100,1000))
b = list(range(100,1000))

highest = 0
for i in a:
    for j in b:
        if str(i*j) == str(i*j)[::-1]:
           if i*j > highest:
               highest = i*j