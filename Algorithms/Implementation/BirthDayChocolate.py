"""
https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""


def solve(n, s, d, m):
    result = 0
    for i in range(n-m+1):
        if sum(s[i:i+m]) == d:
            result += 1
    return result


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().strip().split(' ')))
    d, m = input().strip().split(' ')
    d, m = [int(d), int(m)]

    result = solve(n, s, d, m)

    print(result)
