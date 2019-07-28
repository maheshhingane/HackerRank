"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def findMedian(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst)%2 != 0:
        return sorted_lst[len(sorted_lst)//2]
    else:

        return (sorted_lst[len(sorted_lst)//2] + sorted_lst[len(sorted_lst)//2 + 1])/2


def activityNotifications(expenditure, d):
    result = 0
    i = d
    while i < len(expenditure):
        median = findMedian(expenditure[i-d:i])
        if expenditure[i] >= 2*median:
            result += 1
        i += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

