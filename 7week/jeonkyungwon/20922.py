from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
dict = defaultdict(int)
i, max_len = 0, 0

for j in range(N):
    dict[a[j]] += 1

    while dict[a[j]] > K:
        dict[a[i]] -= 1
        i += 1

    max_len = max(max_len, j - i + 1)

print(max_len)
