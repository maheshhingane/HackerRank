"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""


def kangaroo(x1, v1, x2, v2):
    jump_diff = v2 - v1
    if jump_diff >= 0:
        return "NO"
    while x1 < x2:
        x1 += v1
        x2 += v2
    if x1 == x2:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
