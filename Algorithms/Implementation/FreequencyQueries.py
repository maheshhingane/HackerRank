"""
https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    data_structure = defaultdict(int)
    for query in queries:
        [operation, operand] = query
        if operation == 1:
            data_structure[operand] += 1
        elif operation == 2:
            if data_structure[operand] > 0:
                data_structure[operand] -= 1
        elif operation == 3:
            if operand in data_structure.values():
                output.append(1)
            else:
                output.append(0)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
