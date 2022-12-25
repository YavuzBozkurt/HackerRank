#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

# TODO: auxiliary function to convert char to uppercase
def upper(char):
    return char.upper()


# TODO: auxiliary function to convert char to lowercase
def lower(char):
    return char.lower()


# TODO: solution validation algorithm
def isMatchable(a, b):
    progress = -1
    to_match = [char for char in b]

    for i in range(len(b)):
        for j in range(progress + 1, len(a)):
            if a[j] == b[i]:
                to_match[i] = "+"
                progress = j
                break
            else:
                if a[i].islower():
                    continue
                else:
                    return False

    if len([char for char in to_match if char == "+"]) == len(to_match):
        return True
    else:
        return False


# TODO: recursive backtracking algorithm
def abbrevBacktrack(a, b, pos):
    if pos == len(a) - 1:
        return isMatchable(a, b)

    if not a[pos + 1].isupper():
        for convert in [upper, lower]:
            a = a[:pos + 1] + convert(a[pos + 1]) + a[pos + 2:]
            if abbrevBacktrack(a, b, pos + 1):
                return True
            a = a[:pos + 1] + lower(a[pos + 1]) + a[pos + 2:]
    else:
        if abbrevBacktrack(a, b, pos + 1):
            return True

    return False


def abbreviation(a, b):
    return abbrevBacktrack(a, b, -1)


if __name__ == '__main__':
    a = "AbcDE"
    b = "ABDE"
    print(abbrevBacktrack(a, b, -1))
