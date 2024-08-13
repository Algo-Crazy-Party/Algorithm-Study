# https://www.acmicpc.net/problem/5557

n = int(input())
n_list = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n)]
dp[0][n_list[0]] = 1
for i in range(1, n):
    for j in range(0, 21):
        if dp[i-1][j] > 0:
            if j + n_list[i] <= 20:
                dp[i][j + n_list[i]] += dp[i-1][j]
            if j - n_list[i] >= 0:
                dp[i][j - n_list[i]] += dp[i-1][j]

print(dp[n-2][n_list[-1]])
    