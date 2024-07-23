import sys
input = sys.stdin.readline

N = int(input())

# DP 배열 초기화
dp = [float('inf')] * (N + 1)
dp[0] = 0

# 제곱수 리스트 만들기
squares = []
i = 1
while i * i <= N:
    squares.append(i * i)
    i += 1

# DP 배열 채우기
for i in range(1, N + 1):
    for square in squares:
        if i < square:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[N])