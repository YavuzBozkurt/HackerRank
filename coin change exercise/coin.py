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
        counter1 = Counter(changeArr)
        counter2 = Counter(arr)
        if counter1 == counter2:
            return False
    return True


# TODO: recursive backtracking algorithm
def coinBacktrack(n, c, changeArr, goodsSoFar, count):
    if sum(changeArr) >= n:
        if sum(changeArr) == n and isValid(changeArr, goodsSoFar):
            count += 1
            goodsSoFar.append([x for x in changeArr])
            return count
        else:
            return count

    for coin in c:
        changeArr.append(coin)
        count = coinBacktrack(n, c, changeArr, goodsSoFar, count)
        changeArr.pop(len(changeArr) - 1)

    return count


def getWays(n, c):
    # Write your code here
    return coinBacktrack(n, c, [], [], 0)


if __name__ == '__main__':
    n = 10
    c = [2, 5, 3, 6]

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    print(getWays(n, c))

# print(f'base case: count += 1 done, good goodsSoFar : {goodsSoFar}')
# print(f'base case: count += 0 done, bad goodsSoFar: {goodsSoFar}')
# print(f'changeArr appended: {changeArr}')
# print(f'count: {count}')
# print(f'changeArr popped: {changeArr}')
