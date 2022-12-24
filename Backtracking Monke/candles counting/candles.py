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
def isValid(k, candleConfig):
    # check if the candle sequence is strictly increasing in terms of height
    for x in candleConfig[:-1]:
        if not x[0] < candleConfig[candleConfig.index(x) + 1][0]:
            return False
    # check if all colors are present in the candle sequence
    if len(set([x[1] for x in candleConfig])) != k:
        return False
    return True


# TODO: recursive bactracking algorithm
def candleBacktracking(k, candles, candleConfig, cur):
    # the base
    if len(candleConfig) == len(candles):
        return cur
    else:
        # if the candle sequence is valid, increment solution count by one
        if isValid(k, candleConfig):
            cur += 1

    # select a candidate
    for candle in candles:
        # add the candidate to the candle sequence
        candleConfig.append(candle)
        cur = candleBacktracking(k, candles, candleConfig, cur)
        # backtrack by deleting the candidate from the candle sequence
        del candleConfig[len(candleConfig) - 1]
    # return the solution count
    return cur


def candlesCounting(k, candles):
    return candleBacktracking(k, candles, [], 0)


if __name__ == '__main__':
    k = 3
    candles = [[1, 1], [3, 2], [2, 2], [4, 3]]
    print(candlesCounting(k, candles))
