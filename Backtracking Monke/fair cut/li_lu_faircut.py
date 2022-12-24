#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# TODO: auxiliary fairness computation algorithm
def auxiliary_unfair(unfairArr, k):
    # create a set of sets identify li's and lu's integers
    li_and_lu = [[val for val in unfairArr[0:k]], [val for val in unfairArr[k:len(unfairArr)]]]
    # initialize unfairness to be 0
    unfairness = 0
    for x in li_and_lu[0]:
        for y in li_and_lu[1]:
            # compute unfairness for given x, y pair
            unfairness += abs(x - y)
    # return unfairness magnitude
    return unfairness


# TODO: recursive backtracking algorithm
def fairBacktrack(k, arr, unfairArr, pos, cur):
    # base case
    if pos == len(unfairArr) - 1:
        # compute unfairness magnitude
        return auxiliary_unfair(unfairArr, k)

    for element in arr:
        # select candidate
        unfairArr[pos + 1] = element
        # compute the minimum unfairness magnitude so far
        cur = min(cur, fairBacktrack(k, [x for x in arr[arr.index(element) + 1:]], unfairArr, pos + 1, cur))
        # backtrack
        unfairArr[pos + 1] = 0
    return cur


def fairCut(k, arr):
    return fairBacktrack(k, arr, [0 for i in range(len(arr))], -1, 100000000000)


if __name__ == '__main__':
    k = 1
    arr = [3, 3, 3, 1]
    print(fairCut(k, arr))
