"""
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    d = defaultdict(list)
    for i in range(len(arr)):
        d[arr[i]].append(i)
    
    triplets = 0
    for item in d.items():
        for index in item[1]:
            second_indices = [i for i in d.get(item[0]*r) or [] if i > index]
            for second_index in second_indices:
                third_indices = [i for i in d.get(arr[second_index]*r) or [] if i > second_index]
                for third_index in third_indices:
                    triplets += 1
    return triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
