#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'candlesCounting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY candles
#
# ENTIRE SEQUENCE VERSION, MONKE MISUNDERSTOOD :)

# TODO: solution validation algo
def isValid(k, candleConfig, no_of_candles):
    # initialize sets to store seen candles and colors
    seenSoFar, colorsSoFar = [], []
    for x in candleConfig:
        # if candle has not been seen before, add it
        if x not in seenSoFar:
            seenSoFar.append(x)
    if len(seenSoFar) == no_of_candles:
        for x in candleConfig[:-1]:
            # if the height of current candle is not less than the height of the next candy, return false
            if not x[0] < candleConfig[candleConfig.index(x) + 1][0]:
                return False
        # check if the candle sequence has every color among k at least once
        for x in candleConfig:
            if x[1] not in colorsSoFar:
                colorsSoFar.append(x[1])
        if len(colorsSoFar) == k:
            return True
        else:
            return False
    # if there are duplicate candies, return false
    else:
        return False


# TODO: recursive bactracking algorithm
def candleBacktracking(k, candles, candleConfig, cur):
    # base case
    if len(candleConfig) == len(candles):
        if isValid(k, candleConfig, len(candles)):
            # valid configuration found, update cur
            cur += 1
            return cur
        else:
            # invalid configuration, don't update cur
            return cur

    for candle in candles:
        # add candle to the candy configuration
        candleConfig.append(candle)
        cur = candleBacktracking(k, candles, candleConfig, cur)
        # remove candle from the configuration to backtrack
        del candleConfig[len(candleConfig) - 1]

    return cur


def candlesCounting(k, candles):
    return candleBacktracking(k, candles, [], 0)


if __name__ == '__main__':
    k = 3
    candles = [[1, 1], [3, 2], [2, 2], [4, 3]]
    print(candlesCounting(k, candles))