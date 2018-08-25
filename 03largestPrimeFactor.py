# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:56:28 2018

@author: mathewspmani
"""

num = 600851475143

#TRIAL DIVISION

def getfactors(num):
    factors = []
    fac = 2
    while num > 1:
        while num % fac == 0:
            factors.append(fac)
            num /= fac
        fac = fac + 1
    return sorted(factors)[-1]

getfactors(num)
            

#IMPROVEMENTS

#all primes after 2,3 in the form 6n - 1 or 6n + 1

def getfactors(num):
    factors = []
    fac = 2
    while num > 1:
        if fac > 3:
            if (fac + 1) % 6 == 0 or (fac - 1) % 6 == 0:
                while num % fac == 0:
                    factors.append(fac)
                    num /= fac
        else: 
            while num % fac == 0:
                    factors.append(fac)
                    num /= fac
        fac = fac + 1
    return sorted(factors)[-1]

getfactors(num)



