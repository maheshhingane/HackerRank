"""
https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    deletions = 0
    char = s[0]
    for i in range(1, len(s)):
        if s[i] == char:
            deletions += 1
        else:
            char = s[i]
    return deletions
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
