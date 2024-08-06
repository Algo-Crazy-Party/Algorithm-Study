# [X][ ] [ ][X] [ ][ ]

# [X][ ] [ ][X] [ ][ ] [ ][ ]
# [ ][X] [X][ ] [X][ ] [ ][X]

# [X][ ] [ ][X] [ ][ ]
# [ ][ ] [ ][ ] [ ][ ]

n = int(input())
dp = [3, 7]
for i in range(2, n):
    dp.append((dp[i-2] + dp[i-1] * 2) % 9901) 
print(dp[-1])
