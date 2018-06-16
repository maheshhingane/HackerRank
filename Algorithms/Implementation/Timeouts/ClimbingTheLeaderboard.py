"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""


import sys


def find_rank(scores, score, carry):
    if len(scores) == 0:
        return carry + 1

    mid_index = len(scores) // 2
    mid_score = scores[mid_index]
    if mid_score == score:
        return carry + mid_index + 1
    elif mid_score < score:
        return find_rank(scores[:mid_index], score, carry)
    elif mid_score > score:
        return find_rank(scores[mid_index + 1:], score, carry + mid_index + 1)


def climbingLeaderboard(scores, alice_scores):
    result = []

    unique_scores = []
    min_score = sys.maxsize
    max_score = -1
    for s in scores:
        if s not in unique_scores:
            unique_scores.append(s)
            if s > max_score:
                max_score = s
            if s < min_score:
                min_score = s
    total_unique_scores = len(unique_scores)

    for alice_score in alice_scores:
        if alice_score < min_score:
            result.append(total_unique_scores + 1)
        elif alice_score == min_score:
            result.append(total_unique_scores)
        elif alice_score >= max_score:
            result.append(1)
        else:
            alice_rank = find_rank(unique_scores, alice_score, 0)
            result.append(alice_rank)

    return result


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())
    alice_scores = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice_scores)

    print('\n'.join(map(str, result)))
