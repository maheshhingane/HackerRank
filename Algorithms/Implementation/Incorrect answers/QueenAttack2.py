"""
https://www.hackerrank.com/challenges/queens-attack-2/problem
"""


def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles_in_same_row = sorted([o for o in obstacles if o[0] == r_q], key=lambda x: x[1])
    obstacles_in_same_column = sorted([o for o in obstacles if o[1] == c_q], key=lambda x: x[0])
    obstacles_in_diagonal = sorted([o for o in obstacles if abs(o[0] - r_q) == abs(o[1] - c_q)],
                                   key=lambda x: (x[0], x[1]))

    for o_same_row in obstacles_in_same_row:
        if o_same_row[1] < c_q:
            continue
        right_obstacle = o_same_row
        break
    else:
        right_obstacle = [r_q, n + 1]

    for o_same_row in obstacles_in_same_row[::-1]:
        if o_same_row[1] > c_q:
            continue
        left_obstacle = o_same_row
        break
    else:
        left_obstacle = [r_q, 0]

    for o_same_column in obstacles_in_same_column:
        if o_same_column[0] < r_q:
            continue
        top_obstacle = o_same_column
        break
    else:
        top_obstacle = [n + 1, c_q]

    for o_same_column in obstacles_in_same_column[::-1]:
        if o_same_column[0] > r_q:
            continue
        down_obstacle = o_same_column
        break
    else:
        down_obstacle = [0, c_q]

    for o_diagonal in obstacles_in_diagonal[::-1]:
        if o_diagonal[0] < r_q or o_diagonal[1] > c_q:
            continue
        top_left_obstacle = o_diagonal
        break
    else:
        r = r_q
        c = c_q
        while r <= n and c >= 1:
            r += 1
            c -= 1
        top_left_obstacle = [r, c]

    for o_diagonal in obstacles_in_diagonal:
        if o_diagonal[0] < r_q or o_diagonal[1] < c_q:
            continue
        top_right_obstacle = o_diagonal
        break
    else:
        r = r_q
        c = c_q
        while r <= n and c <= n:
            r += 1
            c += 1
        top_right_obstacle = [r, c]

    for o_diagonal in obstacles_in_diagonal[::-1]:
        if o_diagonal[0] > r_q or o_diagonal[1] > c_q:
            continue
        bottom_left_obstacle = o_diagonal
        break
    else:
        r = r_q
        c = c_q
        while r >= 1 and c >= 1:
            r -= 1
            c -= 1
        bottom_left_obstacle = [r, c]

    for o_diagonal in obstacles_in_diagonal:
        if o_diagonal[0] > r_q or o_diagonal[1] < c_q:
            continue
        bottom_right_obstacle = o_diagonal
        break
    else:
        r = r_q
        c = c_q
        while r >= 1 and c <= n:
            r -= 1
            c += 1
        bottom_right_obstacle = [r, c]

    # Calculate
    result = 0
    result += (c_q - left_obstacle[1] - 1)
    result += (right_obstacle[1] - c_q - 1)
    result += (top_obstacle[0] - r_q - 1)
    result += (r_q - down_obstacle[0] - 1)
    result += (c_q - top_left_obstacle[1] - 1)
    result += (top_right_obstacle[0] - r_q - 1)
    result += (r_q - bottom_left_obstacle[0] - 1)
    result += (bottom_right_obstacle[1] - c_q - 1)

    return result


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
