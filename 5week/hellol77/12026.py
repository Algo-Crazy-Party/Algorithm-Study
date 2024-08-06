import sys

n= int(sys.stdin.readline())
block = sys.stdin.readline().strip()
dp=[sys.maxsize] * n

dp[0]=0

for i in range(n):
    for j in range(i+1,n):
        if block[i] == 'B' and block[j] == 'O':
            dp[j] = min(dp[i] + (j-i)**2, dp[j])
        if block[i] == 'O' and block[j] == 'J':
            dp[j] = min(dp[i] + (j-i)**2, dp[j])
        if block[i] == 'J' and block[j] == 'B':
            dp[j] = min(dp[i] + (j-i)**2, dp[j])

if dp[n-1]==sys.maxsize:
    print(-1)
else:
    print(dp[n-1])
