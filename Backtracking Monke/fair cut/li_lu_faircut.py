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
    li_and_lu = [[val for val in unfairArr[0:k]], [val for val in unfairArr[k:len(unfairArr)]]]
    unfairness = 0
    for x in li_and_lu[0]:
        for y in li_and_lu[1]:
            unfairness += abs(x - y)
    return unfairness


# TODO: recursive backtracking algorithm
def fairBacktrack(k, arr, unfairArr, pos):
    if pos == len(arr) - 1:
        return auxiliary_unfair(unfairArr)

    return 0


def fairCut(k, arr):
    return fairBacktrack(k, arr, [0 for i in range(len(arr))], -1)


if __name__ == '__main__':
    k = 2
    arr = [1, 2, 3, 4]
    # [1, 1], [2, 1]
    # print(fairCut(k, arr))
