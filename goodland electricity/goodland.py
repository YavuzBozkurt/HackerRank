#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

cur = 10000000000000000


# TODO: solution validation algorithm
def isValid(k, plantConfig, plant_indices):
    isCovered = [0 for i in range(len(plantConfig))]
    for index in plant_indices:
        for i_left in range(k - 1):
            if index - (i_left + 1) < 0:
                break
            isCovered[index - (i_left + 1)] = 1
        for i_right in range(k-1):
            if index + (i_right + 1) >= len(isCovered):
                break
            isCovered[index + (i_right + 1)] = 1
    if sum(isCovered) == len(isCovered):
        return True
    else:
        return False


# TODO: recursive backtracking algorithm
def goodlandBacktrack(k, plantConfig, pos, plant_indices):
    if pos == plant_indices[len(plant_indices) - 1]:
        if isValid(k, plantConfig, plant_indices):
            return sum([1 if x == 1 else 0 for x in plantConfig])

    for x in [0, 1]:
        plantConfig[plant_indices[pos + 1]] = 1
        cur = min(cur, goodlandBacktrack(k, plantConfig, plant_indices[pos + 1], plant_indices))
        plantConfig[plant_indices[pos + 1]] = 0
    return cur


def pylons(k, arr):
    plant_indices = []
    for i in range(len(arr)):
        if arr[i] == 1:
            plant_indices.append(i)
    return goodlandBacktrack(k, [-2 if x == 0 else -1 for x in arr], plant_indices[0] - 1, plant_indices)


if __name__ == '__main__':
    n = 0
    k = 0
    arr = [0, 1, 1, 1, 0, 0, 0]
    # print(pylons(k, arr))
