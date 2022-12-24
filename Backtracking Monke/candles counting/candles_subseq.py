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
    for x in candleConfig[:-1]:
        if not x[0] < candleConfig[candleConfig.index(x) + 1][0]:
            return False
    if len(set([x[1] for x in candleConfig])) != k:
        return False
    return True


# TODO: recursive bactracking algorithm
def candleBacktracking(k, candles, candleConfig, cur):
    if len(candleConfig) == len(candles):
        return cur
    else:
        if isValid(k, candleConfig):
            cur += 1

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
