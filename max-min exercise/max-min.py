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
    # base case
    if pos == len(unfairArr) - 1:
        return unfairArr

    for element in arr:
        # add the element to the unfairArr
        unfairArr[pos + 1] = element
        # exclude the already added element
        setFound = unfairBacktrack([x for x in arr if x != element], unfairArr, pos + 1, cur)
        # compare the computed set with the least unfair set found so far
        if max(setFound) - min(setFound) < max(cur) - min(cur):
            # found a less unfair set, update cur
            cur = [x for x in setFound]
    # return the solution
    return cur


def maxMin(k, arr):
    unfairArr = []
    for i in range(k):
        unfairArr.append(0)
    cur = [10000000000000000000000, -10000000000000000000000]
    return unfairBacktrack(arr, unfairArr, -1, cur)


# Write your code here

if __name__ == '__main__':
    k = 2
    # all the elements need to be identical
    arr = [1, 2, 4, 3]
    print(maxMin(k, arr))
