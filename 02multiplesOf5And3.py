# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:54:43 2018

@author: mathewspmani
"""

a=[3,5]
leng = 1000
a3 = [3*i for i in range(999//3+1)]
a5 = [5*i for i in range(999//5+1)]

a35 = a3 + a5
aa=list(set(a35))
sum(list(set(a35)))
