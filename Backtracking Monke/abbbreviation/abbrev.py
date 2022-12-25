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

    # initialize the progress counter
    progress = -1
    # characters that need to be matched with
    to_match = [char for char in b]

    for i in range(len(b)):
        for j in range(progress + 1, len(a)):
            # the letter in a and b match up
            if a[j] == b[i]:
                # there is a match, indicate that this match is done with a + sign
                to_match[i] = "+"
                # record the progress so that you don't look at the letters you checked previously
                progress = j
                break
            # the letter in a and b do not match up
            else:
                # if the letter in a is lowercase, continue, as this letter can be erased at the end
                if a[i].islower():
                    continue
                # if the letter in a is uppercase, then return false, as capital letters cannot be erased
                else:
                    return False

    # if a match was found for every letter in b, then return true, else, return false
    if len([char for char in to_match if char == "+"]) == len(to_match):
        return True
    else:
        return False


# TODO: recursive backtracking algorithm
def abbrevBacktrack(a, b, pos):
    # base case
    if pos == len(a) - 1:
        return isMatchable(a, b)

    # if the letter is lowercase, then we may convert it
    if not a[pos + 1].isupper():
        for convert in [upper, lower]:
            a = a[:pos + 1] + convert(a[pos + 1]) + a[pos + 2:]
            if abbrevBacktrack(a, b, pos + 1):
                return True
            a = a[:pos + 1] + lower(a[pos + 1]) + a[pos + 2:]
    # if the letter is not lower case, then go to the next letter, as capital letters cannot be converted
    else:
        # if the next call returned true (meaning an abbreviation was found), this should return true as well
        if abbrevBacktrack(a, b, pos + 1):
            return True

    # if no abbreviations were ever found in all possible sequence states, return false
    return False


def abbreviation(a, b):
    return abbrevBacktrack(a, b, -1)


if __name__ == '__main__':
    a = "AbcDE"
    b = "ABDE"
    print(abbrevBacktrack(a, b, -1))
