from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    dict = defaultdict(list)
    W = input().rstrip()
    K = int(input())

    for i in range(len(W)):
        if W.count(W[i]) >= K:
            dict[W[i]].append(i)

    if not dict:
        print(-1)
    else:
        min_value = 100001
        max_value = 0

        for i in dict:
            for j in range(len(dict[i]) - K + 1):
                min_value = min(min_value, dict[i][j + K - 1] - dict[i][j] + 1)
                max_value = max(max_value, dict[i][j + K - 1] - dict[i][j] + 1)

        print(min_value, max_value)