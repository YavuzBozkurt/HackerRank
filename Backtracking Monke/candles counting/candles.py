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
    seenSoFar, colorsSoFar = [], []
    for x in candleConfig:
        if x not in seenSoFar:
            seenSoFar.append(x)
    if len(seenSoFar) == no_of_candles:
        for x in candleConfig[:-1]:
            if not x[0] < candleConfig[candleConfig.index(x) + 1][0]:
                return False
        for x in candleConfig:
            if x[1] not in colorsSoFar:
                colorsSoFar.append(x[1])
        if len(colorsSoFar) == k:
            return True
        else:
            return False
    else:
        return False


# TODO: recursive bactracking algorithm
def candleBacktracking(k, candles, candleConfig, cur):
    if len(candleConfig) == len(candles):
        if isValid(k, candleConfig, len(candles)):
            cur += 1
            return cur
        else:
            return cur

    for candle in candles:
        candleConfig.append(candle)
        cur = candleBacktracking(k, candles, candleConfig, cur)
        del candleConfig[len(candleConfig) - 1]

    return cur


def candlesCounting(k, candles):
    return candleBacktracking(k, candles, [], 0)


if __name__ == '__main__':
    k = 3
    candles = [[1, 1], [3, 2], [2, 2], [4, 3]]
    print(candlesCounting(k, candles))

# print(f'base case is hit success, cur: {cur}')
# print(f'base case is hit failure, cur: {cur}')
# print(f'candleConfig: {candleConfig}, cur: {cur}')
