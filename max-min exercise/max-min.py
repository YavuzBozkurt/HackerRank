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
            cur = [x for x in setFound]
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
    k = 3
    set = [1, 19, 4, 3]

    maxMin(k, set)
