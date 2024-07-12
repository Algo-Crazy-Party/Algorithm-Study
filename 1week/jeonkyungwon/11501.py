import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    profit, max_value = 0, stock[0]

    for i in range(1, N):
        if stock[i] <= max_value:
            profit += max_value - stock[i]
        else:
            max_value = stock[i]

    print(profit)