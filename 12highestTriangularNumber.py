# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 23:15:58 2018

@author: mathewspmani
"""

def getprimefactors(num):
    factors = {}
    fac = 2
    while num > 1:
        if fac > 3:
            if (fac + 1) % 6 == 0 or (fac - 1) % 6 == 0:
                while num % fac == 0:
                    factors[fac] = factors.get(fac, 0) + 1
                    num /= fac
        else: 
            while num % fac == 0:
                    factors[fac] = factors.get(fac, 0) + 1
                    num /= fac
        fac = fac + 1
    return factors

#using the fact that each triangle number is in the form n*(n+1)/2, find pairs
#    of consecutive numbers with number of divisors adding to 501( to account 
#for 2 in denomin)
    
from operator import mul    
from functools import reduce

def pairs(limit):
    first = 2
    second = 3
    while True:
        firstf = getprimefactors(first)
        secondf = getprimefactors(second)
        totaldict = { k: firstf.get(k,0) + secondf.get(k,0) + 1 for k in 
                     set(firstf) | set(secondf)}
        totaldict[2] -= 1
        if reduce(mul, list(totaldict.values())) > limit:
            break
        else:
            first += 1
            second += 1
    return first*second/2

pairs(500)