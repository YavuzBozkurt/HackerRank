#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# TODO: validation function
def Valid():
    return 0


# TODO: recursive backtracking function
def unfairBacktrack(k, arr, unfairArr, pos):
    return 0


def maxMin(k, arr):
    unfairArr = []
    result = unfairBacktrack(k, arr, unfairArr, -1)
    print(result)
    return result


# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = 2
    arr = [1, 4, 7, 2]

    maxMin(k, arr)
