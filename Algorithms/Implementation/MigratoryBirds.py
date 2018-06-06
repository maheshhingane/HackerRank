"""
https://www.hackerrank.com/challenges/migratory-birds/problem
"""


def migratoryBirds(n, ar):
    d = {}
    max_count = 0
    max_id = 0
    for i in range(1, 6):
        d[i] = ar.count(i)
        if d[i] > max_count:
            max_count = d[i]
            max_id = i
    return max_id


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(n, ar)

    print(result)
