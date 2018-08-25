# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:46:52 2018

@author: mathewspmani
"""

def fn():
    for a in range(1,999):
        for b in range(1,999):
            c = 1000 - b - a
            if c > b > a:
                if a**2 + b**2 == c**2:
                    return (a,b,c)
                else:
                    continue

fn()
