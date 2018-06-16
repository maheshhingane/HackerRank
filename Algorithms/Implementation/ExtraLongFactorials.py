"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""


def extraLongFactorials(n):
    factorial_list = [0, 1]
    if n < 1:
        return factorial_list[n]
    while len(factorial_list) <= n:
        factorial_list.append(factorial_list[-1] * len(factorial_list))

    print(factorial_list[-1])


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
