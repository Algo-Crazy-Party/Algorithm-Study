# 해설 보긴 했는데,, 아직 코드 이해는 못함,,

# N = int(input())
# home = [list(map(int, input().split())) for _ in range(N)]

# # 파이프의 끝이 해당 칸의 가로, 세로, 대각선에 놓인 경우를 count 하기 위함
# dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

# dp[0][0][1] = 1
# for i in range(2, N):
#     if home[0][i] == 0:
#         dp[0][0][i] = dp[0][0][i-1]

# for r in range(1, N):
#     for c in range(1, N):
#         if home[r][c] == 0 and home[r][c-1] == 0 and home[r-1][c] == 0:
#             dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            
#         if home[r][c] == 0:
#             dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
#             dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]
    
    
# print(sum(dp[i][N-1][N-1] for i in range(3)))