#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#


# TODO: auxiliary 
def check(s):
    fives, threes = 0, 0
    for i in range(len(s)):
        if s[i] == '5':
            fives += 1
        else:
            threes += 1
    return ((fives % 3 == 0) and (threes % 5 == 0))

# TODO: greedy algorithm
# NOTE: greedy choice informally is that you erase as few 5s as possible such
#       that newly formed decent number is valid
def decentNumber(n):
    # set decent number
    s = '5'*n

    # if n is divisible by 3, then biggest decent number is all 5s
    if n % 3 == 0:
        print(s)
        return s
    else:
        # delete as few 5s as possible such that # 5s is valid
        numOfFives = n - (n % 3)
        numOfThrees = (n % 3)
        # form new decent number
        s = '5'*numOfFives + '3'*numOfThrees
        # validate decent number
        while not check(s):
            # if not, # 5s is already divisible by 3, delete as few 5s as possible (i.e. delete 3)
            numOfFives -= 3
            numOfThrees += 3
            # 5s are always to the left, if # 5s < 0, then all possible
            # deletions have been done till now, and yet check still failed,
            # so return -1
            if numOfFives >= 0:
                # form the new decent number
                s = '5'*numOfFives + '3'*numOfThrees
            else:
                print(-1)
                return -1
        print(s)
        return s

# HackerRank validated answer
# exercise link: https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?isFullScreen=true 
# driver program
if __name__ == '__main__':
    n = input()
    decentNumber(int(n))
