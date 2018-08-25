# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:01:32 2018

@author: mathewspmani
"""

a=list(range(1,101))
answer = 0
for ind, i in enumerate(a[:-1]):
    answer = answer + 2 * sum([a[ind] * i for i in a[ind+1:]])
print(answer)

