def solution(n):
    dp = [1] * (n + 1)
    dp[1] = 1
    
    if n == 1:
        return (dp[n] % 1234567)
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
        
    return (dp[n] % 1234567)