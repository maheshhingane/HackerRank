"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_apples = 0
    num_oranges = 0
    for i in apples:
        p = a+i
        if t >= p >= s:
            num_apples += 1
    for i in oranges:
        p = b+i
        if t >= p >= s:
            num_oranges += 1
    print(num_apples)
    print(num_oranges)


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))
    orange = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apple, orange)
