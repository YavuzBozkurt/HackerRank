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

# TODO: valid assignment checker function
def auxiliary_isSafe(arr, c):
    # make a check through all candies in the array
    for i in range(len(arr) - 1):
        # rating (i) < rating (i+1) ==> candies (i) < candies (i+1)
        if arr[i] < arr[i + 1]:
            if not c[i] < c[i + 1]:
                return False
        # rating (i) > rating (i+1) ==> candies (i) < candies (i+1)
        if arr[i] > arr[i + 1]:
            if not c[i] > c[i + 1]:
                return False
        # rating (i) == rating (i+1) ==> candies (i) > candies (i+1)
        if arr[i] == arr[i + 1]:
            if not c[i] > c[i + 1]:
                return False
    return True


# TODO: recursive backtracking function
def auxiliary_candies(arr, c, possibleCandies, cur, pos):
    # base case
    if pos == len(arr) - 1:
        if auxiliary_isSafe(arr, c):
            # valid assignment, return no. of candies
            return sum(c)
        else:
            # invalid assignment, return infinity
            return 10000000000

    # BFS candy positioning
    for element in possibleCandies:
        # put candy to the candies array
        c[pos + 1] = element
        # DFS via recursion to place new candies, step case
        cur = min(cur, auxiliary_candies(arr, c, possibleCandies, cur, pos + 1))
        # backtrack
        c[pos + 1] = 0
    # return solution to candies function
    return cur


# TODO: main function
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
