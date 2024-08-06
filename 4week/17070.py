HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2

HORIZONTAL_MOVES = [(HORIZONTAL, 0, 1), (DIAGONAL, 1, 1)]
VERTICAL_MOVES = [(VERTICAL, 1, 0), (DIAGONAL, 1, 1)]
DIAGONAL_MOVES = [(HORIZONTAL, 0, 1), (VERTICAL, 1, 0), (DIAGONAL, 1, 1)]

def dfs(arr, direction, y, x, n):
    if y == n - 1 and x == n - 1:
        return 1
    cases = []
    if direction == HORIZONTAL: # 수평 파이프
        for d, dy, dx in HORIZONTAL_MOVES:
            cases.append([d, y + dy, x + dx])
    elif direction == VERTICAL: # 수직 파이프
        for d, dy, dx in VERTICAL_MOVES:
            cases.append([d, y + dy, x + dx])
    else: # 대각선 파이프
        for d, dy, dx in DIAGONAL_MOVES:
            cases.append([d, y + dy, x + dx])

    count = 0
    for case in cases:
        if case[1] >= n or case[2] >= n or arr[case[1]][case[2]] == '1':
            continue
        if case[0] == DIAGONAL:
            if arr[case[1]-1][case[2]] == '1' or arr[case[1]][case[2]-1] == '1':
                continue
        count += dfs(arr, case[0], case[1], case[2], n)
    return count

n = int(input())
arr = [input().split(' ') for _ in range(n)]
arr[0][0], arr[0][1] = '1', '1'
print(dfs(arr, HORIZONTAL, 0, 1, n))
