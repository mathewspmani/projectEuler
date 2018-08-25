# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:26:09 2018

@author: mathewspmani
"""
from operator import mul
import functools

def getprimefactors(num):
    factors = {}
    factors[2] = 0
    factors[3] = 0
    fac = 2
    while num > 1:
        if fac > 3:
            if (fac + 1) % 6 == 0 or (fac - 1) % 6 == 0:
                factors[fac] = 0
                while num % fac == 0:
                    factors[fac] = factors[fac] + 1
                    num /= fac
        else: 
            while num % fac == 0:
                    factors[fac] = factors[fac] + 1
                    num /= fac
        fac = fac + 1
    return factors

def getmaxexponents(original, newdict):
    for key, item in newdict.items():
        if key in original.keys():
            if newdict[key] > original[key]:
                original[key] = newdict[key]
        else:
            original[key] = newdict[key]
    return original

start = 1
end = 20
numbers = { i : getprimefactors(i) for i in range(start, (end + 1))}

finaldict = {}
for key, item in numbers.items():
    finaldict = getmaxexponents(finaldict, numbers[key])

answer = functools.reduce(mul,[key**value for key, value in finaldict.items()])
