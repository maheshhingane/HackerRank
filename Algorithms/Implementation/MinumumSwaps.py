"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def isSorted(arr):
    return arr == sorted(arr)

def minimumSwaps(arr):
    swaps = 0
    l = len(arr)
    while not isSorted(arr):
        for i in range(l):
            if arr[i] != i+1:
                swap(arr, i, arr[i]-1)
                swaps += 1
    
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
