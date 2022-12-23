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

# TODO: solution validation algorithm
def isValid(k, plantConfig, plant_indices):
    # create an array that will display the covered cities
    isCovered = [0 for i in range(len(plantConfig))]
    for index in plant_indices:
        # if there is a plant, then handle covering, else, don't
        if plantConfig[index] == 1:
            # a plant trivially covers the city it is in
            isCovered[index] = 1
            # cover left k - 1 cities
            for i_left in range(k - 1):
                if index - (i_left + 1) < 0:
                    break
                # cover city
                isCovered[index - (i_left + 1)] = 1
            # cover right k - 1 cities
            for i_right in range(k - 1):
                if index + (i_right + 1) >= len(isCovered):
                    break
                # cover city
                isCovered[index + (i_right + 1)] = 1
        else:
            # no plant, proceed to the next plant-able index
            continue
    # if all cities are covered, return true, else, return False
    if sum(isCovered) == len(isCovered):
        return True
    else:
        return False


# TODO: recursive backtracking algorithm
def goodlandBacktrack(k, plantConfig, pos, plant_indices, cur):
    # base case
    if pos == len(plant_indices) - 1:
        if isValid(k, plantConfig, plant_indices):
            # return the number of power plants in the plant configuration
            return sum([1 if x == 1 else 0 for x in plantConfig])
        else:
            # invalid plant configuration, no update for cur
            return cur

    # selection candidate is either putting power plant or not
    for x in [0, 1]:
        # put power plant
        plantConfig[plant_indices[pos + 1]] = x
        # take the minimum number of plants used
        cur = min(cur, goodlandBacktrack(k, plantConfig, pos + 1, plant_indices, cur))
        # backtrack by removing power plant
        plantConfig[plant_indices[pos + 1]] = 0
    return cur


def pylons(k, arr):
    # create an array in which plant indices will be carried
    plant_indices = []
    for i in range(len(arr)):
        if arr[i] == 1:
            plant_indices.append(i)
    return goodlandBacktrack(k, [-2 if x == 0 else -1 for x in arr], -1, plant_indices, 1000000000000)


if __name__ == '__main__':
    k = 3
    arr = [0, 1, 0, 0, 0, 0, 1]
    print(pylons(k, arr))