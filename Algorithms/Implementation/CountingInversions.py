"""
https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def countInversions(arr):
    inversions = 0
    is_arr_sorted = False

    while not is_arr_sorted:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                is_arr_sorted = False
                inversions += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
                break
        else:
            is_arr_sorted = True
    
    return inversions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
