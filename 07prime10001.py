# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:02:36 2018

@author: mathewspmani
"""

#all primes in the form 6n -1 or 6n + 1
import math
#nth = 6
def isprime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

def nthprime(nth):
    primelist = [2,3]
    i = 5
    while True:
        if (i + 1) % 6 == 0 or (i - 1) % 6 == 0:
            if isprime(i):
                primelist.append(i)
        if len(primelist) >= nth:
            break
        i = i + 1
    return primelist
        

nthprime(10001)


#more efficient is prime function from the overview solution
#erasthones solution. Idea is that n= root n * root n = a * b. 
#If one of the factors is less than  root of the f, then the other should be. 
#So if we cant find a factor for n which is less than root n, it means that
#the only possible factor is the number n itself, making n prime

def isprime2(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    limit = math.floor(math.sqrt(num))
    for i in range(5,limit+1,2):
        if num % i == 0:
            return False
    return True

isprime(29)
        
    