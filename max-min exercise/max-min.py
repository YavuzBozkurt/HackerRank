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
def unfairBacktrack(arr, unfairArr, pos, cur):

    if pos == len(unfairArr) - 1:
        return unfairArr

    for element in arr[:]:
        unfairArr[pos + 1] = element
        setFound = unfairBacktrack(arr, unfairArr, pos + 1, cur)
        if max(setFound) - min(setFound) < max(cur) - min(cur):
            cur = setFound
        unfairArr[pos+1] = 0
    return cur


def maxMin(k, arr):
    unfairArr = []
    for i in range(k):
        unfairArr.append(0)
    cur = [10000000000000000000000, -10000000000000000000000]
    result = unfairBacktrack(arr, unfairArr, -1, cur)
    print(result)
    return result


# Write your code here

if __name__ == '__main__':

    k = 2
    arr = [1, 2, 3, 4]

    maxMin(k, arr)
