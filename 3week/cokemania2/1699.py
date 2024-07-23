N = int(input())

dp = [0] * (N + 1)
squares = []

for i in range(1, int(N**0.5) + 1):
    squares.append(i * i)

for i in range(1, N + 1):
    dp[i] = i  # 최악의 경우 i개의 1로 표현
    for square in squares:
        if square > i:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[N])