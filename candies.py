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


results = []


def auxiliary_candies(arr, c, possibleCandies, pos):
    if auxiliary_isSafe(arr, c) and pos == len(arr) - 1:
        return True
    if not auxiliary_isSafe(arr, c) and pos == len(arr) - 1:
        return False

    for candy in possibleCandies:
        c[pos + 1] = candy
        if auxiliary_candies(arr, c, possibleCandies, pos + 1):
            results.append(sum(c))
        c[pos + 1] = 0
    return results


def candies(arr, c, possibleCandies):
    result = auxiliary_candies(arr, c, possibleCandies, -1)
    print(result)
    return result


if __name__ == '__main__':
    arr = [1, 2, 1, 2]
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
