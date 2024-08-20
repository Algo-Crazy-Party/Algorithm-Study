# https://www.acmicpc.net/problem/20922

from collections import defaultdict

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
left, right = 0, 0
n_count = defaultdict(int)

answer = 0
while right < n:
    if n_count[n_list[right]] == k:
        n_count[n_list[left]] -= 1
        left += 1
    else:
        n_count[n_list[right]] += 1
        right += 1
    answer  = max(answer, right - left)
print(answer)
