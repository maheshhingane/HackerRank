"""
https://www.hackerrank.com/challenges/electronics-shop/problem
"""


def getMoneySpent(keyboards, drives, b):
    keyboards_sorted = sorted([k for k in keyboards if k <= b], reverse=True)
    drives_sorted = sorted([d for d in drives if d <= b], reverse=True)

    max_money_spent = -1
    for k in keyboards_sorted:
        for d in drives_sorted:
            if k + d < max_money_spent or k + d > b:
                continue
            else:
                max_money_spent = k + d

    return max_money_spent


if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
