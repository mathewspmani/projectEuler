# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 00:22:42 2018

@author: mathewspmani
"""

import anytree as at

def findnextnum(nextnum):
    if nextnum % 2 == 0:
        return nextnum // 2
    else:
        return 3 * nextnum + 1

numbers = {}
numbers [1] = at.Node(1)

for num in range(1,1000001):
    if num not in numbers.keys():
        childnum = num
#        print(f"c{num}")
        numbers[childnum] = at.Node(childnum)
        while True:
#            print(childnum)
            parentnum = findnextnum(childnum)
            if parentnum not in numbers.keys():
                numbers[parentnum] = at.Node(parentnum)
                numbers[childnum].parent = numbers[parentnum]
                childnum = parentnum
            else:
                numbers[childnum].parent = numbers[parentnum]
#                print(at.RenderTree(numbers[parentnum]))
                break


numbers[1].height

flag = 1
for i in numbers[1].descendants:
    if i.depth > flag:
        flag = i.depth
        answer = i.name

