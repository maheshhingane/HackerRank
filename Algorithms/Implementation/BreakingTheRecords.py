"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""


def breakingRecords(score):
    min_score = max_score = score[0]
    min_crossed = max_crossed = 0
    for i in range(1, len(score)):
        if score[i] > max_score:
            max_score = score[i]
            max_crossed += 1
        elif score[i] < min_score:
            min_score = score[i]
            min_crossed += 1
    return [max_crossed, min_crossed]


if __name__ == '__main__':
    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    print(result)
