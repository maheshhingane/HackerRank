"""
https://www.hackerrank.com/challenges/grading/problem
"""

import os


def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        else:
            possible_rounding = 5 - (grade % 5)
            if possible_rounding < 3:
                new_grades.append(grade + possible_rounding)
            else:
                new_grades.append(grade)
    return new_grades


if __name__ == '__main__':
    n = int(input())
    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
