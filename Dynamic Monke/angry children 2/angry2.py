#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'angryChildren' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY packets
#
# TODO: dynamic programming algorithm
def angryDP(k, packets, U):
    packets = sorted(packets)
    given = []
    # base case
    U[0] = 0
    # add it to given list to measure for unfairness later
    given.append(packets[0])
    # delete it from packets list so that this packet is not given again
    del packets[0]

    for i in range(1, k):
        # calculate unfairness magnitude via recursive formula
        U[i] = U[i - 1] + sum([abs(packets[0] - given[j]) for j in range(len(given))])
        # add it to given list to measure for unfairness later
        given.append(packets[0])
        # delete it from packets list so that this packet is not given again
        del packets[0]
    # return the solution
    return U[k - 1]


def angryChildren(k, packets):
    return angryDP(k, packets, [0 for i in range(len(packets))])


if __name__ == '__main__':
    k = 3
    # packets = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
    packets = [10, 100, 300, 200, 1000, 20, 30]
    print(angryChildren(k, packets))
