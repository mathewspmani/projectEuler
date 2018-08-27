# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:47:44 2018

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

def getsum(num):
    factors = getprimefactors(num)
    total = 1
#    print(factors)
    for factor, power in factors.items():
        intsum = 0
        for pr in range(0,power+1):
            intsum += factor ** pr
        total *= intsum
    return (total - num)

def checkifamicable(numdict, fsum, num):
    if fsum in numdict.keys():
        if numdict[fsum] == num and fsum != num:
            return True
    return False

factdict = {}
amicable = []
for i in range(1,10000):
    factdict[i] = getsum(i)
    if checkifamicable(factdict, factdict[i], i):
        amicable.append(i)
        amicable.append(factdict[i])

sum(list(set(amicable)))
        


