import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    start, end = 1, X
    result = -1

    while start <= end:
        mid = (start + end) // 2
        new_X = X + mid
        new_Y = Y + mid
        new_Z = (new_Y * 100) // new_X

        if new_Z > Z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)