import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
total = 0

for i in range(1, W - 1):
    start = max(block[:i])
    end = max(block[i + 1:])
    std = min(start, end)

    if std > block[i]:
        total += std - block[i]

print(total)