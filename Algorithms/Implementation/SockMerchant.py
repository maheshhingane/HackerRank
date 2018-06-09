"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""


def sockMerchant(n, ar):
    pairs = 0
    ar_set = set(ar)
    for i in ar_set:
        cnt = ar.count(i)
        pairs += (cnt//2)
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
