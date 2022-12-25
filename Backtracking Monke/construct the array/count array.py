#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

# TODO: solution validation algorithm
def isValid(arr, x):

    # if the first element is not 0, then the configuration is invalid
    if arr[0] != 1:
        return False

    # if the last element is not x, then the configuration is invalid
    if arr[len(arr)-1] != x:
        return False

    # if there exists any pair of non-unique consecutive elements, then the configuration is invalid
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return False

    # all checks passed, configuration is valid
    return True


# TODO: recursive backtracking algorithm
def arrBacktracking(arr, k, x, pos, cur):
    # base case
    if pos == n-1:
        if isValid(arr, x):
            # found a valid configuration, update number of solutions by one
            cur += 1
            return cur
        else:
            # invalid configuration, do not update the number of solutions
            return cur

    # select a candidate
    for val in [i+1 for i in range(k)]:
        # put the candidate in the array
        arr[pos+1] = val
        cur = arrBacktracking(arr, k, x, pos + 1, cur)
        # backtrack by overwriting the candidate with 0
        arr[pos+1] = 0

    # return the number of solutions
    return cur


def countArray(n, k, x):
    return arrBacktracking([0 for i in range(n)], k, x, -1, 0)
    # Return the number of ways to fill in the array.


if __name__ == '__main__':
    n = 4
    k = 3
    x = 2
    print(countArray(n, k, x))
