"""
https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""


def nonDivisibleSubset(k, S):
    S_dash = []
    for index in range(len(S)):
        for next_index in range(index + 1, len(S)):
            if (S[index] + S[next_index]) % k != 0:
                S_dash.append(S[index])
                S_dash.append(S[next_index])

    return len(set(S_dash))


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    print(result)
