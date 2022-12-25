#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# TODO: auxiliary algorithm to check if a given value is prime
def isPrime(val):
    if val < 2:
        return False

    for number in range(2, val):
        # if val is divisible by number, then val is not prime
        if val % number == 0:
            return False

    # all checks passed, thus, val is prime
    return True


# TODO: solution validation algorithm
def xorIsPrime(solutions, multiset, a):

    for element in solutions:
        count1 = Counter(element)
        count2 = Counter(multiset)
        if count1 == count2:
            return False

    considered = [val for val in a]
    for i in range(len(multiset)):
        if multiset[i] in considered:
            considered[considered.index(multiset[i])] = -1000000000
        else:
            return False

    xor_result = 0
    for value in multiset:
        xor_result = xor_result ^ value

    if isPrime(xor_result):
        return True
    else:
        return False


# TODO: recursive backtracking algorithm
def XorBacktrack(n, a, multiset, solutions, cur):

    if len(multiset) >= 1:
        if xorIsPrime(solutions, multiset, a):
            solutions.append([x for x in multiset])
            cur += 1
        else:
            cur += 0

    # base case
    if len(a) == len(multiset):
        return cur

    for i in range(len(a)):
        multiset.append(a[i])
        cur = XorBacktrack(n, a, multiset, solutions, cur)
        del multiset[-1]

    return cur % (10**9 + 7)


def primeXor(q, n, a):
    return XorBacktrack(n, a, [], [], 0)


if __name__ == '__main__':
    q = 1
    n = 3
    a = [3511, 3671, 4153]
    print(primeXor(q, n, a))
