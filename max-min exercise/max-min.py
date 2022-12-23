#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


# TODO: recursive backtracking function
def unfairBacktrack(set, unfairArr, pos, cur):
    if pos == len(unfairArr) - 1:
        return unfairArr

    for element in set:
        unfairArr[pos + 1] = element
        setFound = unfairBacktrack([x for x in set if x != element], unfairArr, pos + 1, cur)
        if max(setFound) - min(setFound) < max(cur) - min(cur):
            cur = setFound
    return cur


def maxMin(k, set):
    unfairArr = []
    for i in range(k):
        unfairArr.append(0)
    cur = [10000000000000000000000, -10000000000000000000000]
    result = unfairBacktrack(set, unfairArr, -1, cur)
    print(result)
    return result


# Write your code here

if __name__ == '__main__':
    k = 2
    set = [1, 19, 4]

    #maxMin(k, set)

    val = [1,2]
    cur = val
    val.append(3)
    print(cur)
#print(f'element: {element}, set:{set}, unfairArr: {unfairArr}, cur {cur}')
#print(f'max(setFound) : {max(setFound)} - min(setFound): {min(setFound)}  < max(cur) : {max(cur)} - min(cur): {min(cur)}')
#print(f'base case is hit with cur: {cur}, set: {set}, unfairArr: {unfairArr}')
#print(f'cur is set to {cur}')