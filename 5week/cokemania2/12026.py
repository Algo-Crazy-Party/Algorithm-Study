n = int(input())
s = input()

answer = 0
x = ["B", "O", "J"]
index = 0
dp = [1000 * 1000 + 1] * n
dp[0] = 0

for i in range(1, len(s)):
    for j in range(i):
        if s[i] == 'B' and s[j] == 'J' or s[i] == 'O' and s[j] == 'B' or s[i] == 'J' and s[j] == 'O':
            dp[i] = min(dp[i], dp[j] + (i - j) * (i - j))
if dp[-1] == 1000 * 1000 + 1:
    print(-1)
else:
    print(dp[-1])