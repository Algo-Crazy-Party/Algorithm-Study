# https://www.acmicpc.net/problem/1072
# 게임

# 부동소수점 이슈
# 종료 조건

from decimal import Decimal

def get_win_rate(x, y):
    return int(Decimal(y) / Decimal(x) * 100)

x, y = map(int, input().split())

left = 1
right = x
win_rate = int(Decimal(y) / Decimal(x) * 100)

while left < right:
    mid = left + (right - left) // 2
    if get_win_rate(x + mid, y + mid) > win_rate:
        right = mid
    else:
        left = mid + 1


print(right if get_win_rate(x + right, y + right) > win_rate else -1)