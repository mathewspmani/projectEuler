# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 01:34:58 2018

@author: mathewspmani
"""

#count letters in words
def getwords(i):

    base = {0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety" }
    
    last2bit = ""
    middlebit = ""
    firstbit = ""
    if i % 100 <= 20:
        last2bit = base[i % 100]
    else:
        last2bit = base[i % 100 - i % 10] + base[i % 10]
    if i // 100 > 0:
        if i % 100 == 0:
            middlebit = "hundred"
        else:
            middlebit = "hundredand"
    if i // 100 > 0:
        firstbit = base[i // 100]
    return firstbit+middlebit+last2bit

getwords(199)

answer = ""
for i in range(1,1000):
    answer += getwords(i)

answer += "onethousand"
