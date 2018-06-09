"""
https://www.hackerrank.com/challenges/counting-valleys/problem
"""


def countingValleys(n, hike):
    mountains = valleys = 0
    is_mountain = is_valley = False
    altitude = 0

    for step in hike:
        if step == "U":
            if not is_mountain and altitude == 0:
                is_mountain = True
            altitude += 1
        else:
            if not is_valley and altitude == 0:
                is_valley = True
            altitude -= 1
        if altitude == 0:
            if is_mountain:
                mountains += 1
                is_mountain = False
            elif is_valley:
                valleys += 1
                is_valley = False

    return valleys


if __name__ == '__main__':
    n = int(input())
    s = input()

    result = countingValleys(n, s)
    print(result)
