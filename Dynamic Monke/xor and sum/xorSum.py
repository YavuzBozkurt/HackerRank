#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

# TODO: dynamic programming algorithm
def xorSumDP(a, b, memo):
    # convert the binaries into integers
    a = int(a, 2)
    b = int(b, 2)

    # base case
    memo[0] = (a ^ b)

    for i in range(1, len(memo)):
        # store the computation to re-use in the next iteration
        memo[i] = memo[i - 1] + (a ^ (b << i))
    # return the solution
    return memo[len(memo) - 1] % (10 ** 9 + 7)


def xorAndSum(a, b):
    # Write your code here
    return xorSumDP(a, b, [0 for i in range(314159 + 1)])


if __name__ == '__main__':
    a = "10"
    b = "1010"
    print(xorAndSum(a, b))
