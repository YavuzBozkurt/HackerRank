#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

# TODO: dynamic programming algorithm
def stockDP(prices, goods, T):
    # base case
    T[0] = 0
    for i in range(1, len(T)):
        # if there exists a future pinnacle point, buy good
        if len([prices[j] for j in range(i, len(prices)) if prices[j] > prices[i-1]]) >= 1:
            T[i] = T[i-1] - prices[i-1]
            # to indicate that you bought it, add "+" sign
            goods.append("+")
        # == 0
        else:
            # either at a pinnacle point in stock
            if len(goods) >= 1:
                T[i] = T[i-1] + prices[i-1]*len(goods)
                # sold all goods
                goods = []
            # or at a point in which trading in future is not favourable for now (i.e., buying causes loss for now)
            # for profit optimization, we don't buy in these cases
            else:
                # don't do trading for this day
                T[i] = T[i-1]
                continue
    return T[len(T)-1]


def stockmax(prices):
    # Write your code here
    return stockDP(prices, [], [-1 for i in range(len(prices) + 1)])


if __name__ == '__main__':
    print(stockmax([5, 1, 5, 10, 2, 1, 2]))
