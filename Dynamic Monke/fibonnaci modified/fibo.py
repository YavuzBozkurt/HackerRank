#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

# TODO: dynamic programming algorithm
def fiboDP(t1, t2, n, fibo):

    # base cases
    fibo[0] = t1
    fibo[1] = t2

    # 1D tabulation
    for i in range(2, len(fibo)):
        fibo[i] = fibo[i-2] + (fibo[i-1])**2

    # return the n'th value
    return fibo[n-1]


def fibonacciModified(t1, t2, n):
    return fiboDP(0, 1, 6, [0 for i in range(n)])


if __name__ == '__main__':
    t1 = 0
    t2 = 1
    n = 6
    print(fibonacciModified(t1, t2, n))
