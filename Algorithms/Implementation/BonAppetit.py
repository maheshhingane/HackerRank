"""
https://www.hackerrank.com/challenges/bon-appetit/problem
"""


def bonAppetit(k, bill, b):
    total_bill = sum(bill)
    common_bill = total_bill - bill[k]
    annas_portion = common_bill // 2
    if b == annas_portion:
        return "Bon Appetit"
    else:
        return b - annas_portion


if __name__ == '__main__':
    [n, k] = list(map(int, input().split()))
    bill = list(map(int, input().split()))
    b = int(input())

    print(bonAppetit(k, bill, b))
