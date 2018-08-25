# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:02:36 2018

@author: mathewspmani
"""

#all primes in the form 6n -1 or 6n + 1

nth = 10001
nthreq = (nth - 2)//2
if nthreq % 2 == 0:
    flag = 1
else:
    flag = -1

nthreqprime = 6*(nthreq) + flag
print(nthreqprime)
