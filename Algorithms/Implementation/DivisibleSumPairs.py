"""
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""


def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(len(ar) - 1):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
