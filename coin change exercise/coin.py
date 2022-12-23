#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

# def isValid(changeArr, goodSoFar):


# TODO: solution validation algorithm
def isValid(changeArr, goodsSoFar):
    for arr in goodsSoFar:
        # count how many of each element there are in arrays changeArr and arr \in goodsSoFar
        counter1 = Counter(changeArr)
        counter2 = Counter(arr)
        if counter1 == counter2:
            # identical change with different permutation only, return false
            return False
    # new and unique change
    return True


# TODO: recursive backtracking algorithm
def coinBacktrack(n, c, changeArr, goodsSoFar, count):
    # base case
    if sum(changeArr) >= n:
        # is solution valid
        if sum(changeArr) == n and isValid(changeArr, goodsSoFar):
            # valid solution
            count += 1
            # add it to goodsSoFar so that an identical change with different permutation is not re-counted
            goodsSoFar.append([x for x in changeArr])
            return count
        else:
            # invalid solution
            return count

    for coin in c:
        changeArr.append(coin)
        count = coinBacktrack(n, c, changeArr, goodsSoFar, count)
        # backtrack
        changeArr.pop(len(changeArr) - 1)
    # return count to previous call
    return count


def getWays(n, c):
    # Write your code here
    # initialize count to be 0
    return coinBacktrack(n, c, [], [], 0)


if __name__ == '__main__':
    n = 10
    c = [2, 5, 3, 6]

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    print(getWays(n, c))

