"""
https://www.hackerrank.com/challenges/between-two-sets/problem
"""


def getTotalX(a, b):
    max_in_a = max(a)
    min_in_b = min(b)
    if max_in_a > min_in_b:
        return 0
    between_numbers = []
    for number in range(max_in_a, min_in_b+1):
        if all(number % i == 0 for i in a) and all(i % number == 0 for i in b):
            between_numbers.append(number)
    return len(between_numbers)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)
