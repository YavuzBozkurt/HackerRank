#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def auxiliary_isSafe(arr, c):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            if not c[i] < c[i + 1]:
                return False
        if arr[i] > arr[i + 1]:
            if not c[i] > c[i + 1]:
                return False
        if arr[i] == arr[i + 1]:
            if not c[i] > c[i + 1]:
                return False
    return True


def auxiliary_candies(arr, c, possibleCandies, cur, pos):
    # base case
    if pos == len(arr)-1:
        if auxiliary_isSafe(arr, c):
            return sum(c)
        else:
            return 10000000000

    for element in possibleCandies:
        c[pos + 1] = element
        cur = min(cur, auxiliary_candies(arr, c, possibleCandies, cur, pos + 1))
        c[pos + 1] = 0
    return cur


def candies(arr, c, possibleCandies):
    cur = 10000000000
    result = auxiliary_candies(arr, c, possibleCandies, cur, -1)
    print(result)
    return (0)


if __name__ == '__main__':
    arr = [1, 2, 1, 2, 2, 3, 4]
    c = []
    possibleCandies = []
    for i in range(len(arr)):
        c.append(0)
    max_candies = max(arr)
    count = 1
    for i in range(0, max_candies):
        possibleCandies.append(count)
        count += 1
    result = candies(arr, c, possibleCandies)
