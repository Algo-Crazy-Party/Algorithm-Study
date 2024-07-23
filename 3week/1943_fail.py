def can_divde(coins):
    money_sum = sum([value * count for value, count in coins])
    if money_sum % 2 != 0:
        return False
    
    target = money_sum // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    
    for value, count in coins:
        # 동전의 가치, 갯수를 반복
        for current_sum in range(target - value + 1):
            if dp[current_sum]:
                for coin_count in range(1, min(count, (target - current_sum) // value) + 1):
                    # 동전을 1개부터 사용 가능한 최대 개수까지 사용하면서 새로운 합계를 만들 수 있는지 확인한다.
                    new_sum = current_sum + coin_count * value
                    dp[new_sum] = True
    return dp[target]

for i in range(3):
    n = int(input())
    coins = []
    for j in range(n):
        unit, number = map(int, input().split())
        coins.append([unit, number])
    if can_divde(coins):
        print(1)
    else:
        print(0)
