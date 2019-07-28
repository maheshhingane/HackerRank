"""
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxHourGlassSum = 0
    for row in range(len(arr)-2):
        for column in range(len(arr[row])-2):
            hourGlassSum = arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row+1][column+1] + arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2]
            if hourGlassSum > maxHourGlassSum:
                maxHourGlassSum = hourGlassSum
    
    return maxHourGlassSum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
