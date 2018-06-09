"""
https://www.hackerrank.com/challenges/drawing-book/problem
"""


def pageCount(n, p):
    from_front = p//2
    from_back = ((n-p+1)//2) if n%2==0 else ((n-p)//2)
    return min(from_front, from_back)


if __name__ == '__main__':
    n = int(input())
    p = int(input())

    result = pageCount(n, p)
    print(result)
