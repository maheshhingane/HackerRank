"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""


def jul_leap_year(year):
    return year%4 == 0


def greg_leap_year(year):
    return (year%400 == 0 or (year%4 ==0 and year%100 != 0))


def solve(year):
    if year < 1918:
        if jul_leap_year(year):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    elif year == 1918:
        return "26.09.1918"
    else:
        if greg_leap_year(year):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)


if __name__ == '__main__':
    year = int(input())

    result = solve(year)

    print(result)
