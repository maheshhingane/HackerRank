"""
https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    i = 0
    total_price = 0
    while i < len(sorted_prices):
        if total_price + sorted_prices[i] > k:
            break
        total_price += sorted_prices[i]
        i += 1
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
