import sys

n=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

dp=[[0]*21 for i in range(n-1)]

dp[0][arr[0]]=1

for i in range(1,n-1):
    for j in range(21):
        if 20>=j-arr[i]>=0:
            dp[i][j-arr[i]] +=dp[i-1][j]
        if 20>=j+arr[i]>=0:
            dp[i][j+arr[i]]+= dp[i-1][j]
print(dp[-1][arr[-1]])
