#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kMarsh' function below.
#
# The function accepts STRING_ARRAY grid as parameter.
#

# TODO: auxiliary rectangle finder algorithm
def rectFound(R):
    # MONKE WANTS TO SEE 2D ARRAY
    print(R[0])
    print(R[1])
    print(R[2])
    print(R[3])
    # initialize list
    rectangle_perimeters = []
    for i in range(len(R)):
        maxProgress = max(R[i])
        # rectangles of width j to consider
        for j in range(1, maxProgress + 1):
            # left corner of the rectangle
            for k in range(len(R[0])):
                # if rectangle width is going out of bounds, break
                if k + j > len(R[0]) - 1:
                    break
                else:
                    # if the rectangle width is within bounds, check if any top width fences align with marshes
                    if -1 in R[i][k:k+j+1]:
                        continue
                    last_row = -1
                    for row in range(i+1, len(R)):
                        # if any of the height fences align with a marsh, then the rectangle is invalid
                        if R[row][k] == -1:
                            break
                        if R[row][k+j] == -1:
                            break
                        # store last row to build the max perimeter rectangle with the given base width (i.e., maximize height)
                        last_row = row
                    # check if any bottom width fences align with marshes
                    if -1 in R[last_row][k:k+j+1]:
                        continue
                    if last_row != -1:
                        # compute rectangle perimeter
                        rectangle_perimeters.append(2*(len(R[i][k:k+j+1])-1)+2*((last_row-i+1)-1))

    # return all unique perimeters computed
    return set(rectangle_perimeters)


# TODO: dynamic programming algorithm
# utilizes sub-problem solutions to solve problems
def marshDP(grid, R):
    """
    :type R: 2D array
    :type grid: 2D array
    """
    for i in range(len(R)):
        # row starts with a marsh
        if grid[i][0] == 'x':
            R[i][0] = -1
        else:
            # row does not start with a marsh
            R[i][0] = 1
        for j in range(1, len(R[0])):
            # if current pos has marsh, set it to -1
            if grid[i][j] == 'x':
                R[i][j] = -1
            else:
                # if previous pos was marsh, set it to 1
                if grid[i][j-1] == 'x':
                    R[i][j] = R[i][j-1] + 2
                else:
                    # if previous pos was no marsh, then the new positions is previous one plus one
                    R[i][j] = R[i][j-1] + 1

    result = rectFound(R)
    # if the set size is 0, then there were no rectangles found
    if len(result) == 0:
        print('impossible')
    else:
        # set size is > 0, return the maximum rectangle perimeter
        print(max(result))
    return


def kMarsh(grid):
    return marshDP(grid, [[0 if grid[i][j] == '.' else -1 for j in range(len(grid[0]))] for i in range(len(grid))])


if __name__ == '__main__':
    grid = [
        ['x', 'x', '.', '.', '.'],
        ['x', 'x', '.', '.', 'x'],
        ['x', '.', 'x', 'x', 'x'],
        ['.', '.', 'x', '.', 'x'],
    ]
    print(kMarsh(grid))
